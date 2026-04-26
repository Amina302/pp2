import psycopg2
import config


def create_connection():
    conn = psycopg2.connect(
        host=config.HOST,
        database=config.DB_NAME,
        user=config.USER,
        password=config.PASSWORD,
        port=config.PORT
    )
    return conn