import pymongo
from bson.json_util import dumps, loads

client = pymongo.MongoClient("mongodb+srv://capstone_db:U7N9pdZcUN-9FJ@cluster0.ed7en.mongodb.net/listings_db?retryWrites=true&w=majority")
def getjson():
    db = client.listings_db
    curs = db.rentals_table.find()

    list_cur = list(curs)
    
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2).replace("\n","")
    return json_data
