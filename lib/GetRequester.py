import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
          # Fetch the raw response from the URL
        response = requests.get(self.url)
        return response.content

        

    def load_json(self):
        # Parse the raw JSON string into a Python object
        response_body = self.get_response_body()
        return json.loads(response_body)
        