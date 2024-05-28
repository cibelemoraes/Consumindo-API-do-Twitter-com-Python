from pymongo import MongoClient

cliente = MongoClient("mongodb://dio:dio@localhost:27017/")
#criando documento no pymongo
db = client.my_test

tweets_collection = db.trends