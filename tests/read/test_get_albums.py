import utils.logs as log


def test_get_all_albums(api):
    log.get_name(test_get_all_albums)
    res = api.get(
        path='albums')
    log.response_get(res)
    assert res.status_code == 200, 'должен быть 200'
    assert res.json() is not [], 'ответ не должен быть пустым'
