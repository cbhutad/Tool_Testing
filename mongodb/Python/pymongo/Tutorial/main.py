"""

Script for the tutorial mentioned on pymongo official site.

"""

# Import the MongoClient
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime, pprint

# Connecting to mongod instance
client = MongoClient("localhost", 27017)

# Getting a database
db = client["test"]

# Getting a collection
collection = db["blog"]
# List of collections in given database
colls = db.list_collection_names()

# CRUD operations

# Insert
post = { "author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.now(),}
posts = db["posts"]
post_id = posts.insert_one(post).inserted_id

# Read
# Querying with a key as filter
pprint.pprint(posts.find_one({"author": "Mike"}))
# Querying with _id as filter. Here the value passed must be of type ObjectId, string representation for the same is not accepted.
string_id = str(post_id)
pprint.pprint(posts.find_one({"_id": ObjectId(string_id)}))
# Querying for a list of documents. We can also pass the filters to find the matching documents.
for post in posts.find():
    pprint.pprint(post)
# Counting the size of documents returned by a query
posts.count_documents({})
