# Модуль фитнес-трекера
![Python](https://img.shields.io/badge/Python-3.9.10-blue)
## Описание проекта

Модуль для фитнес трекера, рассчитывающий и отображающий полную информацию о тренировках по данным от блока датчиков

## Функционал модуля
- принимает от блока датчиков информацию о прошедшей тренировке,
- определяет вид тренировки,
- рассчитывает результаты тренировки,
- выводит информационное сообщение о результатах тренировки, включающее в себя:
    - тип тренировки (бег, ходьба или плавание);
    - длительность тренировки;
    - дистанция, которую преодолел пользователь, в километрах;
    - среднюю скорость на дистанции, в км/ч;
    - расход энергии, в килокалориях.


## Установка и запуск

 Для MacOs и Linux вместо python использовать python3

1. Клонировать репозиторий.
   ```
   $ git clone git@github.com:JustLight1/Yandex-Practicum-projects-Python.git
   ```
2. Cоздать и активировать виртуальное окружение:
    ```
      $ cd Yandex-Practicum-projects-Python/01_fitness_tracker
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
4. Запустить проект
    ```
    python homework.py
    ```

## Контакты
**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
