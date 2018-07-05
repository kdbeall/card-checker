import unittest
import card_checker


class Test(unittest.TestCase):

    def test_check_valid(self):
        valid_cards = ["4532015112830366", "6011514433546201"]
        for valid_card in valid_cards:
            self.assertTrue(card_checker.check(valid_card))

    def test_check_invalid(self):
        invalid_cards = ["123784912879347168034513904573457892349802384790"]
        for invalid_card in invalid_cards:
            self.assertFalse(card_checker.check(invalid_card))
