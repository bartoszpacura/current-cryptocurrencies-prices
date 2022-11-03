from getinfo import *


cryptocurrencies = {
    1: "BTC",
    2: "ETH",
    3: "USDT",
    4: "USDC",
    5: "BNB"}

while True:
    print(show_menu())

    try:
        user_choice = int(input("Enter the number to get information about the price of the cryptocurrency:\n"))

        if user_choice == 6:
            break
        elif user_choice < 1 or user_choice > 5:
            print("\nInvalid value.\nYou can only choose a number from 1 to 6.\n")
        else:
            cryptocurrency = cryptocurrencies[user_choice]
            information = get_cryptocurrency(cryptocurrency)
            print(get_info(information))
            input("Press Enter to continue.\n")

    except ValueError:
        print("\nInvalid value.\nYou can only choose a number from 1 to 6.\nDon't use letters or special characters.\n")
