from getinfo import *


cryptocurrencies = {
    1: "BTC",
    2: "ETH",
    3: "USDT",
    4: "USDC",
    5: "BNB"}

while True:
    menu = show_menu()
    print(menu)

    try:
        user_choice = int(input("Enter the number to get information about the price of the cryptocurrency:\n"))

        if user_choice == 6:
            break
        elif user_choice < 1 or user_choice > 5:
            print("\nInvalid value.\nYou can only choose a number from 1 to 6.\n")
        else:
            cryptocurrency = cryptocurrencies[user_choice]

            information = get_cryptocurrency(cryptocurrency)
            info = get_info(information)
            print(info)

            input("Press Enter to continue.\n")

    except ValueError:
        print("\nInvalid value.\nYou can only choose a number from 1 to 6.\nDon't use letters or special characters.\n")
