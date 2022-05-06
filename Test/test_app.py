import unittest
import requests

import argparse


class TestApp(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)
        self.port = 8080
        self.ip = "127.0.0.1"


    def test_app_root(self):

        """Test app is running"""
        request = requests.get(f'http://{self.ip}:{self.port}', timeout=1)
        print ("Request = ", request.text)
        self.assertIn(" Hello. This is BankCheckRunner", request.text)


    def test_app_incorrect_card_length_short(self):

        '''Test response for incorrect card number - length < 16'''

        cardNumber = "123456789012345"
        request = requests.get(f'http://{self.ip}:{self.port}/card/{cardNumber}', timeout=1)
        print ("Request = ", request.text)
        self.assertEqual(request.status_code, 500)
        self.assertIn("Card number length is incorrect. Please check", request.text)


    def test_app_incorrect_card_length_long(self):

        '''Test response for incorrect card number - length > 20'''

        cardNumber = "123456789012345678901"
        request = requests.get(f'http://{self.ip}:{self.port}/card/{cardNumber}', timeout = 1 )
        print ("Request = ", request.text)
        self.assertEqual(request.status_code, 500)
        self.assertIn("Card number length is incorrect. Please check", request.text)


    def test_app_incorrect_card_consist(self):

        '''Test response for incorrect card number - it consists letters'''

        cardNumber = "111a"
        request = requests.get(f'http://{self.ip}:{self.port}/card/{cardNumber}', timeout = 1)
        print ("Request = ", request.text)
        self.assertEqual(request.status_code, 500)
        self.assertIn("Card number must contain digits only", request.text)


    def test_app_card_unknown_card(self):
        '''Test card number, that is not in db'''

        cardNumber = "11111111111111111111"
        request = requests.get(f'http://{self.ip}:{self.port}/card/{cardNumber}', timeout = 1)
        print("Request = ", request.text)
        self.assertEqual(request.status_code, 500)
        self.assertEqual(request.json().get("card data"), "Unknown card")


    def test_app_correct_card(self):
        '''Test correct response for valid card number'''

        cardNumber = "18006878901234567890"
        request = requests.get(f'http://{self.ip}:{self.port}/card/{cardNumber}', timeout = 1 )
        print ("Request = ", request.text)
        self.assertEqual(request.status_code, 200)
        self.assertIsNot(request.json().get("card data"), None)

if __name__ == '__main__':
    unittest.main(failfast = True)
