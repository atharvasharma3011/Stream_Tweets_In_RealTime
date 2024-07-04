from ntscraper import Nitter
import pandas as pd

scraper = Nitter(log_level=1, skip_instance_check=False)

tweets = scraper.get_tweets("narendramodi", mode="user", number=10)

tweets_data = tweets['tweets']

df = pd.DataFrame(tweets_data)

excel_file = "power.xlsx"  
df.to_excel(excel_file, index=False)

print(f"Data saved to {excel_file}")