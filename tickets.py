import requests
import json
import pandas as pd
import os
from beautifultable import BeautifulTable
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
url = 'https://farahsamat.zendesk.com/api/v2/tickets'
per_page = '?per_page=25'
data_to_display = ['id', 'subject', 'status']


class Tickets:
    def __init__(self):
        pass

    def view_list(self):
        page_count = 1
        pagination = '{}.json{}'.format(url, per_page)
        try:
            while pagination:
                table = BeautifulTable()
                table.column_headers = data_to_display
                r = requests.get(pagination, auth=(username, password))
                data = r.json()
                for ticket in data['tickets']:
                    table.append_row([ticket.get(key) for key in data_to_display])
                table.append_row(['', '<<<     End of page {}     >>>'.format(str(page_count)), ''])
                print (table)
                page_count += 1
                pagination = data['next_page']
                next_page = input("Press 'enter' to continue ")
                if next_page.lower() == ' ':
                    continue
        except KeyError:
            print("URL/Authentication error")
        except requests.exceptions.HTTPError as errh:
            print("Http Error: ", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting: ", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error: ", errt)
        except requests.exceptions.RequestException as err:
            print("Request Error: ", err)

    def view_ticket(self):
        try:
            while url:
                ticket_id = input("Please enter a ticket number: ")
                ticket_url = '{}/{}.json'.format(url, ticket_id)
                r = requests.get(ticket_url, auth=(username, password))
                data = r.json()
                print (pd.DataFrame(data))
        except KeyError:
            print("URL/Authentication error")
        except ValueError:
            print("Invalid ticket/Authentication error")
        except requests.exceptions.HTTPError as errh:
            print("Http Error: ", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting: ", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error: ", errt)
        except requests.exceptions.RequestException as err:
            print("Request Error ", err)
