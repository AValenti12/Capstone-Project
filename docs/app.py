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

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/data")
def data():
    return render_template('data.html')

@app.route("/charts")
def charts():
    return render_template('charts.html')

@app.route("/test")
def test():
    return render_template('test.html')

@app.route('/submit')
def submit():
    db = client.listings_db
    curs = db.result.find()
    ans = list(curs)[-1]
    res = ans['result']
    print(res)
    return render_template('submit.html',result=res)

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        test = request.form.getlist('arr[]')
        db = client.listings_db
        collection1 = db.X_set.find()
        collection2 = db.y_set.find()
        X = pd.DataFrame(collection1)
        y = pd.DataFrame(collection2)
        ans = model.logreg(X,y,test)
        db.result.insert_one(ans)
    return redirect('/submit', code=302)

@app.route("/team")
def team():
    return render_template('team.html')
    
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)