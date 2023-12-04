import requests
from typing import Union


class RestApiController:
    def __init__(self, api_settings: dict):
        self.api_settings = api_settings

    def post(self, url, data: Union[dict, list, None] = None):
        try:
            response = requests.post(url=url, json=data, auth=(self.api_settings['user'], self.api_settings['pass']))
            if response.status_code == 200:
                print(response.json())
                return response.json()
            else:
                print(f'Тело запроса: {data}\nОтвет: {response.text}')
                return response
        except Exception as err:
            print(err)

    def get(self, url):
        try:
            response = requests.get(url=url, auth=(self.api_settings['user'], self.api_settings['pass']))
            if response.status_code == 200:
                print(response.json())
                return response.json()
            else:
                print(f'Запрос не отправлен - {response.text}')
                return response
        except Exception as err:
            print(err)

    def put(self, url, data: Union[dict, list, None] = None):
        try:
            response = requests.put(url=url, json=data, auth=(self.api_settings['user'], self.api_settings['pass']))
            if response.status_code == 200:
                print(response.json())
                return response.json()
            else:
                print(f'Тело запроса: {data}\nОтвет: {response.text}')
                return response
        except Exception as err:
            print(err)

    def patch(self, url, data: Union[dict, list, None] = None):
        try:
            response = requests.patch(url=url, json=data, auth=(self.api_settings['user'], self.api_settings['pass']))
            if response.status_code == 200:
                print(response.json())
                return response.json()
            else:
                print(f'Тело запроса: {data}\nУРЛ: {url}\nОтвет: {response.text}')
                return response
        except Exception as err:
            print(err)

    def delete(self, url):
        try:
            response = requests.delete(url=url, auth=(self.api_settings['user'], self.api_settings['pass']))
            if response.status_code == 200:
                return response
            else:
                print(f'Запрос не отправлен - {response.text}')
                return response
        except Exception as err:
            print(err)
