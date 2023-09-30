from pymongo import MongoClient

def create_client():
    return MongoClient("localhost", 27017)

def database(client, dbname):
    return client[f"{dbname}"]

def collection(dbname, collection):
    return dbname[f"{collection}"]
