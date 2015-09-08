import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.reddit

stories = db.stories


def find():
    print 'find, reporting for duty'

    # options for case sensitive
    query = {'title': {'$regex': 'apple|google', '$options': 'i'}}
    projection = {'title': 1, '_id': 0}

    try:
        cursor = stories.find(query, projection)
    except Exception as e:
        print "error ", type(e), e

    for doc in cursor:
        print doc


find()