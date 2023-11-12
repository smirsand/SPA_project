# Курсовой проект "SPA_project".
Описание проекта

Проект рассылки напоминаний привычек.

Зависимости проекта:

В файле requirements.txt указаны зависимости проекта (pip install -r requirements.txt - установка зависимостей).
Проект создавался в OS Windows.

Запуск проекта:

1. Установить Redis на компьютер.
2. Установить зависимости командой pip install -r requirements.txt
3. Создать базу данных
4. Создать файл .env, заполните его по образцу файла .env.example
5. Запустить файл csu.py командой python manage.py csu (файл user_csu.py для создания пользователей)
6. Выполните миграции командой python manage.py migrate
7. Создать суперпользователя командой python manage.py csu
8. Заполнить базу данных
9. Выполнить команду python manage.py runserver
10. Для запуска рассылки выполнить команды:
    - celery -A config worker -l info -P gevent
    - celery -A config beat -l info -S django
