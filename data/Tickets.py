import requests
import json
import pandas as pd
import os
from tabulate import tabulate
from beautifultable import BeautifulTable
from dotenv import load_dotenv

load_dotenv()

subdomain = os.getenv("SUBDOMAIN")
username = os.getenv("USERNAME")
token_key = os.getenv("TOKEN")
per_page = str(25)
data_to_display = ['id', 'subject']

class Tickets:
    def view_list(self):
        start_count = 0
        table = BeautifulTable()
        table.column_headers = ['id', 'subject']
        pagination = 'https://{}.zendesk.com/api/v2/tickets.json?per_page={}'.format(subdomain, per_page)
        while pagination:
            r = requests.get(pagination, auth=(username, token_key))
            data = r.json()
            for ticket in data['tickets']:
                table.append_row([ticket.get(key) for key in data_to_display])
            print (table)
            start_count += 1
            pagination = data['next_page']
            table.append_row(['Page','<     {}     >'.format(str(start_count))])
            next_page = input("Press 'enter' to continue ")
            if next_page.lower() == ' ':
                continue

    def view_ticket(self):
        try:
            ticket_id = input("Please enter a ticket number: ")
            ticket_url = 'https://{}.zendesk.com/api/v2/tickets/{}.json'.format(subdomain, ticket_id)
            r = requests.get(ticket_url, auth=(username, token_key))
            data = r.json()
            print (pd.DataFrame(data)[['submitter_id', 'created at', 'subject', 'description',]])
        except ValueError:
            print("Invalid ticket number")
