import pytest
import logging

from .api_object.API import API

log = logging.getLogger(__name__)


def pytest_addoption(parser):
    """
    Параметры из командной строки
    """
    parser.addoption(
        '--url',
        help='This is request url',
        default='https://jsonplaceholder.typicode.com'
    )


@pytest.fixture(scope='session')
def api(request):
    """
    Фикстура инициализации объекта с параметрами из командной строки
    """
    url = request.config.getoption('--url')
    log.info(f'Параметры прогона: url {url}')
    return API(url)

