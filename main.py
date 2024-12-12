import modules.scraper_utils as scraper_utils

url = "https://programmer100.pythonanywhere.com/tours/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 '
                  'Safari/537.36'
}

source = scraper_utils.scrape(url)
value = scraper_utils.extract(source)

print(value)
