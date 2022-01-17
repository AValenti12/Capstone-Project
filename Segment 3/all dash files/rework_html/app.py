from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo
import pandas as pd
from config import db_password
import model

#set up flask app
app = Flask(__name__)

# use flask_pymongo to set up mongo connection
CONNECTION_STRING = f"mongodb+srv://nickj:{db_password}@capstonecluster.7h9ij.mongodb.net/CapstoneCluster?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)

@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/about")
# def about():
#     return render_template('about.html')

# @app.route("/data")
# def data():
#     return render_template('/data.html',code=302)

# @app.route("/charts.html")
# def charts():
#     return render_template('/charts.html',code=302)

@app.route("/test")
def test():
    db = client.listings_db
    coll = db.result.find_one()
    return render_template('test.html', result=coll)

# @app.route("/team.html")
# def team():
#     return render_template('/team.html',code=302)

# @app.route('/',methods = ['GET'])
# def show_test():
#     return 

@app.route('/submit', methods = ['POST','GET'])
def submit():
    db = client.listings_db
    collection1 = db.X_set.find()
    collection2 = db.y_set.find()
    X = pd.DataFrame(collection1)
    y = pd.DataFrame(collection2)
    
    if request.method == 'POST':
        test = []
        t = request.form.getlist('arr[]')
        for i in t:
            test.append(float(i))
    d_result = model.logreg(X,y,test)
    collection3 = db.result
    collection3.insert(d_result)
    return redirect('/test',code=302)
    
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)