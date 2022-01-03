from src.makingDecisions.multistateTaxCalculator.multistateTaxCalculator import MultiStateTaxCalculator
import unittest


class TestMultiStateTaxCalculator(unittest.TestCase):

    def test_calculate_tax_for_non_selected_state(self):
        multiState = MultiStateTaxCalculator()
        multiState.order_amount = 100
        multiState.state = 'New york'

        multiState.calculateTax()

        assert multiState.total == 100

    def test_calculate_tax_for_illinois_state(self):
        multiState = MultiStateTaxCalculator()
        multiState.order_amount = 10
        multiState.state = 'Illinois'

        multiState.calculateTax()

        assert multiState.total == 10.80

    def test_calculate_tax_for_wisconsin_state(self):
        multiState = MultiStateTaxCalculator()
        multiState.order_amount = 500
        multiState.state = 'Wisconsin'
        multiState.county = 'Lafayette'

        multiState.calculateTax()

        assert multiState.total == 500

    def test_calculate_tax_for_wisconsin_state_eau_claire_county(self):
        multiState = MultiStateTaxCalculator()
        multiState.order_amount = 100
        multiState.state = 'Wisconsin'
        multiState.county = 'eau claire'

        multiState.calculateTax()

        assert multiState.total == 100.4

    def test_calculate_tax_for_wisconsin_state_dunn_county(self):
        multiState = MultiStateTaxCalculator()
        multiState.order_amount = 100
        multiState.state = 'Wisconsin'
        multiState.county = 'dunn'

        multiState.calculateTax()

        assert multiState.total == 100.5
