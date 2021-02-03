import utils.logs as log
from utils import randoms


def test_200(api):
    log.get_name(test_200)
    title = randoms.get_title()
    res = api.patch(
        path='albums/1',
        json={'title': title})
    log.response_patch(res)
    assert res.status_code == 200, 'должен быть 200'
    assert res.json()['title'] == title, 'поле title не изменилось'
