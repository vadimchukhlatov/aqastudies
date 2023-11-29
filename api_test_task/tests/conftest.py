import os.path
import sys

WD = os.path.abspath(os.path.dirname(sys.argv[0]))


def pytest_addoption(parser):
    parser.addoption("--actual", help="Actual value")
    parser.addoption("--expected", default=200, type=int, help="Expected value")


STAGE = 'pet_settings'

STAGE_SETTINGS = {
    'pet_settings': {
        'apiSettings': {
            'url': 'https://dog.ceo/api',
            'user': 'qwerty',
            'pass': 'qwerty'
        },
        'dbSettings': {
            'url': 'https://petstore.swagger.io/v2',
            'user': 'qwerty',
            'pass': 'qwerty'
        },
        'domain': {
            'pet': '/pet',
            'store': '/store',
            'user': '/user'
        }
    }
}

API_SETTINGS = STAGE_SETTINGS[STAGE]['apiSettings']
DB_SETTINGS = STAGE_SETTINGS[STAGE]['dbSettings']
DOMAIN_SETTINGS = STAGE_SETTINGS[STAGE]['domain']
