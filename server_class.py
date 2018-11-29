import json
import requests

class Server:
    address = 'https://intelligentnurse.azurewebsites.net/Translation/Set'
    ID = '999666111'
    location = ''

    def __init__(self, address = None):
        if address:
            self.address = address

    def get_response(self):
        location = None
        address = self.address
        try:
            headers = requests.get(address, 
                    headers={'parameters':self.ID}).headers
            if "Location" in headers:
                location = headers["Location"]
        except:
            print("\nFailed to establish connection")
        return location

    def send_request(self, data):
        url = self.address + '/' + self.location
        headers = {'parameters':self.ID}
        
        return(requests.post(url, data=data, headers=headers).status_code)
    
    def set_location(self, location):
        self.location = location
