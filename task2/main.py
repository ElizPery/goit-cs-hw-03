from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

def db_init():
    load_dotenv()
    DB_NAME = os.getenv('DB_NAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    client = MongoClient(
        f"mongodb+srv://{DB_NAME}:{DB_PASSWORD}@cluster0.i6t6i.mongodb.net/",
        server_api=ServerApi('1')
    )

    db = client.book

    result_many = db.cats.insert_many(
        [
            {
                "name": "good",
                "age": 2,
                "features": ["goes to the tray", "does not allow itself to stroke", "grey"],
            },
            {
                "name": "barsik",
                "age": 4,
                "features": ["goes to the tray", "allow itself to stroke", "white"],
            },
            {
                "name": "cat",
                "age": 3,
                "features": ["goes to the tray", "allow itself to stroke", "black"],
            },
        ]
    )

    return db

def read_all_from_db(db):
    result = db.cats.find({})
    for el in result:
        print(el)

def read_from_db(db):
    name = input("Please enter name of the cat that you want to see >>> ").strip()
    try:
        result = db.cats.find_one({"name": name})  
        return result
    except:
        print("Something went wrong, please try again!")

def update_age_by_name(db):
    name = input("Please enter name of the cat that you want to update >>> ").strip()
    age = input("Please enter new age for this cat >>> ")
    try:
        db.cats.update_one({"name": name}, {"$set": {"age": int(age)}})
        result = db.cats.find_one({"name": name})
        return result
    except:
        print("Something went wrong, please try again!")

def update_features_by_name(db):
    name = input("Please enter name of the cat that you want to update >>> ").strip()
    feature = input("Please enter new feature for this cat >>> ")
    try:
        cat_features = db.cats.find_one({"name": name})["features"]
        cat_features.append(feature)
        db.cats.update_one({"name": name}, {"$set": {"features": cat_features}})
        result = db.cats.find_one({"name": name})
        return result
    except:
        print("Something went wrong, please try again!")

def delete_by_name(db):
    name = input("Please enter name of the cat that you want to delete >>> ").strip()
    try:
        db.cats.delete_one({"name": name})
        return "Delete successfully"
    except:
        print("Something went wrong, please try again!")

def delete_all(db):
    try:
        db.cats.delete_many({})
        return "Delete successfully"
    except:
        print("Something went wrong, please try again!")

def main():
    print("Hello! Possible commands: read_all, read, update_age, update_features, delete_all, delete, exit.")
    db = db_init()
    while True:
        command = input("Please enter you command >>> ").strip()
        if command == "exit":
            break
        elif command == "read_all":
            print(read_all_from_db(db))
        elif command == "read":
            print(read_from_db(db))
        elif command == "update_age":
            print(update_age_by_name(db))
        elif command == "update_features":
            print(update_features_by_name(db))
        elif command == "delete_all":
            print(delete_all(db))
        elif command == "delete":
            print(delete_by_name(db))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()