import asyncio
import time
from collections import namedtuple
from concurrent.futures import FIRST_COMPLETED

import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))
SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def aiohttp_get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    json_response = await aiohttp_get_json(service.url)
    ip = json_response[service.ip_attr]

    return '{} finished with result: {}, took {:.2f} seconds'.format(
        service.name, ip, time.time() - start
    )


async def main():
    futures = [fetch_ip(service) for service in SERVICES]
    done, _ = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED
    )   # Unused pending futures

    print(done.pop().result())


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(main())
ioloop.close()
