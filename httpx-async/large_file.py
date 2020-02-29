import asyncio
from cgi import parse_header
from os.path import join
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse

import aiofiles
import httpx
from httpx import AsyncClient


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

if __name__ == '__main__':
    url = 'https://www.dropbox.com/s/a0lj1ddd54ns8qy/' \
        'All-Age-Faces%20Dataset.zip?dl=1'
    # url = 'http://eforexcel.com/wp/wp-content/uploads/2017/07/' \
    #     '1500000%20Sales%20Records.7z'
    filename = asyncio.run(download_file(url))
    print(f"Downloaded '{filename}' succesfully.")
