from src.makingDecisions.legalDrivingAge.LegalDrivingAge import DrivingAge
import unittest


class TestDrivingAge(unittest.TestCase):

    def test_is_legal_driving_age(self):
        age = 25

        driving_age = DrivingAge()
        driving_age.driving_age = age

        driving_age.compare_driving_age()

        assert driving_age.legal_drive == True

    def test_is_not_legal_driving_age(self):
        age = 15

        driving_age = DrivingAge()
        driving_age.driving_age = age

        driving_age.compare_driving_age()

        assert driving_age.legal_drive == False
