import pytest
from api_test_task.Controller.placeholder_api_controller import ApiPlaceholderController
from api_test_task.tests import conftest as conf
from api_test_task.Classes.placeholder_class import ApiPlaceholderBody

CONNECT_SETTINGS = conf.STAGE_SETTINGS['placeholderSettings']


@pytest.mark.parametrize('resource_id', [1, 23])
def test_get_resources(resource_id):
    api = ApiPlaceholderController(CONNECT_SETTINGS['apiSettings'])
    result = api.resource_usage(method='get', resource_id=resource_id)
    assert result['id'] == resource_id


def test_create_resource():
    api = ApiPlaceholderController(CONNECT_SETTINGS['apiSettings'])
    term = ApiPlaceholderBody()
    resource_body = term.create_resource_body()
    result = api.resource_usage(method='post', resource_body=resource_body).json()
    assert (result['title'] == resource_body['title']) and (result['userId'] == resource_body['userId'])


@pytest.mark.parametrize('resource_id', [4, 66])
def test_update_resource(resource_id):
    api = ApiPlaceholderController(CONNECT_SETTINGS['apiSettings'])
    term = ApiPlaceholderBody()
    resource_body = term.create_resource_body(resource_id)
    result = api.resource_usage(method='put', resource_body=resource_body, resource_id=resource_id)
    assert (result['title'] == resource_body['title']) and (result['id'] == resource_body['id'])


@pytest.mark.parametrize('change_key', ['title', 'body'])
def test_patch_resource(change_key):
    api = ApiPlaceholderController(CONNECT_SETTINGS['apiSettings'])
    result = api.resource_usage(method='patch', resource_body={change_key: "perekusTaksistaCheeeck"}, resource_id=3)
    assert (result[change_key] == "perekusTaksistaCheeeck") and (result['id'] == 3)


def test_delete_resource():
    api = ApiPlaceholderController(CONNECT_SETTINGS['apiSettings'])
    result = api.resource_usage(method='delete', resource_id=2)
    assert result.status_code == 200
