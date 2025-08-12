"""Parser module."""

# -- Imports

import re
import csv
import requests
from bs4 import BeautifulSoup
from src.core.parser.models import EoraInfo, EoraInfoJSON


# --

EXCLUDE_KEYWORDS = {
    "О компании",
    "Вакансии",
    "Контакты",
    "+7",
    "HELLO@",
    "Политика конфиденциальности",
    "En",
    "ИННОПОЛИС",
    "ул.",
    "Портфолио",
    "Блог",
    "СТАТЬЯ",
    "Статья",
    "Услуги",
    "Нажимая на кнопку",
    "Отправить",
    "Позвоните нам",
    "Напишите нам",
    "Бот поддержки",
    "Робот для колл-центра",
    "Цифровой аватар",
    "Консультация в ИИ",
    "ИИ-ассистент с ChatGPT",
    "Навыки для голосовых ассистентов",
    "Топ 4 профессии",
    "Что такое Telegram Web App",
    "5 преимуществ голосового ассистента Маруся",
    "Все права защищены",
    "ООО «ЕОРА ДАТА ЛАБ»",
    "И наши менеджеры ответят на ваши вопросы",
    "Заполните форму",
    "Оставить заявку",
    "нажимая на кнопку, вы соглашаетесь с нашей политикой в отношении обработки персональных данных пользователей",
    "нажимая на кнопку, вы соглашаетесь с нашей политикой в отношении обработки персональных данных пользователя",
    "+7 495 414-40-49",
    "2025 © EORA. Все права защищены.",
    "hello@eora.ru",
    "тимлид",
    "2025 © eora. все права защищены. ооо «еора дата лаб»",
    "владислав виноградов",
    "ул. университетская, д. 7",
    "полезное",
    "топ 4 профессии, которые заменит gpt-4",
    "что такое telegram web appдля интернет-магазинов?",
}

# --


def normalize_text(text: str) -> str:
    # Заменяем все виды пробельных символов (включая U+00A0) на обычный пробел
    text = re.sub(r"[\u00a0\s]+", " ", text)
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


def parser(url: str):

    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, "lxml")

    h1_tags = soup.find_all("h1", class_="tn-atom")
    h2_tags = soup.find_all("h2", class_="tn-atom")
    div_tags = soup.find_all("div", class_="tn-atom")

    h1_texts = clean_texts([tag.text.strip() for tag in h1_tags])
    h2_texts = clean_texts([tag.text.strip() for tag in h2_tags])
    div_texts = clean_texts([tag.text.strip() for tag in div_tags])

    return EoraInfo(
        h1=" | ".join(h1_texts),
        h2=" | ".join(h2_texts),
        div=" | ".join(div_texts),
    )


def write_csv(data: EoraInfo):
    with open("eora.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                normalize_text(data.h1),
                normalize_text(data.h2),
                normalize_text(data.div),
            ]
        )


if __name__ == "__main__":
    url = "https://eora.ru/cases/computer-vision/lamoda-systema-segmentacii-i-poiska-po-pohozhey-odezhde"
    eora_info_data = parser(url=url)
    write_csv(data=eora_info_data)
