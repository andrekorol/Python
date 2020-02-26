"""
An example of periodically scheduling coroutines using an infinite loop of
awaiting and sleeping.
"""

import asyncio
import argparse
import logging
from datetime import datetime

import aiohttp
import async_timeout

LOGGER_FORMAT = '%(asctime)s %(message)s'
URL_TEMPLATE = 'https://hacker-news.firebaseio.com/v0/item/{}.json'
TOP_STORIES_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json'
FETCH_TIMEOUT = 10

parser = argparse.ArgumentParser(
    description='Calculate the number of comments of the top stories in HN.'
)
parser.add_argument(
    '--period', type=int, default=5, help='Number of seconds between poll'
)
parser.add_argument(
    '--limit', type=int, default=5,
    help='Number of new stories to calculate comments for'
)
parser.add_argument('--verbose', action='store_true', help='Detailed output')

logging.basicConfig(format=LOGGER_FORMAT, datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

fetch_counter = 0


async def fetch(session, url):
    """Fetch a URL using aiohttp returning parsed JSON response.
    As suggested by the aiohttp docs, we reuse the session.
    """
    global fetch_counter
    with async_timeout.timeout(FETCH_TIMEOUT):
        fetch_counter += 1
        async with session.get(url) as response:
            return await response.json()


async def post_number_of_comments(loop, session, post_id):
    """Retrieve data for current post and recursively for all comments."""
    url = URL_TEMPLATE.format(post_id)
    response = await fetch(session, url)

    if 'kids' not in response:  # base case, there are no comments
        return 0

    # calculate this post's comments as number of comments
    number_of_comments = len(response['kids'])

    # create recursive tasks for all comments
    tasks = [post_number_of_comments(
        loop, session, kid_id
    ) for kid_id in response['kids']]

    # schedule the tasks and retrieve results
    results = await asyncio.gather(*tasks)

    # reduce the descendents comments and add it to this post's
    number_of_comments += sum(results)
    log.debug('{:^6} > {} comments'.format(post_id, number_of_comments))

    return number_of_comments


async def get_comments_of_top_stories(loop, session, limit, iteration):
    """Retrieve the top stories in HN."""
    response = await fetch(session, TOP_STORIES_URL)
    tasks = [post_number_of_comments(
        loop, session, post_id
    ) for post_id in response[:limit]]

    results = await asyncio.gather(*tasks)
    for post_id, num_comments in zip(response[:limit], results):
        log.info('Post {} has {} comments ({})'.format(
            post_id, num_comments, iteration
        ))


async def poll_top_stories_for_comments(loop, session, period, limit):
    """Periodically poll for new stories and retrieve number of comments."""
    global fetch_counter
    iteration = 1
    while True:
        start = datetime.now()
        log.info('Calculating comments for top {} stories. ({})'.format(
            limit, iteration
        ))
        asyncio.create_task(
            get_comments_of_top_stories(loop, session, limit, iteration)
        )

        log.info(
            '> Calculating comments took {:.2f} seconds and {} fetches'.format(
                (datetime.now() - start).total_seconds(), fetch_counter
            )
        )
        log.info('Waiting for {} seconds...'.format(period))
        iteration += 1
        fetch_counter = 0
        await asyncio.sleep(period)


async def main(loop, period, limit):
    """Async entry point coroutine."""
    async with aiohttp.ClientSession(loop=loop) as session:
        comments = await poll_top_stories_for_comments(loop, session, period,
                                                       limit)

        return comments


if __name__ == "__main__":
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, args.period, args.limit))

    loop.close()
