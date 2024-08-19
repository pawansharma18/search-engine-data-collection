import pymongo
import os


class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["DATABASE_NAME"]) -> None:
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(
                f"mongodb://pa1sharma1802:pawan1802@project-shard-00-00.w3ujp.mongodb.net:27017,project-shard-00-01.w3ujp.mongodb.net:27017,project-shard-00-02.w3ujp.mongodb.net:27017/?replicaSet=atlas-sjdra9-shard-0&ssl=true&authSource=admin"
            )
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
