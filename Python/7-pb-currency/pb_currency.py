import json

import requests

from currency import Currency

PB_CURRENCY_API_PATH = "https://otp24.privatbank.ua/v2/api/1/info/currency/get"
DATE_KEY = "date"
RATE_KEY = "rate"
BUY_RATE_KEY = "B"
SELL_RATE_KEY = "S"


def get_currency_rate():
    response = requests.get(PB_CURRENCY_API_PATH)
    if response.status_code == 200:
        return response.content
    else:
        return "Unable to get currency rate"


def prepare_currencies_list(raw_json):
    currencies_to_get = ['USD', 'EUR']
    currencies_list = []
    raw_json = json.loads(raw_json)

    for currency in currencies_to_get:
        currencies_list.append(process_currency(raw_json, currency))

    return currencies_list


def process_currency(raw_json, currency_to_process):
    currency_info = raw_json[currency_to_process]

    return Currency(
        currency_to_process,
        "Updated: " + currency_info[BUY_RATE_KEY][DATE_KEY],
        fixed_digits(float(currency_info[BUY_RATE_KEY][RATE_KEY])),
        fixed_digits(float(currency_info[SELL_RATE_KEY][RATE_KEY])))


def fixed_digits(number, digits=2):
    return f"{number:.{digits}f}"