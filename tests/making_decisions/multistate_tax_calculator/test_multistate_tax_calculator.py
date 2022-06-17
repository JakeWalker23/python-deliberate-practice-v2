from src.making_decisions.multistate_tax_calculator.MultistateTaxCalculator import MultiStateTaxCalculator
from unittest.mock import patch
import unittest


class TestMultiStateTaxCalculator(unittest.TestCase):

    @patch('builtins.input')
    def test_calculate_tax_for_non_selected_state(self, mock_input):
        mock_input.side_effect = [1000, "New York",]
        
        MSC = MultiStateTaxCalculator()
        MSC.run()
        
        assert MSC.order_amount == 1000
        assert MSC.state == "New York"
        assert MSC.total == 1000

    @patch('builtins.input')
    def test_calculate_tax_for_illinois_state(self, mock_input):
        mock_input.side_effect = [1000, "Illinois"]
        
        MSC = MultiStateTaxCalculator()
        MSC.run()
        
        assert MSC.order_amount == 1000
        assert MSC.state == "Illinois"
        assert MSC.illinois_sales_tax == 0.08
        assert MSC.total == 1080

    @patch('builtins.input')
    def test_calculate_tax_for_wisconsin_state(self, mock_input):
        mock_input.side_effect = [1000, "Wisconsin", "Lafayette"]
        
        MSC = MultiStateTaxCalculator()
        MSC.run()
        
        assert MSC.order_amount == 1000
        assert MSC.state == "Wisconsin"
        assert MSC.total == 1000

    @patch('builtins.input')
    def test_calculate_tax_for_wisconsin_state_eau_claire_county(self, mock_input):
        mock_input.side_effect = [1000, "Wisconsin", "eau claire"]
        
        MSC = MultiStateTaxCalculator()
        MSC.run()
        
        assert MSC.order_amount == 1000
        assert MSC.state == "Wisconsin"
        assert MSC.county == "eau claire"
        assert MSC.eau_claire_sales_tax == 0.004
        assert MSC.total == 1004

    @patch('builtins.input')
    def test_calculate_tax_for_wisconsin_state_dunn_county(self, mock_input):
        mock_input.side_effect = [1000, "Wisconsin", "dunn"]
        
        MSC = MultiStateTaxCalculator()
        MSC.run()
        
        assert MSC.order_amount == 1000
        assert MSC.state == "Wisconsin"
        assert MSC.county == "dunn"
        assert MSC.dunn_sales_tax == 0.005
        assert MSC.total == 1005
