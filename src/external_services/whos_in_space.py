import requests
import pprint


class SpaceService:
    def __init__(self):
        self.__response = None

    def run(self):
        self.__response = self.query_service()
        self.display_to_std_out()

    def display_to_std_out(self):
        print(
            f"There are currently {self.__response['number']} people in space")

        pprint.pprint(self.__response['people'])

    def query_service(self):
        response = requests.get(
            'http://api.open-notify.org/astros.json')

        return response.json()

    @property
    def response(self):
        return self.__response
