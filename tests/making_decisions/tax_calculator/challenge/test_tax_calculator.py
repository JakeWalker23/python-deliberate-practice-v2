from src.making_decisions.tax_calculator.TaxCalculator import TaxCalculator
from unittest.mock import patch
import unittest

class Test_TaxCalculator(unittest.TestCase):
    
    @patch('builtins.input')
    def test_tax_calculator_run(self, mock_input):
        mock_input.side_effect = [50, 'NY']
        
        tax_calculator = TaxCalculator()
        tax_calculator.run()
        
        assert tax_calculator.total == 50
        assert tax_calculator.state == "NY"
        assert tax_calculator.tax_percentage == 0.055
        
    @patch('builtins.input')
    def test_tax_calculator_run_state_with_wisconsin(self, mock_input):
        mock_input.side_effect = [50, 'WI']
        
        tax_calculator = TaxCalculator()
        tax_calculator.run()
        
        assert tax_calculator.total == 52.75
        assert tax_calculator.order_amount == 50
        assert tax_calculator.state == "WI"
        assert tax_calculator.tax_percentage == 0.055