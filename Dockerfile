# Базовый образ Python версии 3
FROM python:3

# Установка рабочей директории
WORKDIR /code

# Копирование зависимостей
COPY ./requirements.txt /code/

# Установка зависимостей
RUN pip install -r /code/requirements.txt

# Копирует все файлы и директории текущего каталога (где находится Dockerfile) внутрь контейнера вдиректорию /code/.
COPY . /code/
