from flask import Flask, render_template, request, redirect, url_for
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
    return render_template('test.html')

# @app.route("/team.html")
# def team():
#     return render_template('/team.html',code=302)

# @app.route('/',methods = ['GET'])
# def show_test():
#     return 

@app.route('/submit', methods = ['POST','GET'])
def get_data_from_html():
    test = ':..........('
    if request.method == 'POST':
        test.append(request.POST('idRadio'))
        # test.append(request.POST.get('accoInput'))
        # test.append(request.POST.get('bathInput'))
        # test.append(request.POST.get('bedroomInput'))
        # test.append(request.POST.get('bedInput'))
        # test.append(request.POST.get('bedRadio'))
        # test.append(request.POST.get('amenitInput'))
        # test.append(request.POST.get('priceInput'))
        # test.append(request.POST.get('depositInput'))
        # test.append(request.POST.get('cleanInput'))
        # test.append(request.POST.get('guestInput'))
        # test.append(request.POST.get('extraInput'))
        # test.append(request.POST.get('minInput'))
        # test.append(request.POST.get('maxInput'))
        # test.append(request.POST.get('instantRadio'))
        # test.append(request.POST.get('busInput'))
        # test.append(request.POST.get('cancelRadio'))
        # test.append(request.POST.get('picRadio'))
        # test.append(request.POST.get('phoneRadio'))
        # test.append(request.POST.get('placeRadio'))
        # test.append(request.POST.get('roomRadio'))
        # db = client.listings_db
        # collection1 = db.X_set.find()
        # collection2 = db.y_set.find()
        # X = pd.DataFrame(collection1)
        # y = pd.DataFrame(collection2)
        #result = model(X,y,test)
    print(test)
    return render_template("submit.html", test=test) #result

if __name__ == '__main__':
    app.run(port=5000, debug=True)
