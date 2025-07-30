# Django Test Task

Веб-сервис для управления движением денежных средств (ДДС), реализованный на Django с использованием Django ORM и SQLite.

## Установка зависимостей

1. Клонируйте репозиторий:

   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Создайте и активируйте виртуальное окружение:

   python -m venv .venv
   .venv\Scripts\activate  # для Windows
   source .venv/bin/activate  # для Linux/macOS

3. Установите зависимости:

   pip install -r requirements.txt

## Настройка базы данных

1. Примените миграции:

   python manage.py migrate

## Запуск веб-сервиса

Запустите встроенный сервер Django:

   python manage.py runserver

Приложение будет доступно по адресу: http://127.0.0.1:8000

## Дополнительно

- Доступ к админке: http://127.0.0.1:8000/admin
- Для управления справочниками (статусы, типы, категории, подкатегории) используется стандартная Django admin-панель.
