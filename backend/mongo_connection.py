from mongoengine import connect

def mongo_connect():
    connect(
        db="mortgage_db_two",
        host="localhost",
        port=27017
    )