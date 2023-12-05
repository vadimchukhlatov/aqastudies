from api_test_task.Controller.rest_api_controller import RestApiController
from typing import Union


class ApiDogController(RestApiController):
    def __init__(self, api_settings: dict):
        super().__init__(api_settings=api_settings)
        self.domain = api_settings['url']

    def find_all_breeds(self):
        end_point = '/api/breed/hound/list'
        return self.get(self.domain + end_point)

    def find_sub_breed_image(self, breed: str):
        end_point = f'/api/breed/hound/{breed}/images/random'
        return self.get(self.domain + end_point)

    def find_random_image(self, image_count: Union[str, int] = None):
        end_point = f'/api/breeds/image/random/{image_count}'
        return self.get(self.domain + end_point)
