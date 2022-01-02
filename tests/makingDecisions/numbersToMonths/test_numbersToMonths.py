from src.makingDecisions.numbersToMonths.numbersToMonths import NumbersToMonths
import unittest


class Test_NumbersToNames(unittest.TestCase):
    def test_convert_to_1_to_month(self):
        months = NumbersToMonths()
        months.user_choice = 1

        months.convert_to_month()

        assert months.converted_month == "January"

    def test_convert_to_12_to_month(self):
        months = NumbersToMonths()
        months.user_choice = 12

        months.convert_to_month()

        assert months.converted_month == "December"
