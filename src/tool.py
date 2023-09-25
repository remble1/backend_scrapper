import asyncio
import aiohttp

api = "https://www.boredapi.com/api/activity/"

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()