import json
import requests

class Server:
    address = 'https://intelligent-nurse.azurewebsites.net/Translation/set'

    def __init__(self, address = None):
        if address:
            self.address = address

    def get_response(self):
        address = self.address
        return requests.get(address).status_code

    def send_request(self, data):
        url = self.address
        payload = {'some':'data'}
        headers = {'parameters':'880777'}
        
        return(requests.post(url, data=json.dumps(payload), headers=headers).status_code)
