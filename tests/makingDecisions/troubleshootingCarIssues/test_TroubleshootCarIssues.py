from src.makingDecisions.troubleshootingCarIssues.TroubleshootCarIssues import TroubleshootCarIssues
import unittest


class Test_TroubleshootCarIssues(unittest.TestCase):
    def test_troubleshoot_car_issues_root_yes_yes(self):
        car_issues = TroubleshootCarIssues()

        car_issues.troubleshoot_car_issues()

        assert car_issues.answer == 'Clean terminals and try starting again.'

    def test_troubleshoot_car_issues_root_yes_no(self):
        car_issues = TroubleshootCarIssues()

        car_issues.troubleshoot_car_issues()

        assert car_issues.answer == 'Replace cables and try again.'

    def test_troubleshoot_car_issues_root_no_yes(self):
        car_issues = TroubleshootCarIssues()

        car_issues.troubleshoot_car_issues()

        assert car_issues.answer == 'Replace the battery.'

    def test_troubleshoot_car_issues_root_no_no_yes(self):
        car_issues = TroubleshootCarIssues()

        car_issues.troubleshoot_car_issues()

        assert car_issues.answer == 'Check spark plug connections.'

    def test_troubleshoot_car_issues_root_no_no_no_yes_yes(self):
        car_issues = TroubleshootCarIssues()

        car_issues.troubleshoot_car_issues()

        assert car_issues.answer == 'Get it in for service.'

    def test_troubleshoot_car_issues_root_no_no_no_yes_no(self):
        car_issues = TroubleshootCarIssues()

        car_issues.troubleshoot_car_issues()

        assert car_issues.answer == 'Check to ensure the choke is opening and closing.'

    def test_troubleshoot_car_issues_root_no_no_no_no(self):
        car_issues = TroubleshootCarIssues()

        car_issues.troubleshoot_car_issues()

        assert car_issues.answer == 'See a specialist.'
