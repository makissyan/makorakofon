import sys

import pb_currency
import rates_history
import time

from plyer import notification

for i in range(8):
    raw_response = pb_currency.get_currency_rate().decode('utf-8')
    rates_history.update_file(raw_response, rates_history.RAW_JSON_RESPONSES)

    currencies = pb_currency.prepare_currencies_list(raw_response)
    stringed_currencies = "".join(currency.get_info() for currency in currencies)
    stringed_currencies = currencies[0].date + "\n" + stringed_currencies

    rates_history.update_file(stringed_currencies, rates_history.HISTORY_FILE)

    notification.notify(title="PrivatBank currency rates",
                        message=stringed_currencies,
                        app_name="PB_RATES",
                        app_icon="symbol.ico",
                        timeout=10)

    time.sleep(int(sys.argv[1]))

notification.notify(title="PrivatBank currency rates",
                    message="Currency check finished",
                    app_name="PB_RATES",
                    app_icon="symbol.ico",
                    timeout=10)
