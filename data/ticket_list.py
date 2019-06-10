import requests
import json
import pandas as pd

#pagination
pagination = '?per_page=25'
per_page = 'https://{}.zendesk.com/api/v2/tickets.json{}'.format(subdomain, pagination)
while per_page:
    r = requests.get(per_page, auth=auth)
    data = r.json()
    for ticket in data['tickets']:
        keys = ['id', 'subject', 'status', 'priority']
        print ([ticket.get(key) for key in keys])
    per_page = data['next_page']

#view ticket
ticket_id = input("Please enter a ticket number: ")
ticket_url = 'https://{}.zendesk.com/api/v2/tickets/{}.json'.format(subdomain, ticket_id)
try:
    r = requests.get(ticket_url, auth=auth)
    data = r.json()
    print (pd.DataFrame(data))
except ValueError:
    print("Invalid ticket number")
