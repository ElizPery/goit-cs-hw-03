from faker import Faker
import psycopg2
import random
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

fake = Faker() 

# Functions to generate data
def generate_users(n=10):
    # Generate random data for users table
        users = []

        for num in n:
            fullname = fake.name()
            email = fake.email()
            users.append((num, fullname, email,))

        return users

def generate_statuses():
    # Generate statuses for status table
        statuses = [(1, "new",), (2, "in progress",), (3, "completed",)]
        return statuses

def generate_tasks(n=30):
    # Generate random data for tasks table
        tasks = []

        for _ in n:
            title = fake.text(100)
            description = fake.text(200)
            status_id = random.randint(1, 3)
            user_id = random.randint(1, 10)
            tasks.append((title, description, status_id, user_id,))

        return tasks

# Function to fill the data base
def populate_database():
    conn = None
    try:
        # Connection with data base
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Insert users 
        users = generate_users()
        cur.executemany("INSERT INTO users (id, fullname, email) VALUES (%s, %s, %s)", users)

        # Insert statuses
        statuses = generate_statuses()
        cur.executemany("INSERT INTO status (id, name) VALUES (%s, %s)", statuses)

        # Insert tasks 
        tasks = generate_tasks()
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        conn.commit()

        # Close cursor and connection 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    populate_database()