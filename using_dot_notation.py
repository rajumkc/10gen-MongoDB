import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the reddit database
db=connection.reddit
stories = db.stories

def find():
	print "find, reporting for duty"

	query = {'media.oembed.type':'video'}
	projection = {'media.oembed.url':True, '_id':False}

	try:
		cursor = stories.find(query, projection)

	except:
		print "Unexpected error:", sys.exc_info()[0]

	sanity = 0
	for doc in cursor:
		print doc
		sanity += 1
		if (sanity > 10):
			break

find()