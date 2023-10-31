import unittest
from unittest.mock import Mock, patch
from easy_credit import Client

class TestClient(unittest.TestCase):

    @patch('requests.request')
    def test_get_transaction(self, mock_request):
        # Create an instance of the Client class
        client = Client(webshop_id='your_webshop_id', token='your_token')

        # Mock the response from the requests library
        mock_response = Mock()
        mock_response.json.return_value = {'status': 'AUTHORIZED'}
        mock_request.return_value = mock_response

        # Call the get_transaction method
        response = client.get_transaction('1.de.4145.1-0303135329-211')

        # Assert that the request method was called with the correct URL
        expected_url = 'https://ratenkauf.easycredit.de/api/payment/v3/transaction/1.de.4145.1-0303135329-211'
        mock_request.assert_called_with('GET', expected_url, auth=(client.webshop_id, client.token))

        # Assert that the response object has an is_authorized method
        self.assertTrue(hasattr(response, 'is_authorized'))

        # Call the is_authorized method and assert the result
        self.assertTrue(response.is_authorized())

if __name__ == '__main__':
    unittest.main()