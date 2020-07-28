from pymongo import MongoClient
from bson import ObjectId

connection = MongoClient() # connect to mongodb

new_database = connection.get_database('D4E15') # create / get database
quiz_database = connection.get_database('quiz')

result_collection = quiz_database.get_collection('result')
new_collection = new_database.get_collection('students') # create / get collection
quiz_collection = quiz_database.get_collection('quizzes')

# new_collection.insert_one({'name': 'first data'}) # write document to collection
result_found = result_collection.find({'name': {'$ne': 'Đức'} })
print(list(result_found))

quiz_collection.update_one(
    {'_id': ObjectId("5f202aad945100442014fc50")},  # query
    {
        '$push': {'choices': "7"} # push, set, unset
    } # update
)

result_collection.delete_one(
    {
        'correct_percent': 100 
    }
) # Delete