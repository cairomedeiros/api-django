from pymongo import MongoClient
from . import settings

class MongoConnection(object):

    def get_db_handle(db_name):
        client = MongoClient(
                            port=int("27017"),
                            username=settings.MONGODB_USERNAME,
                            password=settings.MONGODB_PASSWORD
                            )
        db_handle = client[db_name]
        return db_handle, client


    def get_collection_handle(db_handle, collection_name):
        return db_handle[collection_name]