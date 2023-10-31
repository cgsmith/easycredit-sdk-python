import json
import requests
from requests.auth import HTTPBasicAuth


class Client:
    BASE_URL = 'https://ratenkauf.easycredit.de/api/payment/v3'
    TRANSACTION_URL = '/transaction'

    def __init__(self, webshop_id=None, token=None):
        self.setup(webshop_id, token)

    def setup(self, webshop_id, token):
        self.webshop_id = webshop_id
        self.token = token
        self.response = None
        return self

    def get_transaction(self, transaction_id):
        """
        easyCredit - Get Transaction
        Get the specific transaction data based on the unique TeamBank identifier

        :param str transaction_id: Unique TeamBank transaction identifier
            Example: 1.de.4145.1-0303135329-211
        :return: response
        :rtype: requests.Response
        """
        self.response = self.request('GET', f"{self.BASE_URL}{self.TRANSACTION_URL}/{transaction_id}")
        return self

    def is_authorized(self):
        response_data = self.response.json()
        return response_data.get('status') == 'AUTHORIZED'

    def request(self, method, url):
        return requests.request(method, url, auth=HTTPBasicAuth(self.webshop_id, self.token))
