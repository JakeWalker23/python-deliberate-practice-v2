from src.makingDecisions.bmiCalculator.BMI import BMI
from unittest.mock import patch
import unittest


class TestBMICalculator(unittest.TestCase):
    def test_bmi_calculate(self):
        height = 72
        weight = 182

        bmi = BMI(height, weight)
        bmi.calculate_bmi()

        assert bmi.bmi_index == 24.68

    # Need to mock input for prompt user
    # @patch.object(BMI, "prompt_user")
    # def test_prompt_user(mock_prompt_user):
    #     # GIVEN
    #     mock_prompt_user.return_value = 1

    #     # WHEN I call prompt_user
    #     bmi = BMI(2, 2)
    #     bmi.prompt_user()

    #     # THEN height and weight should be saved to the object
    #     assert bmi.height == 1
    #     assert bmi.weight == 1

    def test_display_bmi_is_ideal(self):
        height = 72
        weight = 182

        bmi = BMI(height, weight)
        bmi.calculate_bmi()
        result = bmi.display_bmi()

        assert result == '24.68. You are the ideal weight.'

    def test_display_bmi_is_overweight(self):
        height = 50
        weight = 100

        bmi = BMI(height, weight)
        bmi.calculate_bmi()
        result = bmi.display_bmi()

        assert result == '28.12. You are overweight. Please consult your doctor.'

    def test_display_bmi_is_underweight(self):
        height = 50
        weight = 40

        bmi = BMI(height, weight)
        bmi.calculate_bmi()
        result = bmi.display_bmi()

        assert result == '11.25. You are underweight. Please consult your doctor.'
