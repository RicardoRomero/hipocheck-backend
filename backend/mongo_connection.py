from mongoengine import connect

def mongo_connect():
    connect(
        db="mortgage_db",
        host="localhost",
        port=27017
    )