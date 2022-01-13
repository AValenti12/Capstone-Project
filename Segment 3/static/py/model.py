import pymongo
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from password import password

client = pymongo.MongoClient(f"mongodb+srv://capstone_db:{password}@cluster0.ed7en.mongodb.net/listings_db?retryWrites=true&w=majority")

def model():
    db = client.listings_db
    collection1 = db.train_X.find()
    collection2 = db.train_y.find()
    X = pd.DataFrame(collection1)
    y = pd.DataFrame(collection2)
    X = X.drop('_id',1)
    X = X[:15963]

    y_new = []
    for i in y['is_success'][0]:
        if i == 'yes':
            y_new.append(1)
        else:
            y_new.append(0)

    y = y_new

    #splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    X_train.shape

    # Creating a StandardScaler instance.
    scaler = StandardScaler()
    # Fitting the Standard Scaler with the training data.
    X_scaler = scaler.fit(X_train)

    # Scaling the data.
    X_train = X_scaler.transform(X_train)
    X_test = X_scaler.transform(X_test)

    #creating the model
    classifier = LogisticRegression(solver='lbfgs',
                                    max_iter=200,
                                    random_state=1)

    #fitting the model
    classifier.fit(X_train, y_train)

    #making predictions
    y_pred = classifier.predict(X_test)
    if y_pred == 1:
        result = "Success"
    else:
        result = "May need some work"
    return result

#accuracy of the model
# print(accuracy_score(y_test, y_pred))