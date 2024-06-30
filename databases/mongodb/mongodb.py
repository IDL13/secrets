import pymongo

class MongoDB:
    def __init__(self, url: str, collection_name: str):
        self.db_client = pymongo.MongoClient(url)
        self.current_db = self.db_client["Secrets"]
        self.collection = self.current_db[collection_name]
        
    def add_secret(self, json: dict):
        status = self.collection.insert_one(json).inserted_id
        return status

    def get_secret(self,json: dict):
        status = self.collection.find_one(json)
        return status["secret"]

    def get_passphrase(self, json: dict):
        status = self.collection.find_one(json)
        return status["passphrase"]
        