import os
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


def read() -> str:
    content = ""

    if os.path.exists("data.txt"):
        with open("data.txt") as file:
            content = file.read()
    else:
        with open("data.txt", "w") as file:
            pass

    return content


def store(value: str) -> None:
    with open("data.txt", "a") as file:
        file.write(value + "\n")
