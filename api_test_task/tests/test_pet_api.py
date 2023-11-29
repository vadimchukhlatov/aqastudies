import pytest
from api_test_task.Controller.pet_rest_api_controller import ApiPetController


@pytest.mark.parametrize('status', ['available', 'pending', 'sold', 'another',  None, 1, ''])
def test_find_pets_by_status(status):
    pet_api = ApiPetController()
    for resp in pet_api.find_by_status(status):
        assert resp['status'] == status or int(status)
