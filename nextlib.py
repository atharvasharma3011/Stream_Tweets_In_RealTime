import aiohttp
import asyncio

async def fetch_tweets(session, username, limit):
    url = f"http://api.ntscraper.com/fetch_tweets?username={username}&limit={limit}"
    async with session.get(url) as response:
        return await response.json()

async def fetch_all_tweets(accounts, limit):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_tweets(session, account, limit) for account in accounts]
        return await asyncio.gather(*tasks)

accounts = ['@narendramodi', '@another_account', '@third_account']
tweets_per_account = 100

# Fetch tweets concurrently
all_tweets = asyncio.run(fetch_all_tweets(accounts, tweets_per_account))

# Process the fetched tweets
for account, tweets in zip(accounts, all_tweets):
    print(f"Fetched {len(tweets)} tweets from {account}.")
