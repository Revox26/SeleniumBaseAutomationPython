import random
import requests


class RandomWebsiteGenerator:
    def __init__(self):
        self.domains = [
            "https://www.google.com", "https://www.facebook.com", "https://www.amazon.com",
            "https://www.youtube.com", "https://www.wikipedia.org", "https://www.reddit.com",
            "https://www.twitter.com", "https://www.instagram.com", "https://www.tiktok.com",
            "https://www.twitch.tv", "https://www.netflix.com", "https://www.hulu.com",
            "https://www.disneyplus.com", "https://www.apple.com", "https://www.microsoft.com",
            "https://www.amazon.com", "https://www.ebay.com", "https://www.etsy.com",
            "https://www.walmart.com", "https://www.target.com", "https://www.bestbuy.com",
            "https://www.homedepot.com", "https://www.lowes.com", "https://www.cnn.com",
            "https://www.nytimes.com", "https://www.washingtonpost.com", "https://www.bbc.com",
            "https://www.theguardian.com", "https://www.espn.com", "https://www.nfl.com",
            "https://www.nba.com", "https://www.mlb.com", "https://www.nhl.com",
            "https://www.wikipedia.org", "https://www.quora.com",
            "https://www.stackoverflow.com", "https://www.github.com",
            "https://www.foxstudiosscratch.xyz", "https://github.com/Fox-Studios-Scratch",
            "https://www.youtube.com/@aidenjamesyt"
        ]

    def generate_random_website(self):
        while True:
            domain = random.choices(self.domains, k=1)[0]
            path = random.choice(["/", "/about", "/contact", "/products", "/services"])
            website_url = f"{domain}{path}"

            # # Use requests.head for faster check
            # response = requests.head(website_url)
            #
            # if response.status_code == 200:
            return website_url

    @staticmethod
    def generate_random_notification_title():
        random_category_title = ["New Update Available", "Special Offer", "Event Reminder", "Breaking News"]
        random_title = random.choice(random_category_title)
        return random_title

    @staticmethod
    def generate_random_notification_text():
        random_category_text = ["Check out the latest features!", "Limited time offer just for you.", "Don't forget our upcoming event.", "Stay tuned for important updates."]
        random_text = random.choice(random_category_text)
        return random_text
