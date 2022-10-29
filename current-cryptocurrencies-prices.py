from requests import get

BASE_URL = "https://cryptingup.com/api/assets/"

m = 3.300
print(round(m, 2))


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
    {'-' * 34}
    {currency_name} ({currency_id})\n
    USD price: {currency_price_USD}
    EUR price: {currency_price_EUR}
    GBP price: {currency_price_GBP}\n
    Updated at: {update_time[:10]} {update_time[11:19]}
    {'-' * 34}\n"""

    print(info)


def show_menu():
    menu_text = f"""
    {'-' * 34}
    1. Bitcoin (BTC))
    2. Ethereum (ETH))
    3. Tether (USDT)
    4. USD Coin (USDC)
    5. BNB (BNB)
    6. Exit
    {'-' * 34}\n"""

    print(menu_text)


cryptocurrencies = {
    1: "BTC",
    2: "ETH",
    3: "USDT",
    4: "USDC",
    5: "BNB"}

while True:
    show_menu()

    try:
        user_choice = int(input("Enter the number to get information about the price of the cryptocurrency:\n"))

        if user_choice == 6:
            break
        elif user_choice < 1 or user_choice > 5:
            print("\nInvalid value.\nYou can only choose a number from 1 to 6.\n")
        else:
            cryptocurrency = cryptocurrencies[user_choice]
            information = get_cryptocurrency(cryptocurrency)
            get_info(information)
            input("Press Enter to continue.\n")

    except ValueError:
        print("\nInvalid value.\nYou can only choose a number from 1 to 6.\nDon't use letters or special characters.\n")
