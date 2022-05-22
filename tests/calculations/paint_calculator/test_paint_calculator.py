from src.calculations.paint_calculator.PaintCalculator import Gallons
from unittest.mock import patch
import unittest


class TestGallons(unittest.TestCase):

    @patch('builtins.input')
    def test_run_integration(self, mock_input):
        mock_input.side_effect = [1, 2]

        gallons = Gallons()
        gallons.run()

        assert gallons.length == 1
        assert gallons.width == 2
        assert gallons.total == 1

    @patch('builtins.input')
    def test_run_integration_2(self, mock_input):
        mock_input.side_effect = [23, 50]

        gallons = Gallons()
        gallons.run()

        assert gallons.length == 23
        assert gallons.width == 50
        assert gallons.total == 4
