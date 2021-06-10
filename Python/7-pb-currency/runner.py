import sys

import pb_currency
import rates_history
import time

from plyer import notification

for i in range(8):
    currencies = pb_currency.prepare_currencies_list()
    stringed_currencies = "".join(currency.get_info() for currency in currencies)
    stringed_currencies = currencies[0].date + "\n" + stringed_currencies
    rates_history.update_currency_history_file(stringed_currencies)
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
