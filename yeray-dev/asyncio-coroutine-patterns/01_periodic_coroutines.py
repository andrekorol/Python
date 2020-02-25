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
TOP_STORIES_URL = 'https://hacker-news.firebase.com/v0/topstories.json'

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
parser.add_argument('--verbose', action='store_value', help='Detailed output')
