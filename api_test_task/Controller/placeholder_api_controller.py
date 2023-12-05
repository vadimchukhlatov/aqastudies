from api_test_task.Controller.rest_api_controller import RestApiController
from typing import Union


class ApiPlaceholderController(RestApiController):
    def __init__(self, api_settings: dict):
        super().__init__(api_settings=api_settings)
        self.url = api_settings['url'] + '/posts'

    def resource_usage(self, method: str, resource_body: dict = None, resource_id: int = None):
        reso_id = f'/{resource_id}/'[:-1]
        match method:
            case 'get':
                return self.get(self.url + reso_id)
            case 'post':
                return self.post(self.url, resource_body)
            case 'put':
                return self.put(self.url + reso_id, resource_body)
            case 'patch':
                return self.patch(self.url + reso_id, resource_body)
            case 'delete':
                return self.delete(self.url + reso_id)
