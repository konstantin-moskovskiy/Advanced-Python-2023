import asyncio
import aiohttp
import os

async def download_image(session, url, filename):
    async with session.get(url) as response:
        with open(filename, 'wb') as f:
            f.write(await response.content.read())

async def download_images(num_images):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, num_images+1):
            url = f'https://picsum.photos/200/300?random={i}'
            filename = f'artifacts/image_{i}.jpg'
            tasks.append(asyncio.ensure_future(download_image(session, url, filename)))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    num_images = 10
    asyncio.run(download_images(num_images))