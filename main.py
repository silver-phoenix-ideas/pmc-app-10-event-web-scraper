import dotenv
import modules.scraper_utils as scraper_utils
import modules.email_utils as email_utils

dotenv.load_dotenv(".env")

url = "https://programmer100.pythonanywhere.com/tours/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 '
                  'Safari/537.36'
}

source = scraper_utils.scrape(url)
value = scraper_utils.extract(source)
content = scraper_utils.read()

print(value)

if value != "No upcoming tours":
    if value not in content:
        scraper_utils.store(value)
        email_utils.send_email(value)
    else:
        print("Email for this event already sent.")
