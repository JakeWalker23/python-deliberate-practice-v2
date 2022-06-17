from src.making_decisions.bmi_calculator.BMI import BMI
from unittest.mock import patch
import unittest

class TestBMICalculator(unittest.TestCase):
    
    @patch('builtins.input')    
    def test_bmi_calculate(self, mock_input):
        mock_input.side_effect = [100, 200]
    
        bmi = BMI()
        bmi.run()

        assert bmi.height == 100
        assert bmi.weight == 200


    @patch('builtins.input')   
    def test_display_bmi_is_ideal(self, mock_input):
        mock_input.side_effect = [72, 182]
    
        bmi = BMI()
        bmi.run()

        assert bmi.bmi_index == 24.68
        
    @patch('builtins.input')   
    def test_display_bmi_is_overweight(self, mock_input):
        mock_input.side_effect = [50, 100]
    
        bmi = BMI()
        bmi.run()

        assert bmi.bmi_index == 28.12
        
    @patch('builtins.input')   
    def test_display_bmi_is_underweight(self, mock_input):
        mock_input.side_effect = [50, 40]
    
        bmi = BMI()
        bmi.run()

        assert bmi.bmi_index == 11.25
        assert bmi.upper_bmi_range == 25
        assert bmi.lower_bmi_range == 18.5