import pyexcel
from pymongo import MongoClient

connection = MongoClient()

quiz_database = connection.get_database('quiz')

quiz_collection = quiz_database.get_collection('quizzes')

records = pyexcel.get_records(file_name='quizzes.xlsx')

list_data = []
for record in records:
    record['choices'] = record['choices'].split(',')
    list_data.append(record)

quiz_collection.insert_many(list_data)
