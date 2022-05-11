from src.makingDecisions.troubleshootingCarIssues.TroubleshootCarIssues import TroubleshootCarIssues
from unittest.mock import patch
from unittest import mock, TestCase
import unittest


class Test_TroubleshootCarIssues(unittest.TestCase):

    @patch('builtins.input')
    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_yes_yes(self, mock_input, mock_input1):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'yes'
        mock_input1.return_value = 'y'

        result = car_issues.run()

        assert result == "Clean terminals and try starting again."

    @patch('builtins.input')
    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_yes_n(self, mock_input, mock_input1):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'yes'
        mock_input1.return_value = 'n'

        result = car_issues.run()

        assert result == "Replace cables and try again."

    @patch('builtins.input')
    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_no_y(self, mock_input, mock_input1):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'no'
        mock_input1.return_value = 'y'

        result = car_issues.run()

        assert result == "Replace the battery."

    @patch('builtins.input')
    @mock.patch.object(TroubleshootCarIssues, "check_if_car_makes_clicking_noise")
    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_no_no_y(self, mock_input, mock_input1, mock_input2):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'no'
        mock_input1.return_value = 'no'
        mock_input2.return_value = 'y'

        result = car_issues.run()

        assert result == "Check spark plug connections."

    @patch('builtins.input')
    @mock.patch.object(TroubleshootCarIssues, "check_if_engine_starts_then_dies")
    @mock.patch.object(TroubleshootCarIssues, "check_if_car_cranks_but_fails")
    @mock.patch.object(TroubleshootCarIssues, "check_if_car_makes_clicking_noise")
    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_no_no_no_y_y(self, mock_input, mock_input1, mock_input2, mock_input3, mock_input4):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'no'
        mock_input1.return_value = 'no'
        mock_input2.return_value = 'no'
        mock_input3.return_value = 'y'
        mock_input4.return_value = 'y'

        result = car_issues.run()

        assert result == 'Get it in for service.'

    @mock.patch.object(TroubleshootCarIssues, "check_if_engine_starts_then_dies")
    @mock.patch.object(TroubleshootCarIssues, "check_if_car_cranks_but_fails")
    @mock.patch.object(TroubleshootCarIssues, "check_if_car_makes_clicking_noise")
    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_no_no_no_n(self, mock_input, mock_input1, mock_input2, mock_input3):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'no'
        mock_input1.return_value = 'no'
        mock_input2.return_value = 'no'
        mock_input3.return_value = 'n'

        result = car_issues.run()

        assert result == False

    @patch('builtins.input')
    @mock.patch.object(TroubleshootCarIssues, "check_if_engine_starts_then_dies")
    @mock.patch.object(TroubleshootCarIssues, "check_if_car_cranks_but_fails")
    @mock.patch.object(TroubleshootCarIssues, "check_if_car_makes_clicking_noise")
    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_no_no_no_y_n(self, mock_input, mock_input1, mock_input2, mock_input3, mock_input4):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'no'
        mock_input1.return_value = 'no'
        mock_input2.return_value = 'no'
        mock_input3.return_value = 'y'
        mock_input4.return_value = 'n'

        result = car_issues.run()

        assert result == 'Check to ensure the choke is opening and closing.'

    @patch('builtins.input')
    def test_check_if_engine_starts_then_dies_returns_yes(self, mock_input):
        car_issues = TroubleshootCarIssues()

        mock_input.return_value = 'y'

        result = car_issues.check_if_engine_starts_then_dies()

        assert result == 'yes'

    @patch('builtins.input')
    def test_check_if_engine_starts_then_dies_returns_false(self, mock_input):
        car_issues = TroubleshootCarIssues()

        mock_input.return_value = 'n'

        result = car_issues.check_if_engine_starts_then_dies()

        assert result == False

    @patch('builtins.input')
    def test_check_if_car_is_silent_when_turn_key(self, mock_input):
        car_issues = TroubleshootCarIssues()

        mock_input.return_value = 'y'

        result = car_issues.check_car_is_silent_when_turn_key()

        assert result == 'yes'

    @patch('builtins.input')
    def test_check_if_car_is_silent_when_turn_key_no(self, mock_input):
        car_issues = TroubleshootCarIssues()

        mock_input.return_value = 'n'

        result = car_issues.check_car_is_silent_when_turn_key()

        assert result == 'no'

    @mock.patch.object(TroubleshootCarIssues, "check_car_is_silent_when_turn_key")
    def test_troubleshoot_car_issues_root_yes_False(self, mock_input):
        car_issues = TroubleshootCarIssues()
        mock_input.return_value = 'abc'

        result = car_issues.run()

        assert result == False
