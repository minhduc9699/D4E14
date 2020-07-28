import pyexcel
from pymongo import MongoClient

connection = MongoClient()

quiz_database = connection.get_database('quiz')

quiz_collection = quiz_database.get_collection('quizzes')

records = pyexcel.get_records(file_name='quizzes.xlsx')

for record in records:
    quiz_collection.insert_one({
        'question': record['question'],
        'choices': record['choices'].split(','),
        'right_choice': record['right_choice']
    })
