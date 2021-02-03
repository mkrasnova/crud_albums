import json
import logging

log = logging.getLogger(__name__)


def response_post(res):
    try:
        log.info(f'\t\tОтвет POST {res.url} '
                 f'status_code: {res.status_code} '
                 f'response: {res.json()}')
    except json.decoder.JSONDecodeError:
        log.critical(f'Ответ POST {res.url} '
                     f'status_code: {res.status_code}')


def without_response_post(res):
    log.info(f'\t\tОтвет POST {res.url} '
             f'status_code: {res.status_code}')


def response_get(res):
    try:
        log.info(f'\t\tОтвет GET {res.url} '
                 f'status_code: {res.status_code} '
                 f'response: {res.json()}')
    except json.decoder.JSONDecodeError:
        log.critical(f'Ответ GET {res.url} '
                     f'status_code: {res.status_code}')


def response_put(res):
    try:
        log.info(f'\t\tОтвет PUT {res.url} '
                 f'status_code: {res.status_code} '
                 f'response: {res.json()}')
    except json.decoder.JSONDecodeError:
        log.critical(f'Ответ PUT {res.url} '
                     f'status_code: {res.status_code}')


def response_patch(res):
    try:
        log.info(f'\t\tОтвет PATCH {res.url} '
                 f'status_code: {res.status_code} '
                 f'response: {res.json()}')
    except json.decoder.JSONDecodeError:
        log.critical(f'Ответ PATCH {res.url} '
                     f'status_code: {res.status_code}')


def without_response_delete(res):
    log.info(f'\t\tОтвет DELETE {res.url} '
             f'status_code: {res.status_code}')


def get_name(func):
    log.info(f'Запуск теста {func.__name__} из модуля {func.__module__}:')
