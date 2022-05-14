import unittest
from src.calculations.area_of_rectangle_room.Room import Room
from unittest.mock import patch


class Test_Room(unittest.TestCase):

    @patch('builtins.input')
    @patch('builtins.input')
    def test_run(self, mocked_input_1, mocked_input_2):
        mocked_input_1.return_value = 5.5
        mocked_input_2.return_value = 5.5

        room = Room()
        room.run()

        assert room.area == 30.25
        assert room.meter_area == 9.2202
        assert room.squared_meter_area == 85.01208804000001

    @patch('builtins.input')
    @patch('builtins.input')
    def test_run_2(self, mocked_input_1, mocked_input_2):
        mocked_input_1.return_value = 1
        mocked_input_2.return_value = 1

        room = Room()
        room.run()

        assert room.area == 1
        assert room.meter_area == 0.3048
