import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def get_db_connection():
    print("DB_HOST:", os.getenv("DB_HOST"))
    print("DB_USER:", os.getenv("DB_USER"))
    print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
    print("DB_NAME:", os.getenv("DB_NAME"))

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=3306
    )
