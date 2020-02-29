import asyncio
from typing import Dict

import httpx


async def get_post_from_comment(comment_id: int):
    REST_API = "https://jsonplaceholder.typicode.com"
    async with httpx.AsyncClient(base_url=REST_API) as api:
        resp = await api.get(f"comments/{comment_id}")
        resp.raise_for_status()
        comment = resp.json()
        resp = await api.get(f"posts/{comment['postId']}")
        resp.raise_for_status()
        return resp.json()

if __name__ == "__main__":
    post = asyncio.run(get_post_from_comment(1))
    print(post)

    # will raise
    post = asyncio.run(get_post_from_comment(-1))
