from src.external_services.whos_in_space import SpaceService

from unittest.mock import patch
import unittest


class TestSpaceService(unittest.TestCase):

    @patch('src.external_services.whos_in_space.SpaceService.query_service')
    def test_space_service(self, mock_response):
        mock_response.return_value = {
            "number": 10, "people": [{"Name": "Jake"}]}

        space_service = SpaceService()
        space_service.run()

        assert space_service.response == {
            "number": 10, "people": [{"Name": "Jake"}]}
