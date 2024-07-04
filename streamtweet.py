from ntscraper import Nitter

scraper = Nitter(log_level=1, skip_instance_check=False)

tweets = scraper.get_tweets("CMOfficeUP", mode="user", number=1)
print(tweets)