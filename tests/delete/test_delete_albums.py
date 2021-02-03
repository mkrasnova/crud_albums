import utils.logs as log


def test_200(api):
    log.get_name(test_200)
    res = api.delete(
        path='albums/1')
    log.without_response_delete(res)
    assert res.status_code == 200, 'должен быть 200'
