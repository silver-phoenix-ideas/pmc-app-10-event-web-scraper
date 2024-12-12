import requests
import selectorlib


def scrape(url: str) -> str:
    response = requests.get(url)
    source = response.text

    return source


def extract(source: str) -> str:
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    value = extractor.extract(source)["tours"]

    return value
