from src.calculations.pizza_party.Pizza import Pizza
from unittest.mock import patch
import unittest


class TestPizza(unittest.TestCase):

    @patch('builtins.input')
    def test_run_integration_1(self, mock_input):

        mock_input.side_effect = [1, 1, 8]

        pizza = Pizza()
        pizza.run()

        assert pizza.people == 1
        assert pizza.pizzas == 1
        assert pizza.slices == 8
        assert pizza.slices_per_person == 8.0

    @patch('builtins.input')
    def test_run_integration_2(self, mock_input):

        mock_input.side_effect = [4, 2, 8]

        pizza = Pizza()
        pizza.run()

        assert pizza.people == 4
        assert pizza.pizzas == 2
        assert pizza.slices == 8
        assert pizza.slices_per_person == 4
