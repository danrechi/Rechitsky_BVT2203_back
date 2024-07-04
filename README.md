# Parser Backend

## Описание

Это FastAPI-приложение для парсинга вакансий с сайта HH.ru и сохранения их в базу данных PostgreSQL.

## Установка и запуск

### Локальный запуск

1. Устанавливаем зависимости:
    ```bash
    pip install -r requirements.txt
    ```
2. Запускаем PostgreSQL сервер и создаем DATABASE с названием <your_dbname>
3. Переходим в db.py и меняем строку DATABASE_URL на свои данные:
    ```python
    DATABASE_URL=postgresql://<username>:<password>@<hostname>/<your_dbname>
    ```
4. Запустите приложение:
    ```bash
    uvicorn main:app --reload
    ```

### Запуск с использованием Docker

1. Убеждаемся, что Docker и Docker Compose установлен.
2. Создаем директорию проекта и переходим в директорию с backend:
    ```bash
    cd backend
    ```
3. Меняем в docker-compose.yml:
   1) В backend: environment: DATABASE_URL на свои данные
   2) В frontend: context: на ../<your_directory_withfront>

4. Запускаем Docker Compose командой
    ```bash
    docker-compose up --build
    ```

## Структура проекта

- `main.py`: Основной файл приложения FastAPI.
- `db.py`: Настройки подключения к базе данных и создание сессий.
- `models.py`: Описание моделей базы данных.
- `schemas.py`: Описание схем данных Pydantic.

## Эндпоинты
- `GET /vacancies/`: Получение всех вакансий из базы данных.

## Остановка приложения
При остановке контейнеров Docker, данные в базе данных будут автоматически очищены.
