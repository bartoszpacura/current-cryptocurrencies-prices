# Module used to downloading cryptocurrencies prices.

from requests import get


BASE_URL = "https://cryptingup.com/api/assets/"


def get_cryptocurrency(currency):
    endpoint = currency
    data = get(BASE_URL + endpoint).json()
    return data


def get_info(data):
    data_info = data['asset']
    currency_id = data_info['asset_id']
    currency_name = data_info['name']
    currency = data_info['quote']

    currency_USD = currency['USD']
    currency_price_USD = "%.2f" % round(currency_USD['price'], 2)

    currency_EUR = currency['EUR']
    currency_price_EUR = "%.2f" % round(currency_EUR['price'], 2)

    currency_GBP = currency['GBP']
    currency_price_GBP = "%.2f" % round(currency_GBP['price'], 2)

    update_time = data_info['updated_at']

    info = f"""
{'-' * 36}
    {currency_name} ({currency_id})\n
    USD price: {currency_price_USD}
    EUR price: {currency_price_EUR}
    GBP price: {currency_price_GBP}\n
    Updated at: {update_time[:10]} {update_time[11:19]}
{'-' * 36}\n"""

    return info


def show_menu():
    menu_text = f"""
{'-' * 36}
        1. Bitcoin (BTC))
        2. Ethereum (ETH))
        3. Tether (USDT)
        4. USD Coin (USDC)
        5. BNB (BNB)
        6. Exit
{'-' * 36}\n"""

    return menu_text
