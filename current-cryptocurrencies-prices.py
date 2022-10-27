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
    currency_price_USD = str(currency_USD['price'])

    currency_EUR = currency['EUR']
    currency_price_EUR = str(currency_EUR['price'])

    currency_GBP = currency['GBP']
    currency_price_GBP = str(currency_GBP['price'])

    update_time = data_info['updated_at']

    print(currency_name + " (" + currency_id + ")\n")
    print("USD price: " + currency_price_USD)
    print("EUR price: " + currency_price_EUR)
    print("GBP price: " + currency_price_GBP + "\n")
    print("Updated at: " + update_time[:10] + " " + update_time[11:19] + "\n")


def show_menu():
    print("1. Bitcoin (BTC)")
    print("2. Ethereum (ETH)")
    print("3. Tether (USDT)")
    print("4. USD Coin (USDC)")
    print("5. BNB (BNB)")
    print("6. Exit\n")


cryptocurrencies = {1: "BTC", 2: "ETH", 3: "USDT", 4: "USDC", 5: "BNB"}

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
