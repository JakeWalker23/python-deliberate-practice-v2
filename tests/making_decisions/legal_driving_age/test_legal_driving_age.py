from src.making_decisions.legal_driving_age.LegalDrivingAge import DrivingAge
from unittest.mock import patch
import unittest


class TestDrivingAge(unittest.TestCase):

    @patch('builtins.input')
    def test_is_legal_driving_age_all(self, mock_input):
        mock_input.return_value = 25

        driving_age = DrivingAge()
        driving_age.run()

        assert driving_age.driving_age == 25
        assert driving_age.legal_drive == True
        
        assert "England" in driving_age.legal_countries
        assert "Scotland" in driving_age.legal_countries
        assert "Ireland" in driving_age.legal_countries
        assert "Wales" in driving_age.legal_countries
        assert "USA" in driving_age.legal_countries
        assert "Germany" in driving_age.legal_countries
        assert "Australia" in driving_age.legal_countries
        assert "Poland" in driving_age.legal_countries
        
    @patch('builtins.input')
    def test_is_legal_driving_age_17(self, mock_input):
        mock_input.return_value = 17

        driving_age = DrivingAge()
        driving_age.run()

        assert driving_age.driving_age == 17
        assert driving_age.legal_drive == True
        assert driving_age.minimum_driving_age == 16
        
        assert "USA" in driving_age.legal_countries
        assert "Australia" in driving_age.legal_countries
    
    @patch('builtins.input')
    def test_is_legal_driving_age_15(self, mock_input):
        mock_input.return_value = 15

        driving_age = DrivingAge()
        driving_age.run()

        assert driving_age.driving_age == 15
        assert driving_age.legal_drive == False
        assert driving_age.minimum_driving_age == 16
        
        assert len(driving_age.legal_countries) == 0