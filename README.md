# Админ-панель

Административаня панель для добавления фильмов, актеров и жанров. Данные в поисковый движок попадает только через админ-панель.  
Стек: Python, Django, Postgres, Docker, Nginx.

## Запуск
- Заполнить .env по примеру
- Запуск проекта с помощью docker: docker compose build && docker compose down && docker compose up -d

## Дополнительно
- Миграции: python manage.py migrate
- Статика: python manage.py collectstatic
