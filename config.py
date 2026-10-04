import os

# Получаем абсолютный путь к папке, где лежит config.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Собираем полный путь к базе данных
DB_PATH = os.path.join(BASE_DIR, "databases", "db_variant_1.db")
