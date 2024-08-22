# Используем официальный Python 3.9 образ
FROM python:3.9-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Создаем и переходим в рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
