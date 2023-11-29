from api_test_task.Controller.rest_api_controller import RestApiController


class ApiPetController(RestApiController):
    def find_all_breeds(self):
        end_point = '/breed/hound/list'
        return self.get(self.api_settings['url'] + end_point)

    def find_all_sub_breed(self):
        end_point = '/breed/hound/lis'
        return self.get(self.api_settings['url'] + end_point)
