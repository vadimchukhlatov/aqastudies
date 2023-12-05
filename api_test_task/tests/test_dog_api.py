import random
import pytest
from api_test_task.Controller.dog_rest_api_controller import ApiDogController
from api_test_task.tests import conftest as conf

DOG_SETTINGS = conf.STAGE_SETTINGS['dogSettings']


def test_find_image():
    dog_api = ApiDogController(DOG_SETTINGS['apiSettings'])
    result = dog_api.find_random_image()
    assert result['status'] == 'success' and result['message']


@pytest.mark.parametrize('image_count', [2, 3])
def test_find_count_image(image_count):
    dog_api = ApiDogController(DOG_SETTINGS['apiSettings'])
    result = dog_api.find_random_image(image_count)
    assert result['status'] == 'success' and len(result['message']) == image_count


def test_negative_find_image():
    dog_api = ApiDogController(DOG_SETTINGS['apiSettings'])
    assert dog_api.find_random_image('sobaka/pes').json()['status'] == 'error'


@pytest.mark.parametrize('breed', ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'])
def test_find_breed(breed):
    dog_api = ApiDogController(DOG_SETTINGS['apiSettings'])
    result = dog_api.find_all_breeds()
    assert result['status'] == 'success' and breed in result['message']


def test_find_sub_breed():
    dog_api = ApiDogController(DOG_SETTINGS['apiSettings'])
    breed_list = dog_api.find_all_breeds()
    assert breed_list['status'] == 'success' and dog_api.find_sub_breed_image(random.choice(breed_list['message']))[
        'message']
