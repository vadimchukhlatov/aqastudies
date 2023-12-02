import random
import pytest
from api_test_task.Controller.breweries_rest_api_controller import ApiBreweriesController
from api_test_task.tests import conftest as conf

BREWERIES_SETTINGS = conf.STAGE_SETTINGS['brewerySettings']


@pytest.mark.parametrize('per_page', [1, 2])
def test_list_breweries(per_page):
    brewery_api = ApiBreweriesController(BREWERIES_SETTINGS['apiSettings'])
    assert len(brewery_api.find_filtered_list_breweries(per_page=per_page)) == per_page


def test_find_breweries_by_id():
    brewery_api = ApiBreweriesController(BREWERIES_SETTINGS['apiSettings'])
    list_breweries = random.choice(brewery_api.find_filtered_list_breweries(per_page=5))
    result = brewery_api.find_single_brewery(list_breweries['id'])
    assert result['id'] == list_breweries['id'] and result['address_1'] == list_breweries['address_1']


@pytest.mark.parametrize('by_type',
                         ['micro', 'regional', 'nano', 'brewpub', 'large',
                          'planning', 'bar', 'contract', 'proprietor', 'closed'])
def test_find_by_type(by_type):
    brewery_api = ApiBreweriesController(BREWERIES_SETTINGS['apiSettings'])
    brewery_list = brewery_api.find_filtered_list_breweries(per_page=random.randint(1, 10), by_type=by_type)
    for brewery in brewery_list:
        assert brewery['brewery_type'] == by_type


def test_negative_find_by_id():
    brewery_api = ApiBreweriesController(BREWERIES_SETTINGS['apiSettings'])
    result = brewery_api.find_single_brewery('2')
    assert result.status_code == 404 and result.json()['message'] == "Couldn't find Brewery"


def test_negative_find_by_type():
    brewery_api = ApiBreweriesController(BREWERIES_SETTINGS['apiSettings'])
    error_msg = brewery_api.find_filtered_list_breweries(by_type='fake_type')
    assert 'Brewery type must include one of these types:' in error_msg.text
