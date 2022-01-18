import pymongo
from bson.json_util import dumps, loads
from password import password

client = pymongo.MongoClient(f"mongodb+srv://capstone_db:{password}@cluster0.ed7en.mongodb.net/listings_db?retryWrites=true&w=majority")
def getjson():
    db = client.listings_db
    curs = db.rentals_table.find()

    list_cur = list(curs)
    
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2).replace("\n","")
    return json_data
