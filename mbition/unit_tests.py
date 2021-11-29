import unittest
import json
import requests


class TestApiStatus(unittest.TestCase):
    def test_api_url_status(self):
        base_url = "http://reqres.in"
        response = requests.get(base_url)
        self.assertEqual(response.status_code, 200)

    def test_user_pages_list(self):
        base_url = "http://reqres.in"
        response = requests.get(f"{base_url}/api/users/")
        user_list = json.loads(response.text)['total']
        total_pages = json.loads(response.text)['total_pages']
        self.assertGreaterEqual(user_list, 12)
        self.assertGreaterEqual(total_pages, 1)

    def test_data_is_list(self):
        self.base = "http://reqres.in"
        response = requests.get(f"{self.base}/api/users/")
        data = json.loads(response.text)['data']
        self.assertTrue(list(data))


if __name__ == '__main__':
    unittest.main()
