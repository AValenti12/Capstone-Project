import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://capstone_db:U7N9pdZcUN-9FJ@cluster0.ed7en.mongodb.net/listings_db?retryWrites=true&w=majority")
def t():
    db = client.listings_db
    collection = db.rentals_table

    t = collection.find()

    table = pd.DataFrame(t)

    some = table[:1000].drop('_id',1)

    return some.to_html('t.html')

