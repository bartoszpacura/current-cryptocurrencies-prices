from getinfo import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.geometry("400x475+760+200")
root.resizable(False, False)
root.configure(background="#1e2224")
root.title("Current Cryptocurrencies Prices")


def select_clicked():
    user_choice = answer.get()

    if user_choice == "":
        msg = "You have to enter something."
        showinfo(title="Invalid value", message=msg)
    else:
        try:
            user_choice = int(user_choice)

            if user_choice == 6:
                root.destroy()
            elif user_choice < 1 or user_choice > 5:
                msg = "You can only choose a number from 1 to 6."
                showinfo(title="Invalid value", message=msg)
            else:
                get_info_about_currency(user_choice)

        except ValueError:
            msg = "You can only choose a number from 1 to 6.\nDon't use letters or special characters.\n"
            showinfo(title="Invalid value", message=msg)


def get_info_about_currency(choice_number):
    cryptocurrencies = {
        1: "BTC",
        2: "ETH",
        3: "USDT",
        4: "USDC",
        5: "BNB"}

    cryptocurrency = cryptocurrencies[choice_number]

    information = get_cryptocurrency(cryptocurrency)
    info_to_show = get_info(information)

    global label_visible
    global label_2

    if label_visible is True:
        label_2.destroy()

    label_2 = ttk.Label(root, text=info_to_show, background="#1e2224", foreground="#e6db74", font=("Consolas", 12))
    label_2.pack()
    label_visible = True


menu = show_menu()
ttk.Label(root, text=menu, background="#1e2224", foreground="#e6db74", font=("Consolas", 12)).pack()

label_visible = False

answer = tk.StringVar()

answer_entry = ttk.Entry(root, textvariable=answer)
answer_entry.pack()
answer_entry.focus()


ttk.Button(root, text="Select", command=select_clicked).pack(pady=10)

label_2 = ttk.Label(root)

root.mainloop()
