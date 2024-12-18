import os
import requests
import selectorlib
import modules.config as config


class Tour(selectorlib.formatter.Formatter):
    def format(self, text: str) -> dict[str, str]:
        tour = {}

        if text == "No upcoming tours":
            return tour

        values = text.split(",")

        for value, column in zip(values, config.DATA_FORMAT):
            value = value.strip()

            if column == "date":
                day, month, year = value.split(".")
                value = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

            tour[column] = value

        return tour


def scrape(url: str) -> str:
    response = requests.get(url)
    source = response.text

    return source


def extract(source: str) -> dict[str, str]:
    extractor = selectorlib.Extractor.from_yaml_file(
        config.EXTRACTOR_FILE, formatters=[Tour]
    )
    data = extractor.extract(source)["tours"]

    return data


def init_csv() -> None:
    if not os.path.exists(config.DATA_FILE):
        with open(config.DATA_FILE, "w") as file:
            file.write(",".join(config.DATA_FORMAT) + "\n")


def check_csv(data: dict[str, str]) -> bool:
    init_csv()

    with open(config.DATA_FILE) as file:
        rows = file.read()

    already_parsed = ",".join(data.values()) in rows

    return already_parsed


def store_csv(data: dict[str, str]) -> None:
    init_csv()

    with open(config.DATA_FILE, "a") as file:
        file.write(",".join(data.values()) + "\n")
