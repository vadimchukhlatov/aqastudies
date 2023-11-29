import requests
from api_test_task.tests import conftest as conf


class RestApiController:
    def __init__(self):
        self.api_settings = conf.API_SETTINGS

    def post(self, url, data):
        try:
            response = requests.post(url=url, json=data, auth=(self.api_settings['user'], self.api_settings['pass']))
            print(response.json())
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Тело запроса: {data}\nОтвет: {response.text}')
        except Exception as err:
            print(err)

    def get(self, url):
        try:
            response = requests.get(url=url, auth=(self.api_settings['user'], self.api_settings['pass']))
            print(response.json())
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Запрос не отправлен - {response.text}')
        except Exception as err:
            print(err)
