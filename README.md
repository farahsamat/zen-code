# ZENDESK TICKET VIEWER
This project is part of the Zendesk Software Engineering Intern selection process. The task is to build a ticket viewer that can display a list of tickets and view the details of each individual ticket.

## Getting Started
* Make sure you have Python 3 [installed](https://www.python.org/downloads/).
* Clone this repository: `git clone https:://github.com/farahsamat/zen-code.git`
* Install dependencies: `pip install -r requirements.txt`
* API authentication credentials: Rename `.env.example` to `.env` and populate it with the required login credentials.

## Running the happy path tests
On the CLI, run: `python -m unittest`

## Using the ticket viewer
The ticket viewer is a CLI. Ensure you are working in the directory where the script is saved.

`python ticket_viewer.py`
<insert main_menu screen shot>
![Main menu](https://github.com/farahsamat/blob/master/images/main_menu.png)

Choose your option:

<b>Option 1</b> will display a list of tickets. The list will only display a maximum of 25 tickets at a time.
![Ticket list](https://github.com/farahsamat/zen-code/blob/master/images/sample_list.png)

<b>Option 2</b> will prompt you to select a ticket to view the details.
![Ticket details](https://github.com/farahsamat/zen-code/blob/master/images/sample_ticket.png)

If an invalid ticket number is given, you will be brought back to the main menu.
![Go back](https://github.com/farahsamat/zen-code/blob/master/images/back_to_main.png)

<b>Option 3</b> will exit the program.
 
The ticket viewer will keep prompting for an option if an invalid input is given.
![Invalid input](https://github.com/farahsamat/zen-code/blob/master/images/invalid_input.png)

## Acknowledgments

[Zendesk Ticket API Doc](https://developer.zendesk.com/rest_api/docs/support/tickets)

