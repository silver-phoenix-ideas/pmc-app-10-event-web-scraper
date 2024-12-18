import time
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

if __name__ == "__main__":
    while True:
        source = scraper_utils.scrape(url)
        data = scraper_utils.extract(source)

        if data:
            print(data)
            already_parsed = scraper_utils.check_csv(data)

            if not already_parsed:
                scraper_utils.store_csv(data)
                email_utils.send_email(" - ".join(data.values()))
            else:
                print("Email for this event already sent.")
        else:
            print("No upcoming events.")

        time.sleep(5)
