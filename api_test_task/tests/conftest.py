import os.path
import sys
import pytest

WD = os.path.abspath(os.path.dirname(sys.argv[0]))


def pytest_addoption(parser):
    parser.addoption("--service", default='brewery_settings', help="dog_settings, brewery_settings")
    parser.addoption("--expected", default=200, type=int, help="Expected value")


STAGE_SETTINGS = {
    'dogSettings': {
        'apiSettings': {
            'url': 'https://dog.ceo',
            'user': 'qwerty123',
            'pass': 'qwerty123'
        }
    },
    'brewerySettings': {
        'apiSettings': {
            'url': 'https://api.openbrewerydb.org/v1',
            'user': 'qwerty',
            'pass': 'qwerty'
        }
    }
}


@pytest.fixture(scope='session')
def connection_info(request):
    return STAGE_SETTINGS[request.config.getoption('service')]
