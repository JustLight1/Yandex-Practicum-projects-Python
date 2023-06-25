<div align=center>

# Проект Kittygram

![Python](https://img.shields.io/badge/Python-3.9.10-blue)
![Django](https://img.shields.io/badge/Django-3.2.16-blue)
![Django_REST_framework](https://img.shields.io/badge/Django_REST_framework-3.12.4-blue)
![Nginx](https://img.shields.io/badge/Nginx-1.18.0-blue)
![Gunicorn](https://img.shields.io/badge/Gunicorn-20.1.0-blue)
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
   $ git clone git@github.com:JustLight1/Yandex-Practicum-projects-Python.git
   ```

3. Cоздать и активировать виртуальное окружение:

   ```
      $ cd backend/
      $ python -m venv venv
      $ source venv/bin/activate
   ```

4. Установить зависимости из файла requirements.txt:

    ```
    (venv) $ python -m pip install --upgrade pip
    (venv) $ pip install -r requirements.txt
    ```
5. Создать секретный ключ приложения:

    * Создать файл .env в папке ```/infra_sprint1/backend```

    * Сгенерировать секретный ключ с помощью команды:

        ```
        (venv) $ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
        ```

    *  Записать полученный ключ в файл .env по принципу:

        ```
        SECRET_KEY=<Ваш секретный ключ>
        ```
        > Без пробелов и <>

6. Выполнить миграции:

    ```
    (venv) $ python manage.py migrate
    ```

7. Установить Gunicorn:

    ```
    pip install gunicorn==20.1.0
    ```

8. Создать юнит для Gunicorn:

    ```
    sudo nano /etc/systemd/system/gunicorn_kittygram.service 
    ```
    Прописать
    ```
    [Unit]
    Description=gunicorn daemon 
    After=network.target 

    [Service]
    User=<Имя пользователя> 
    
    WorkingDirectory=<Путь к директории проекта>
    
    ExecStart=<директория-с-проектом>/<путь-до-gunicorn-в-виртуальном-окружении> --bind 0.0.0.0:8000 kyttygram_backend.wsgi
    
    [Install]
    WantedBy=multi-user.target
    ```

9. Запустить созданный юнит:

    ```
    sudo systemctl start gunicorn_kittygram     
    ```

10. Установить Nginx:

    ```
    sudo apt install nginx -y 
    ```

11. Настроить и запустить файрвол:

    ```
    sudo ufw allow 'Nginx Full'
    sudo ufw allow OpenSSH
    sudo ufw enable
    ```

12. Собрать статику фронтенд-приложения и скопировать её в системную директорию Nginx:

    * Перейти в директорию kittygram/frontend и выполнить команду:

        ```
            npm run build
        ```

    * Скопировать созданную папку в /var/www

        ```
        sudo cp -r /infra_sprint1/frontend/build/. /var/www/kittygram/ 
        ```

13. Прописать конфиг веб-сервера:

    ```
     sudo nano /etc/nginx/sites-enabled/default
    ```

    ```
    server {
        server_name kittygramlight.ddns.net;

        location /media/ {
            alias /var/www/kittygram/media/;
        }

        location /admin/ {
            proxy_pass http://127.0.0.1:8000;
        }
    
        location /api/ {
            proxy_pass http://127.0.0.1:8000;
        }
    
        location /redoc/ {
            proxy_pass http://127.0.0.1:8000;
        }
    
        location / {
            root   /var/www/kittygram;
            index  index.html index.htm;
            try_files $uri /index.html;
        }
    }
    ```

14. Перезагрузить Nginx:

    ```
    sudo systemctl reload nginx
    ```

15. Собрать статику и перенести её в Nginx:

    ```
    (venv) $ python manage.py collectstatic
    ```
    ```
        sudo cp -r /infra_sprint1/backend/static_backend/. /var/www/kittygram/
    ```

16. Cоздать директорию media в директории /var/www/kittygram/

17. При необходимости настроить SSL-соединение.


## Контакты
**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
