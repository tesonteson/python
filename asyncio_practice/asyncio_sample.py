"""
IOバウンドとは、InputとOutputに時間が生じる処理のこと。
具体的には、データやファイルの読み込みの時間が生じること

CPUバウンドとは、処理を継続して行う処理のこと。
具体的には、forループなど。
"""

import asyncio
import aiohttp
import requests
import time

loop = asyncio.get_event_loop()

async def worker(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(time.time())

if __name__ == "__main__":
    loop.run_until_complete(asyncio.gather(
        worker("https://qiita.com/suikabar/items/32c6215d3c0535aba328"),
        worker("https://qiita.com/suikabar/items/32c6215d3c0535aba328")
    ))
    loop.close()
