import unittest
from src.calculations.currency_converter.Currency import Currency
from unittest.mock import patch
import sys


class Test_Currency(unittest.TestCase):

    @patch('builtins.input')
    def test_currency_calculator_run_france_1000(self, mocked_input_1):
        mocked_input_1.side_effect = ['france', 1000]

        currency = Currency()
        currency.run()

        assert currency.country == 'france'
        assert currency.convert_amount == 1000
        assert currency.converted_currency == 1190.0

    @patch('builtins.input')
    def test_currency_calculator_run_uk_10(self, mocked_input_1):
        mocked_input_1.side_effect = ['uk', 10]

        currency = Currency()
        currency.run()

        assert currency.country == 'uk'
        assert currency.convert_amount == 10
        assert currency.converted_currency == 13.865

    @patch('builtins.input')
    def test_currency_calculator_run_russia_100000(self, mocked_input_1):
        mocked_input_1.side_effect = ['russia', 100000]

        currency = Currency()
        currency.run()

        assert currency.country == 'russia'
        assert currency.convert_amount == 100000
        assert currency.converted_currency == 1400.0

    @patch('builtins.input')
    def test_currency_calculator_run_invalid(self, mocked_input_1):
        mocked_input_1.side_effect = ['azerbajin', 1000]

        currency = Currency()

        with self.assertRaises(BaseException) as E:
            currency.run()
            self.assertEqual(E.exception, "Invalid Country provided")
