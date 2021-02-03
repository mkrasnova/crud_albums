import utils.logs as log
from utils import randoms


def test_200(api):
    log.get_name(test_200)
    title = randoms.get_title()
    res = api.put(
        path='albums/1',
        json={'userId': 1,
              'title': title,
              'id': 1})
    log.response_put(res)
    assert res.status_code == 200, 'должен быть 200'
    assert res.json()['title'] == title, 'поле title не обновилось'
