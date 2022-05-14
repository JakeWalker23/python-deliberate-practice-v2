import unittest
from src.calculations.area_of_rectangle_room.Room import Room
from unittest.mock import patch


class Test_Room(unittest.TestCase):

    @patch('builtins.input')
    def test_run(self, mocked_input_1):
        mocked_input_1.side_effect = [5.125, 10.5]

        room = Room()
        room.run()

        assert room.area == 53.8125
        assert room.meter_area == 16.40205
        assert room.squared_meter_area == 269.0272442025

    @patch('builtins.input')
    def test_run_2(self, mocked_input_1):
        mocked_input_1.side_effect = [1, 1]

        room = Room()
        room.run()

        assert room.area == 1
        assert room.meter_area == 0.3048
