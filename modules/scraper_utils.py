import os
import requests
import selectorlib
import modules.config as config


def scrape(url: str) -> str:
    response = requests.get(url)
    source = response.text

    return source


def extract(source: str) -> str:
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    value = extractor.extract(source)["tours"]

    return value


def init_csv() -> None:
    if not os.path.exists(config.DATA_FILE):
        with open(config.DATA_FILE, "w") as file:
            file.write(",".join(config.DATA_FORMAT) + "\n")


def check_csv(value: str) -> bool:
    init_csv()

    with open(config.DATA_FILE) as file:
        content = file.read()

    already_parsed = value in content

    return already_parsed


def store_csv(value: str) -> None:
    init_csv()

    with open(config.DATA_FILE, "a") as file:
        file.write(value + "\n")
