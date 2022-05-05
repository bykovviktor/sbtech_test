import unittest

from Bank_check.card_validation import card


class TestCard(unittest.TestCase):
    def test_check_card_data_min_length(self):
        """checking length error if length < 16"""
        #check length error <16
        request = card('123')
        self.assertEqual(request.check_card_data()["code"], 500)  # add assertion here
        self.assertEqual(request.check_card_data()["message"], "Card number length is incorrect. Please check")

    def test_check_card_data_max_length(self):
        """checking length error if length > 20"""
        # check length error >20
        request = card("123456789012345678901")
        self.assertEqual(request.check_card_data()["code"], 500)
        self.assertEqual(request.check_card_data()["message"], "Card number length is incorrect. Please check")

    def test_check_card_data_digits_only(self):
        """checking error if card number contains letters"""
        request = card ("12345678901234567q")
        self.assertEqual(request.check_card_data()["code"], 500)
        self.assertEqual(request.check_card_data()["message"], "Card number must contain digits only")

    def test_get_bank_data_nonexists_bin(self):
        """checking error if bin code was not found in data file"""
        request = card("11111111111111111")
        self.assertEqual(request.get_bank_data()[1], 500)
        self.assertEqual(request.get_bank_data()[0], "bin code 111111 not found in database")

    def test_get_bank_data_correct(self):
        """checking correct request and correct response"""
        request = card("18006878901234567890")
        self.assertEqual(request.get_bank_data()[1], 200)
        self.assertEqual(request.get_bank_data()[0].get('card data')[0].get('bin'), "180068")

if __name__ == '__main__':
    unittest.main()
