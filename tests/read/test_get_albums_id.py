import utils.logs as log
import pytest


@pytest.mark.parametrize('id_album', [i for i in range(1, 6)])
def test_get_album(api, id_album):
    log.get_name(test_get_album)
    res = api.get(
        path=f'albums/{id_album}')
    log.response_get(res)
    assert res.status_code == 200, 'должен быть 200'
    assert res.json() is not [], 'ответ не должен быть пустым'
    assert res.json()['id'] == id_album, 'в ответе некорректный id'
