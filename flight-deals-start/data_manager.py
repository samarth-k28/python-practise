import requests
from main import iatta_codes
class DataManager:
    def get_data(self):
        url = 'https://api.sheety.co/533b0f93a2d968bafefe717915530f3a/copyOfFlightDeals/prices'
        response = requests.get(url)
        data = response.json()
        return data


    # def add_iatta_codes(self):

        