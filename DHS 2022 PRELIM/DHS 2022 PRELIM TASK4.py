#Task 4.1
import pymongo
import json
client = pymongo.MongoClient("localhost", 27017)
client.drop_database("applicants")
db = client["applicants"]
coll = db["contingents"]
with open("contingents.json") as f:
    coll.insert_many(json.load(f))

x = coll.find()
for document in x:
    print(document)

print()

#Task 4.2
x = coll.find({'$and' : [{'height' : {'$gte' : 1.5}}, {'medical_history' : {'$nin' : ['heart issues']}}]})

for document in x:
    objID = document['_id']
    coll.update_one({'_id' : objID}, {'$set' : {'suitability' : 'High'}})

x = coll.find()
for document in x:
    print(document)
