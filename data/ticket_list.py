import requests
import json

url = 'https://{subdomain}.zendesk.com/api/v2/tickets.json?per_page=25'

while url:
    response = requests.get(url, auth=('{username}', '{password}'))
    data = response.json()
    for item in data['tickets']:
        keys = ['id', 'subject', 'status', 'priority']
        print ([item.get(key) for key in keys])
    url = data['next_page']
