from ntscraper import Nitter
import psycopg2
from psycopg2 import Error
from config import db_config
from accounts import get_accounts


def insert_tweets(account, tweets_data):
    config = db_config()
    try:
        connection = psycopg2.connect(**config)
        cursor = connection.cursor()

        for tweet in tweets_data:
            username = tweet.get('user', {}).get('name')
            tweet_text = tweet.get('text')

            cursor.execute("""
                INSERT INTO tweets (username, tweet_text)
                VALUES (%s, %s)
            """, (username, tweet_text))

        connection.commit()
        print(f"{len(tweets_data)} tweets inserted successfully into PostgreSQL for account: {account}")

    except (Exception, Error) as error:
        print(f"Error while inserting tweets for account {account}: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


scraper = Nitter(log_level=1, skip_instance_check=False)
accounts = get_accounts()

for account in accounts:
    tweets = scraper.get_tweets(account, mode="user", number=100)
    tweets_data = tweets['tweets']
    insert_tweets(account, tweets_data)