from testclass import Tickets

ticket_list = Tickets()
select_ticket = Tickets()

user_prompt = input("Type '1' to view ticket list or '2' to view selected ticket ")
error_message = "Invalid"
user_exit = "Have a nice day!"

def user_interaction(user_input):
    while int(user_input) == 1:
        ticket_list.view_list()
        option1 = input("Do you want to view list again? (Y/N) ")
        if option1.lower() == 'y':
            continue
        elif option1.lower() == 'n':
            print (user_exit)
            break
        else:
            print (error_message)

    while int(user_input) == 2:
        select_ticket.view_ticket()
        option2 = input("Do you want to choose another ticket? (Y/N) ")
        if option2.lower() == 'y':
            continue
        elif option2.lower() == 'n':
            print (user_exit)
            break
        else:
            print (error_message)


user_interaction(user_prompt)
