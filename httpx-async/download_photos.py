import asyncio
from cgi import parse_header
from os import makedirs
from os.path import join
from pathlib import Path
from typing import Optional, Sequence
from urllib.parse import unquote, urlparse

import aiofiles
import httpx
from httpx import AsyncClient

DOG_API = "https://dog.ceo/api/breeds"


def get_photos_urls(number: int = 3) -> Sequence[str]:
    """Get the URLs for a `number` of random images on the Dog CEO API."""
    if number > 50:
        error_msg = "The maximum number of images returned by the API is 50."
        error_msg += "\nMore info here: " \
            "https://github.com/ElliottLandsborough/dog-ceo-api/pull/3."
        raise ValueError(error_msg)

    resp = httpx.get(f"{DOG_API}/image/random/{number}")
    resp.raise_for_status()
    urls = {image_url for image_url in resp.json()["message"]}
    return urls


async def download_file(url: str,
                        client: Optional[AsyncClient] = AsyncClient(),
                        filename: Optional[str] = "",
                        folder: Optional[str] = "") -> str:
    """Use an async `client` to download the file found at `url`
    and save it to `folder` as `filename`"""
    async with client.stream('GET', url) as resp:
        resp.raise_for_status()
        if not filename:
            params = {}
            if 'Content-Disposition' in resp.headers:
                content_disposition = resp.headers.get('Content-Disposition')
                _, params = parse_header(content_disposition)
            if params and 'filename*' in params:
                filename_str = params['filename*']
                encoding, filename = filename_str.split("''")
                filename = unquote(filename, encoding)
            elif params and 'filename' in params:
                filename = unquote(params['filename'])
            else:
                parsed_url = urlparse(url)
                filename = unquote(Path(parsed_url.path).name)

        async with aiofiles.open(join(folder, filename), 'wb') as f:
            async for chunk in resp.aiter_bytes():
                if chunk:
                    await f.write(chunk)

    return filename


# async def download(client: AsyncClient, url: str, folder: str) -> None:
    # """Use an async `client` to download the file found at `url`
    # and save it to `folder`."""
#     filename = url.split("/")[-1]
#     resp = await client.get(url)
#     resp.raise_for_status()
#     async with aiofiles.open(join(folder, filename), "wb") as f:
#         await f.write(resp.content)


async def download_all_photos(urls: Sequence[str], out_dir: str) -> None:
    """Asynchronously download the files from the `urls` and save
    them to `out_dir`."""
    makedirs(out_dir, exist_ok=True)
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(
            download_file(url, client, folder=out_dir)) for url in urls]

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = get_photos_urls(50)
    asyncio.run(download_all_photos(urls, "dog_photos"))
