<div align=center>

# Проект Kittygram-Docker

![Python](https://img.shields.io/badge/Python-3.9.10-blue)
![Django](https://img.shields.io/badge/Django-3.2.3-blue)
![Django_REST_framework](https://img.shields.io/badge/Django_REST_framework-3.12.4-blue)
![Nginx](https://img.shields.io/badge/Nginx-1.22.1-blue)
![Gunicorn](https://img.shields.io/badge/Gunicorn-20.1.0-blue)
![Docker](https://img.shields.io/badge/Docker-4.20.10-blue)
![Postgres](https://img.shields.io/badge/Postgres-13.10-blue)
</div>

## Описание проекта

Kittygram - SPA, предназначенное для всех, кто увлекается котиками и хочет делиться фотографиями и достижениями своих питомцев с другими пользователями.

В Kittygram предоставлены интерфейсы для регистрации новых и для аутентификации зарегистрированных пользователей.

Аутентифицированным пользователям проект позволяет добавлять новых питомцев на сайт.

Для каждого нового котика нужно указать его имя, год рождения и достижения(выбрать из уже существующих или создать новое), выбрать цвет . Опционально можно загрузить фотографию своего питомца; для котиков без фотографии будет выводиться изображение по умолчанию. Информацию о собственных котах можно изменить или вовсе удалить с сайта.

На одной странице отображается не более десяти котиков.

Все вышеперечисленные возможности работают на базе API

## Ресурсы API:
- Ресурс **cats**: котики
- Ресурс **achivements**: достижения котиков
- Ресурс **users**: пользователи
- Ресурс **token**: создание токена

### Как запустить проект на удаленном сервере:

1. Подключиться к удалённому серверу (Linux Ubuntu 22.04 с публичным ip):

   ```
   $ ssh -i путь_до_файла_с_SSH_ключом/название_файла_с_SSH_ключом_без_расширения login@ip
   ```

2. Клонировать репозиторий:
   ```
   $ git clone git@github.com:JustLight1/kittygram_final.git
   ```

3. В файле main.yml указать необходимые переменные:
    * Например:

        ```
        username: ${{ secrets.USER }} -> username: Light
        ```

4. Создать секретный ключ приложения:

    * Создать файл .env в папке ```/kittygram/backend```

    * Сгенерировать секретный ключ с помощью команды:

        ```
        (venv) $ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
        ```

    *  Записать полученный ключ в файл .env по принципу:

        ```
        SECRET_KEY=<Ваш секретный ключ>
        ```
        > Без пробелов и <>

5. Выполнить git push в ветку main, git push запускает тестирование и деплой проекта, а после успешного деплоя вам приходит сообщение в телеграм.


## Контакты
**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)