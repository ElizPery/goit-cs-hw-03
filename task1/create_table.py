import psycopg2
from dotenv import load_dotenv
import os

# Configuration of data base connection
load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

db_config = {
    'dbname': DB_NAME,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'port': DB_PORT,
    'host': DB_HOST
}

# SQL requests to create tables
create_tables_commands = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        CONSTRAINT persons_email_un UNIQUE KEY (email)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
        CONSTRAINT task_name_un UNIQUE KEY (name)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (status_id) REFERENCES status(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
        FOREIGN KEY (user_id) REFERENCES user(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
    """
]

def create_tables():
    conn = None
    try:
        # Connection with data base
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Create tables
        for command in create_tables_commands:
            cur.execute(command)

        conn.commit()

        # Close cursor and connection 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_tables()