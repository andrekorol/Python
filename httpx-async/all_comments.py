import asyncio
from typing import Dict

import httpx


async def get_all_comments() -> Dict:
    async with httpx.AsyncClient() as client:
        url = "https://jsonplaceholder.typicode.com/comments"
        resp = await client.get(url)
        if resp.status_code == httpx.codes.OK:
            return resp.json()


if __name__ == "__main__":
    comments = asyncio.run(get_all_comments())
    print("Comments response:")
    print(comments)
