from pymongo import MongoClient

connection = MongoClient() # connect to mongodb

new_database = connection.get_database('D4E15') # create / get database

new_collection = new_database.get_collection('students') # create / get collection

new_collection.insert_one({'name': 'first data'}) # write document to collection