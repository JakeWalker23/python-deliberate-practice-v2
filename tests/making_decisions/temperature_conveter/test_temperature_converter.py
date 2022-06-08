from src.making_decisions.temperature_converter.TemperatureConverter import TemperatureConverter
from unittest.mock import patch
import unittest

class Test_TemperatureConverter(unittest.TestCase):
    
    @patch('builtins.input')
    def test_temperature_converter_run(self, mock_input):
        mock_input.side_effect = ["C", 500]
        
        temperature_converter = TemperatureConverter()
        temperature_converter.run()
        
        assert temperature_converter.result == 260.0
        assert temperature_converter.metric == "C"
        assert temperature_converter.temperature == 500
        
    @patch('builtins.input')
    def test_temperature_converter_run(self, mock_input):
        mock_input.side_effect = ["F", 500]
        
        temperature_converter = TemperatureConverter()
        temperature_converter.run()
        
        assert temperature_converter.result == 932.0
        assert temperature_converter.metric == "F"
        assert temperature_converter.temperature == 500