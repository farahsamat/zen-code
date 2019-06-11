import numpy as np
from Tickets import Tickets

ticket_list = Tickets()
select_ticket = Tickets()

main_menu = np.array(["Display ticket list", "View ticket", "Quit"])

def input_number(prompt):
    while True:
        try:
            num=float(input(prompt))
            break
        except ValueError:
            print ("Invalid input")
    return num


def display_menu(options):
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = input_number("Please choose your option ")
    return choice

while True:
    choice = display_menu(main_menu)
    if choice == 1:
        ticket_list.view_list()
    elif choice == 2:
        select_ticket.view_ticket()
    elif choice == 3:
        break
