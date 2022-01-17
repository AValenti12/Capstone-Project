import pymongo
import pandas as pd
import numpy as np
from collections import Counter
# from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def logreg(X,y,test):
    X = X.drop('_id',1)

    y_new = []
    for i in y['is_success'][0]:
        if i == 'yes':
            y_new.append(1)
        else:
            y_new.append(0)

    y = y_new

    test =  {'host_identity_verified': test[0],
        'accommodates': test[1],                       
        'bathrooms': test[2],                        
        'bedrooms' : test[3],                      
        'beds' : test[4],                     
        'bed_type' :test[5],                     
        'amenities' : test[6],                    
        'price': test[7],                  
        'security_deposit' : test[8],                   
        'cleaning_fee' : test[9],                  
        'guests_included' : test[10],                 
        'extra_people' : test[11],                 
        'minimum_nights' : test[12],                
        'maximum_nights' : test[13],          
        'instant_bookable' : test[14],           
        'is_business_travel_ready' : test[15],        
        'cancellation_policy' : test[16],      
        'require_guest_profile_picture' : test[17],   
        'require_guest_phone_verification' : test[18],
        'neighbourhood' : test[19],                 
        'room' : test[20]}         
    res = pd.DataFrame(test,index=[0])
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
    y_pred = classifier.predict(res)

    def result(y_pred):
        if y_pred == 1:
            ans = "This rental should do well!"
            return ans
        else:
            ans = "Your rental may need some work"
        return ans

    result = {'result':result(y_pred)}
    return result

if __name__ == "__main__":

    # If running as script, print scraped data
    print(logreg())    

#accuracy of the model
# print(accuracy_score(y_test, y_pred))