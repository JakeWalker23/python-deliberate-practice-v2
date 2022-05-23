from src.making_decisions.numbers_to_months.numbersToMonths import NumbersToMonths
from unittest.mock import patch
import unittest


class Test_NumbersToNames(unittest.TestCase):

    @patch('builtins.input')
    def test_run_integration_july(self, mock_input):
        mock_input.return_value = 7

        numbers_to_months = NumbersToMonths()
        numbers_to_months.run()

        assert numbers_to_months.converted_month == 'July'

    @patch('builtins.input')
    def test_run_integration_january(self, mock_input):
        mock_input.return_value = 1

        numbers_to_months = NumbersToMonths()
        numbers_to_months.run()

        assert numbers_to_months.converted_month == 'January'

    @patch('builtins.input')
    def test_run_integration_december(self, mock_input):
        mock_input.return_value = 12

        numbers_to_months = NumbersToMonths()
        numbers_to_months.run()

        assert numbers_to_months.converted_month == 'December'

    def test_display_returns_false_when_choice_invalid(self):
        numbers_to_months = NumbersToMonths()
        numbers_to_months.errors.append("Test")
        result = numbers_to_months.display()

        assert result == False
