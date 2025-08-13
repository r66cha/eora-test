"""Модуль парсера."""

# -- Imports

import time
import re
import csv
import requests
from bs4 import BeautifulSoup

# from src.core.parser import EoraInfo
from src.core.schemas import EoraInfoSchema
from src.core.parser import EXCLUDE_KEYWORDS
from src.core.parser.pages import PARSE_PAGES

# --

MAX_RETRIES = 5
RETRY_DELAY = 2

# --


def normalize_text(text: str) -> str:
    text = re.sub(r"[\u00a0\u200e\s]+", " ", text)
    return text.strip().lower()


normalized_exclude = {normalize_text(ex) for ex in EXCLUDE_KEYWORDS}


def clean_texts(texts: list[str]) -> list[str]:
    seen = set()
    result = []
    for t in texts:
        t_norm = normalize_text(t)
        if not t_norm:
            continue
        if t_norm in normalized_exclude:
            continue
        if t not in seen:
            seen.add(t)
            result.append(t)
    return result


def get_full_text(tag) -> str:
    return "".join(tag.strings)


def fetch_page(url: str) -> str:

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    }
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                return res.text
            else:
                # TODO: Log
                print(f"{url} — ошибка {res.status_code}, попытка {attempt}")
        except Exception as e:
            # TODO: Log
            print(f"{url} — исключение: {e}, попытка {attempt}")
        time.sleep(RETRY_DELAY)
    # TODO: Log
    print(f"{url} — не удалось загрузить страницу после {MAX_RETRIES} попыток")
    return ""


def parser(url: str) -> EoraInfoSchema:
    html = fetch_page(url)
    if not html:
        return EoraInfoSchema(case_="*")  # если страница не загрузилась

    soup = BeautifulSoup(html.strip(), "lxml")

    case_tags = soup.find_all("a", class_="t-menu__link-item")
    case_ = clean_texts([get_full_text(tag) for tag in case_tags])

    description_tags = soup.find_all(["h1", "h2", "div"], class_="tn-atom")
    description = clean_texts([get_full_text(tag) for tag in description_tags])

    return EoraInfoSchema(
        case_="  | ".join(case_),
        description="  | ".join(description),
    )


def write_csv(index: int, data: EoraInfoSchema, url: str):
    with open("eora.csv", mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            [
                index + 1,
                normalize_text(data.case_),
                normalize_text(data.description),
                url,
            ]
        )
        writer.writerow(["---"])


if __name__ == "__main__":
    for i, url in enumerate(PARSE_PAGES):
        eora_info_data = parser(url=url)
        write_csv(i, eora_info_data, url)
