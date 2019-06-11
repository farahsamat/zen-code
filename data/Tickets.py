import requests
import json
import pandas as pd
import os
from beautifultable import BeautifulTable
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

data_to_display = ['id', 'subject', 'status']

class Tickets:
    def view_list(self):
        page_count = 1
        pagination = 'https://farahsamat.zendesk.com/api/v2/tickets.json?per_page=25'
        while pagination:
            table = BeautifulTable()
            table.column_headers = data_to_display
            r = requests.get(pagination, auth=(username, password))
            data = r.json()
            for ticket in data['tickets']:
                table.append_row([ticket.get(key) for key in data_to_display])
            table.append_row(['','<<<     End of page {}     >>>'.format(str(page_count)),''])
            print (table)
            page_count += 1
            pagination = data['next_page']
            next_page = input("Press 'enter' to continue ")
            if next_page.lower() == ' ':
                continue

    def view_ticket(self):
        try:
            ticket_id = input("Please enter a ticket number: ")
            ticket_url = 'https://farahsamat.zendesk.com/api/v2/tickets/{}.json'.format(ticket_id)
            r = requests.get(ticket_url, auth=(username, password))
            data = r.json()
            print (pd.DataFrame(data))
        except ValueError:
            print("**Invalid ticket number**")
