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
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    subdomain = input('Please enter your subdomain: ')
    root_url = f'https://{subdomain}.zendesk.com/api/v2/tickets'
    page_size = 25

    tickets = Tickets(username, password, root_url)

    while True:
        choice = display_menu(main_menu)
        if choice == 1:
            next_page = 1
            next_page = tickets.view_list(next_page, page_size)
            while next_page:
                input("Press enter to view the next page")
                next_page = tickets.view_list(next_page, page_size)
        elif choice == 2:
            ticket_id = input("Please enter a ticket number: ")
            tickets.view_ticket(ticket_id)
        elif choice == 3:
            break
