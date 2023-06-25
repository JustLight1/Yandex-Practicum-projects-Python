import logging
import os
import sys
import time
from http import HTTPStatus
from logging.handlers import RotatingFileHandler

import requests
import telegram
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        RotatingFileHandler(
            'main.log',
            maxBytes=50000000,
            backupCount=1,
            mode='a',
            encoding='Windows 1251'),
        logging.StreamHandler(stream=sys.stdout)],
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s'
)

load_dotenv()


PRACTICUM_TOKEN = os.getenv('TOKEN_PRACTICUM')
TELEGRAM_TOKEN = os.getenv('TOKEN_TELEGRAM')
TELEGRAM_CHAT_ID = os.getenv('CHAT_ID_TELEGRAM')

RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}


HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def check_tokens():
    """
    Проверка доступности переменных окружения.
    """
    return all([PRACTICUM_TOKEN, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID])


def send_message(bot, message):
    """Отправка сообщения."""
    try:
        logging.debug(f'Начало отправки сообщения - "{message}".')
        bot.send_message(TELEGRAM_CHAT_ID, message)
    except Exception as error:
        logging.error(error)


def get_api_answer(timestamp):
    """
    Делает запрос к эндпоинту API-сервиса.
    В случае успешного запроса возвращает ответ API,
    приводя его из формата JSON к типам данных Python.
    """
    payload = {'from_date': timestamp}
    try:
        response = requests.get(
            ENDPOINT,
            headers=HEADERS,
            params=payload
        )
    except Exception as error:
        logging.info(
            f'Ошибка при отправке запроса к API: {error}.'
        )
    if response.status_code != HTTPStatus.OK:
        raise ConnectionError(
            'Не удалось подключиться к API, '
            f'код ответа: {response.status_code}.'
        )
    return response.json()


def check_response(response):
    """
    Проверка ответа API на соответствие документации.
    Если ответ API соответствует ожиданиям,
    то функция должна вернуть список домашних работ (он может быть и пустым),
    доступный в ответе API по ключу 'homeworks'.
    """
    if not isinstance(response, dict):
        raise TypeError(
            f'Некорректный тип данных: {type(response)}, ожидался словарь.'
        )
    if 'homeworks' not in response:
        raise KeyError('Нет нужного ключа.')
    homework = response['homeworks']
    if not isinstance(homework, list):
        raise TypeError(
            'Неккоректный тип данных: '
            f'{type(response["homeworks"])}, ожидался список.'
        )
    return homework


def parse_status(homework):
    """
    Извлекает из информации о конкретной домашней работе статус этой работы.
    В случае успеха, функция возвращает подготовленную для отправки
    в Telegram строку.
    """
    if 'homework_name' not in homework:
        raise KeyError('Отсутствует ключ "homework_name".')
    homework_name = homework['homework_name']
    if 'status' not in homework:
        raise KeyError('Отсутствует ключ "status".')
    status = homework['status']
    if status not in HOMEWORK_VERDICTS:
        raise KeyError(f'Неизвестный статут {status}.')
    verdict = HOMEWORK_VERDICTS[status]
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def main():
    """Основная логика работы бота."""
    if not check_tokens():
        message = 'Отсутствует токен. Работа бота невозможна!'
        logging.critical(message)
        exit()
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    timestamp = int(time.time())
    msg = ''
    while True:
        try:
            response = get_api_answer(timestamp)
            homeworks = check_response(response)
            if homeworks:
                message = parse_status(homeworks[0])
            else:
                message = 'Статус работы не изменился'
            if message != msg:
                send_message(bot, message)
                msg = message
        except Exception as error:
            message = f'Сбой в работе программы: {error}.'
            logging.error(message)
            if message != msg:
                send_message(bot, message)
                msg = message
        finally:
            time.sleep(RETRY_PERIOD)


if __name__ == '__main__':
    main()
