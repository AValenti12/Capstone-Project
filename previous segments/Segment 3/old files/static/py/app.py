from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from password import password
import model

#set up flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "capstonecluster-shard-00-01.7h9ij.mongodb.net:27017"
mongo = PyMongo(app)

@app.route("/")
def test():
   db = mongo.listings_db
    collection1 = db.X.find()
    collection2 = db.y.find()
   return render_template("test.html", db=db )

@app.route("/submit")
def pred():
    X = pd.DataFrame(collection1)
    y = pd.DataFrame(collection2)
   result = model.model()
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()