from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print("connected to mongodb ",client)
