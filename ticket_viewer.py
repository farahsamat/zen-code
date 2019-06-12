from tickets import Tickets
import numpy as np
import os

os.system('cls' if os.name == 'nt' else 'clear')

main_menu = np.array(["Display ticket list", "View ticket", "Quit"])


def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print(" ")
            pass
    return num


def display_menu(options):
    print(" ")
    print("----------MAIN MENU-----------------")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i + 1, options[i]))

    option = 0
    while not (np.any(option == np.arange(len(options)) + 1)):
        option = input_number("Please choose your option: ")
        print(" ")
    return option


if __name__ == "__main__":
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    tickets = Tickets(username, password)

    while True:
        choice = display_menu(main_menu)
        if choice == 1:
            tickets.view_list()
        elif choice == 2:
            tickets.view_ticket()
        elif choice == 3:
            break
