import requests
import logging

log = logging.getLogger(__name__)


class API:
    """
    Класс, переопределяющий базовые методы для работы с API
    """
    def __init__(self, url):
        self.url = url + '/'

    def post(self, path='', params=None, json=None, headers=None):
        url = self.url + path
        log.info(f'\t\tЗапрос POST {url} '
                 f'params: {params}, '
                 f'data: {json}, '
                 f'headers: {headers}')
        return requests.post(url=url, params=params, json=json, headers=headers)

    def get(self, path='', params=None, headers=None):
        url = self.url + path
        log.info(f'\t\tЗапрос GET {url} '
                 f'params: {params}, '
                 f'headers: {headers}')
        return requests.get(url=url, params=params, headers=headers)

    def patch(self, path='', params=None, json=None, headers=None):
        url = self.url + path
        log.info(f'\t\tЗапрос PATCH {url} '
                 f'params: {params}, '
                 f'data: {json}, '
                 f'headers: {headers}')
        return requests.patch(url=url, params=params, json=json, headers=headers)

    def put(self, path='', params=None, json=None, headers=None):
        url = self.url + path
        log.info(f'\t\tЗапрос PUT {url} '
                 f'params: {params}, '
                 f'data: {json}, '
                 f'headers: {headers}')
        return requests.put(url=url, params=params, json=json, headers=headers)

    def delete(self, path='', params=None, json=None, headers=None):
        url = self.url + path
        log.info(f'\t\tЗапрос DELETE {url} '
                 f'params: {params}, '
                 f'data: {json}, '
                 f'headers: {headers}')
        return requests.delete(url=url, params=params, json=json, headers=headers)
