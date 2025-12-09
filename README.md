# Mini Document Store

**Mini Document Store** — это мини-сервис для хранения документов с версионированием, метаданными и базовым AI-анализом.

Реализован на **Python** с использованием **FastAPI**, **SQLAlchemy** и **SQLite**.

---

## Возможности

- Загрузка файлов (PDF, DOCX, PNG и др.)
- Автоматическая версияция файлов
- Хранение метаданных: имя, версия, размер, дата загрузки
- Базовый AI-анализ файлов (фейковая функция)
- Просмотр результатов анализа по каждому файлу
- API для получения списка файлов

---

## Структура проекта

pythonProject4/

├── main.py           # FastAPI приложение

├── models.py         # SQLAlchemy модели

├── crud.py           # Функции работы с базой

├── schemas.py        # Pydantic-схемы

├── database.py       # Настройка базы данных

├── ai.py             # Фейковая функция AI-анализ

├── storage/          # Папка для сохранённых файлов

├── requirements.txt  # Зависимости проекта

├── app.db            # База данных

└── README.md         # Этот файл


---

Как запустить проект
1. Клонировать репозиторий
git clone https://github.com/kudaibergendias/Mini-Document-Store.git
cd Mini-Document-Store

2. Создать виртуальное окружение
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

3. Установить зависимости
pip install -r requirements.txt

4. Запустить сервер FastAPI
uvicorn main:app --reload

5. Открыть документацию API

Swagger UI:

http://127.0.0.1:8000/docs


ReDoc:

http://127.0.0.1:8000/redoc

---
## API Основные маршруты

- **POST /files/upload** — загрузка файла  
- **GET /files** — список всех файлов  
- **POST /files/{file_id}/analyze** — провести AI-анализ файла  
- **GET /files/{file_id}/analysis** — получить результаты анализа  

---

## Технологии

- Python 3.10+
- FastAPI
- SQLAlchemy ORM
- SQLite / PostgreSQL
- Pydantic

---

## Автор

Проект создан **Dias Kudaibergen**
