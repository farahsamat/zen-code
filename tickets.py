import pandas as pd
import requests
from beautifultable import BeautifulTable
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

load_dotenv()

data_to_display = ['id', 'subject', 'status']


class Tickets:
    def __init__(self, username, password, root_url):
        self.username = username
        self.password = password
        self.root_url = root_url

    def view_list(self, page, page_size):
        next_page_url = '{}.json?page={}&per_page={}'.format(self.root_url, page, page_size)
        try:
            table = BeautifulTable()
            table.column_headers = data_to_display
            r = requests.get(next_page_url, auth=(self.username, self.password))
            data = r.json()
            for ticket in data['tickets']:
                table.append_row([ticket.get(key) for key in data_to_display])
            table.append_row(['', '<<<     End of page {}     >>>'.format(str(page)), ''])
            print(table)
            next_page = data['next_page']
            if next_page:
                url = urlparse(data['next_page'])
                return int(parse_qs(url.query)['page'][0])
            else:
                return None
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

    def view_ticket(self, ticket_id):
        try:
            ticket_url = '{}/{}.json'.format(self.root_url, ticket_id)
            r = requests.get(ticket_url, auth=(self.username, self.password))
            data = r.json()
            print(pd.DataFrame(data))
            return data
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
