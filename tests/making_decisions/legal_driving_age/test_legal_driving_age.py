from src.making_decisions.legal_driving_age.LegalDrivingAge import DrivingAge
import unittest


class TestDrivingAge(unittest.TestCase):

    def test_is_legal_driving_age(self):
        '''tests that 25 is a legal driving age'''
        age = 25

        driving_age = DrivingAge()
        driving_age.driving_age = age

        driving_age.compare_driving_age()

        assert driving_age.legal_drive == True

    def test_is_not_legal_driving_age(self):
        '''tests that 15 is not a legal driving age'''
        age = 15

        driving_age = DrivingAge()
        driving_age.driving_age = age

        driving_age.compare_driving_age()

        assert driving_age.legal_drive == False

    def test_legal_countries(self):
        '''tests that 17 is a legal driving age in Australia and USA'''
        age = 17

        driving_age = DrivingAge()
        driving_age.driving_age = age

        driving_age.filter_legal_countries()
        legal_countries = driving_age.legal_countries

        assert "Australia" in legal_countries
        assert "USA" in legal_countries
        assert "England" not in legal_countries
        assert "Scotland" not in legal_countries

    def test_illegal_countries(self):
        '''Tests that 18 is a legal driving age in England Scotland Ireland Wales'''
        age = 18

        driving_age = DrivingAge()
        driving_age.driving_age = age

        driving_age.filter_legal_countries()
        legal_countries = driving_age.legal_countries

        assert "England" in legal_countries
        assert "Scotland" in legal_countries
        assert "Ireland" in legal_countries
        assert "Wales" in legal_countries
