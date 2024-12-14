from pymongo import MongoClient

class MongoDB:    
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.find_one(query)
        return result

    def find_all(self, collection_name, query):
        collection = self.db[collection_name]
        results = collection.find(query)
        return list(results)

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        result = collection.update_one(query, {'$set': update})
        return result.modified_count

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count


# def check() -> None:
#     print("Database is working!")

# check()
# x = MongoDB("mongodb+srv://shimulsutradhar814:8GdKJHmXjAiwadvv@cluster0.g81ls.mongodb.net/", "gamestore")
# x.insert_one("users", {"name": "sc", "email": "sc@gmail.com"})
# print(x.find_all("users", {}))