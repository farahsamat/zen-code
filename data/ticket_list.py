import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

subdomain = os.getenv("SUBDOMAIN")
username = os.getenv("USERNAME")
token_key = os.getenv("TOKEN")
per_page = str(25)
data_to_display = ['id', 'subject', 'status', 'priority']


class Tickets:
    def view_list(self):
        pagination = 'https://{}.zendesk.com/api/v2/tickets.json?per_page={}'.format(subdomain, per_page)
        while pagination:
            r = requests.get(pagination, auth=(username, token_key))
            data = r.json()
            for ticket in data['tickets']:
                print ([ticket.get(key) for key in data_to_display])
            pagination = data['next_page']

    def view_ticket(self):
        ticket_id = input("Please enter a ticket number: ")
        ticket_url = 'https://{}.zendesk.com/api/v2/tickets/{}.json'.format(subdomain, ticket_id)
        try:
            r = requests.get(ticket_url, auth=(username, token_key))
            data = r.json()
            print (pd.DataFrame(data))
        except ValueError:
            print("Invalid ticket number")
