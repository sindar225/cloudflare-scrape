import cfscrape

scraper = cfscrape.create_scraper()
print(scraper.get("https://rsbuddy.com/static/home/img/paypal.png").content)
