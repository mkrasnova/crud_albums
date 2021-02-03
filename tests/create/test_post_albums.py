import utils.logs as log
from utils import randoms


def test_201(api):
    log.get_name(test_201)
    res = api.post(
        path='albums',
        json={'userId': 1,
              'title': randoms.get_title()})
    log.response_post(res)
    assert res.status_code == 201, 'должен быть 201'


def test_invalid_data(api):
    log.get_name(test_invalid_data)
    res = api.post(
        path='albums',
        json={'qwerty': 'qwerty'})
    log.response_post(res)
    assert res.status_code == 400, 'должен быть 400'
