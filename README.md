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

"""Mini-Document-Store/
├── main.py # FastAPI приложение
├── models.py # SQLAlchemy модели
├── crud.py # Функции работы с базой
├── schemas.py # Pydantic-схемы
├── database.py # Настройка базы данных
├── ai.py # Фейковая функция AI-анализ
├── storage/ # Папка для сохранённых файлов
├── requirements.txt # Зависимости проекта
└── README.md # Этот файл"""




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
