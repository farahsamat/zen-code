import os
import unittest

from tickets import Tickets


class TicketsTest(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        root_url = 'https://farahsamat.zendesk.com/api/v2/tickets'
        self.tickets = Tickets(username, password, root_url)

    def test_view_list(self):
        page_count = 1
        next_page = 1
        next_page = self.tickets.view_list(next_page, 25)
        while next_page:
            page_count += 1
            next_page = self.tickets.view_list(next_page, 25)
        self.assertEqual(page_count, 5)

    def test_view_ticket(self):
        ticket = self.tickets.view_ticket(5)
        self.assertEqual(ticket['ticket']['id'], 5)
