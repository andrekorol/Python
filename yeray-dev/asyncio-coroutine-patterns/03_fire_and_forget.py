"""
A recursive function solves a problem by simplifying the input until
we arrive at a base trivial case and then combining the results up the stack.
Assume we want to calculate the number of comments of a particular post in
Hacker News by recursively aggregating the number of descendents.
"""

import argparse
import asyncio
import logging
from datetime import datetime
from random import random
from urllib.parse import parse_qs, urlparse

import aiohttp
import async_timeout

LOGGER_FORMAT = '%(asctime)s %(message)s'
URL_TEMPLATE = 'https://hacker-news.firebaseio.com/v0/item/{}.json'
FETCH_TIMEOUT = 10
MIN_COMMENTS = 5

parser = argparse.ArgumentParser(
    description='Calculate the comments of a Hacker News post.'
)
parser.add_argument('--id', type=int, default=8863,
                    help='ID of the post in HN, defaults to 8863')
parser.add_argument('--url', type=str, help='URL of a post in HN')
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


async def log_post(post):
    """Simulate logging of a post."""
    await asyncio.sleep(random() * 3)
    # log.info('Post logged: {}'.format(post))
    log.info('Post logged')


async def post_number_of_comments(loop, session, post_id):
    """Retrieve data for current post and recursively for all comments.
    """
    url = URL_TEMPLATE.format(post_id)
    start = datetime.now()
    response = await fetch(session, url)
    log.debug('{:^6} > Fetching of {} took {} seconds'.format(
        post_id, url, (datetime.now() - start).total_seconds()
    ))

    if 'kids' not in response:  # base case, there are no comments
        return 0

    # calculate this post's comments as number of comments
    number_of_comments = len(response['kids'])

    # create recursive tasks for all comments
    log.debug('{:^6} > Fetching {} child posts'.format(
        post_id, number_of_comments
    ))
    tasks = [post_number_of_comments(
        loop, session, kid_id
    ) for kid_id in response['kids']]

    # schedule the tasks and retrieve results
    results = await asyncio.gather(*tasks)

    # reduce the descendents comments and add it to this post's
    number_of_comments += sum(results)
    log.debug('{:^6} > {} comments'.format(post_id, number_of_comments))

    # Log if number of comments is over a threshold
    if number_of_comments > MIN_COMMENTS:
        asyncio.create_task(log_post(response))
        # asyncio.ensure_future(log_post(response))

    return number_of_comments


def id_from_HN_url(url):
    """Return the value of the `id` query arg of a URL if present, or None."""
    parse_result = urlparse(url)
    try:
        return parse_qs(parse_result.query)['id'][0]
    except (KeyError, IndexError):
        return None


async def main(loop, post_id):
    """Async entry point coroutine."""
    start = datetime.now()
    async with aiohttp.ClientSession(loop=loop) as session:
        start = datetime.now()
        comments = await post_number_of_comments(loop, session, post_id)
        log.info(
            '> Calculating comments took {:.2f} seconds and {} fetches'.format(
                (datetime.now() - start).total_seconds(), fetch_counter
            )
        )
    return comments


if __name__ == '__main__':
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    post_id = id_from_HN_url(args.url) if args.url else args.id

    loop = asyncio.get_event_loop()
    comments = loop.run_until_complete(main(loop, post_id))
    log.info('-- Post {} has {} comments'.format(post_id, comments))

    pending_tasks = [
        task for task in asyncio.all_tasks(loop) if not task.done()
    ]
    loop.run_until_complete(asyncio.gather(*pending_tasks))

    loop.close()
