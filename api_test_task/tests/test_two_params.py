import requests

def test_last_task(get_option):
    assert requests.get(get_option[0]).status_code == get_option[1]
