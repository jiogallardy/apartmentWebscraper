from webScraper import WebScraper
from pushNotifier import PushNotifier
import time


url = 'https://www.equityapartments.com/los-angeles/marina-del-rey/marina-41-apartments#/'
web_scraper = WebScraper(url, "Marina 41")
apartments = web_scraper.findAboveAFloor(10)
print(apartments)
api_token = 'a6v5rk5g8j3hi9x84axhkupojc5msf'  # Your API Token
user_key = 'ujw4rnukf4xtr8bq81gapwc13brdqd'  # Your User Key

push_notifier = PushNotifier(api_token, user_key) 

web_scraper.monitorChangesOnSetRange(10, push_notifier)


