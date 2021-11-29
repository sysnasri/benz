
import json
import requests


class UrlResponse:
    def __init__(self, url):
        self.base = url
        response = requests.get(f"{self.base}/api/users/")
        self.pages = json.loads(response.text)['total_pages']

    @property
    def fetch_users(self):
        data_response = []
        for pages in range(self.pages + 1):
            response_body = requests.get(
                f"{self.base}/api/users?page={pages}")
            data_response.append(json.loads(response_body.text)['data'])

        return data_response
