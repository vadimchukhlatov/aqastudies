from api_test_task.Controller.rest_api_controller import RestApiController
from typing import Union


class ApiBreweriesController(RestApiController):
    def __init__(self, api_settings: dict):
        super().__init__(api_settings=api_settings)
        self.domain = api_settings['url']

    def find_single_brewery(self, obdb_id: str):
        end_point = f'/breweries/{obdb_id}'
        return self.get(self.domain + end_point)

    def find_filtered_list_breweries(self, **kwargs):
        """Поиск фильтруемого списка заводов

        :param kwargs:используются фильтры из ТЗ (type=micro)
        :return: (dict list)
        """
        end_point = f'/breweries?'
        for key, value in kwargs.items():
            end_point += f'{key}={value}&'
        return self.get(self.domain + end_point[:-1])
