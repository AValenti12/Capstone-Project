import pymongo
import pandas as pd
import numpy as np
from collections import Counter
# from sklearn.metrics import accuracy_score
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def logreg(X,y,test):
    X = X.drop('_id',1)
    X['price'] = X['price'].div(100)
    X['amenities'] = X['amenities'].div(100)
    X['maximum_nights'] = X['maximum_nights'].div(100)
    y_new = []
    for i in y['is_success'][0]:
        if i == 'yes':
            y_new.append(1)
        else:
            y_new.append(0)

    y = y_new
    
    X['is_success']=y
    
    X = X.sort_values(by=['maximum_nights'],ascending=False)[3:]
    
    y = X['is_success']
    X = X.drop('is_success',1)

    d =  {'host_identity_verified': test[0],
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
    res = pd.DataFrame(d,index=[0])
#     #splitting the data
#     X_train, X_test, y_train, y_test = train_test_split(X, y)
#     X_train.shape

#     # Creating a StandardScaler instance.
#     scaler = StandardScaler()
#     # Fitting the Standard Scaler with the training data.
#     X_scaler = scaler.fit(X_train)

#     # Scaling the data.
#     X_train = X_scaler.transform(X_train)
#     X_test = X_scaler.transform(X_test)

#     #creating the model
#     classifier = LogisticRegression(solver='lbfgs',
#                                     max_iter=200,
#                                     random_state=1)

#     #fitting the model
#     classifier.fit(X_train, y_train)
    X_train, X_test, y_train, y_test = train_test_split(X,
    y,  test_size=0.1, random_state=0)

    transformer = RobustScaler().fit(X_train)


    # Scaling the data.
    X_train_scaled = transformer.transform(X_train)
    X_test_scaled = transformer.transform(X_test)
    res_scaled = transformer.transform(res)

    # Create a random forest classifier.
    rf_model = RandomForestClassifier(n_estimators=128, random_state=0) 

    # Fitting the model
    rf_model = rf_model.fit(X_train_scaled, y_train)

    
    #making predictions
    y_pred = rf_model.predict(res_scaled)

    def result(y_pred):
        if y_pred == 1:
            ans = "This rental should do well!"
            return ans
        else:
            ans = "Your rental may need some work..."
        return ans

    result = {'result':result(y_pred)}
    return result

if __name__ == "__main__":

    # If running as script, print scraped data
    print(logreg())    

#accuracy of the model
# print(accuracy_score(y_test, y_pred))