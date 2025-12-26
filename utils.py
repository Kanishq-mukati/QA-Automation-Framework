import psycopg2
from config.settings import DB_CONFIG


def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        return conn
    except Exception as e:
        raise ConnectionError(f"Failed to connect to database: {str(e)}")

