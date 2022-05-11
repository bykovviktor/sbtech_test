import unittest

from Bank_check.card_validation import Card


class TestCard(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCard, self).__init__(*args, **kwargs)
        self.card = Card(path='./Tests/binlist-data.csv')

    def test_check_card_data_min_length(self):

        """checking length error if length < 16"""

        request = self.card.check_card_data('123')
        self.assertEqual(request["code"], 500)  # add assertion here
        self.assertEqual(request["message"], "Card number length is incorrect. Please check")

    def test_check_card_data_max_length(self):

        """checking length error if length > 20"""

        request = self.card.check_card_data("123456789012345678901")
        self.assertEqual(request["code"], 500)
        self.assertEqual(request["message"], "Card number length is incorrect. Please check")

    def test_check_card_data_digits_only(self):

        """checking error if card number contains letters"""

        request = self.card.check_card_data("12345678901234567a")
        self.assertEqual(request["code"], 500)
        self.assertEqual(request["message"], "Card number must contain digits only")


    def test_get_bank_data_unknown_card(self):

        """checking error if bin code was not found in data file"""

        request = self.card.get_bank_data("1234567890123456")
        self.assertEqual(request[1], 500)
        self.assertEqual(request[0].get('card data'), "Unknown card")


    def test_get_bank_data_correct(self):

        """checking correct request and correct response"""

        request = self.card.get_bank_data("42326078901234567890")
        print (request)
        self.assertEqual(request[1], 200)
        self.assertIsNot(request[0].get('card data'), None)

if __name__ == '__main__':
    unittest.main()
