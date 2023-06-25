# Социальная сеть Yatube для публикации личных дневников
![Python](https://img.shields.io/badge/Python-3.9.10-blue) ![!Django](https://img.shields.io/badge/Django-2.2.9-blue)

## Описание проекта
Социальная сеть для авторов и подписчиков. Пользователи могут подписываться на избранных авторов, оставлять и удалять комментари к постам, оставлять новые посты на главной странице и в тематических группах, прикреплять изображения к публикуемым постам.

- Добавлена возможность публикации постов с изображениями;
- Создана система комментариев;
- Добавлена система подписок;
- Добавлено кешировние;
- Все вышеперечисленное покрыто тестами.

## Запуск сервера

 Для MacOs и Linux вместо python использовать python3

1. Клонировать репозиторий.
   ```
   $ git clone git@github.com:JustLight1/Yandex-Practicum-projects-Python.git
   ```
2. Cоздать и активировать виртуальное окружение:
    ```
      $ cd Yandex-Practicum-projects-Python/02_Yatube
      $ python -m venv venv
    ```
    Для Windows:
    ```
      $ source venv/Scripts/activate
    ```
    Для MacOs/Linux:
    ```
      $ source venv/bin/activate
    ```
3. Установить зависимости из файла requirements.txt:
    ```
    (venv) $ python -m pip install --upgrade pip
    (venv) $ pip install -r requirements.txt
    ```
4. Создать и запустить миграции:
    ```
    cd yatube/
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Запустить сервер:
    ```
    python manage.py runserver
    ```
> После выполнения вышеперечисленных инструкций проект доступен по адресу http://127.0.0.1:8000/

## Контакты
**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)

