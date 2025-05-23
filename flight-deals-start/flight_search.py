import requests
import os


class FlightSearch:
    def __init__(self):
        self.api_key = os.environ.get('api_key')
        self.api_secret = os.environ.get('api_secret')

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url='https://test.api.amadeus.com/v1/security/oauth2/token', headers=header, data=body)
        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    def iata_code(self, city):
        url ='https://test.api.amadeus.com/v1/reference-data/locations/cities'
        parameters ={'keyword': city, 'max': 2}
        header={"Authorization": f"Bearer {self._get_new_token}"}
        response = requests.get(url, params=parameters, headers=header)
        result= response.json()
        return result['data'][0]['iataCode']
