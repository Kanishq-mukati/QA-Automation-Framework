import os

API_BASE_URL = os.getenv("API_BASE_URL", "")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "testdb"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres")
}

UI_BASE_URL = os.getenv("UI_BASE_URL", "")
TEST_TIMEOUT = int(os.getenv("TEST_TIMEOUT", "60"))

