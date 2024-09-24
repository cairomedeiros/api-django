from pymongo import MongoClient

class MongoConnection(object):

    def get_db_handle(db_name):
        client = MongoClient(
                            port=int("27017"),
                            username="root",
                            password="root"
                            )
        db_handle = client[db_name]
        return db_handle, client


    def get_collection_handle(db_handle, collection_name):
        return db_handle[collection_name]