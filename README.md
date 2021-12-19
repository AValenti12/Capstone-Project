# Team Airbnb (Capstone-Project)

## Team Members
1. Amy V. (Square)
1. Anna S. (Triangle)
1. Neeraj (Nick) J. (Circle)
1. Zoe F. (X)

#
## Purpose
Airbnb has grown tremendously over the past few years offering users a convenient way to find accommodations other than traditional hotels. For this project, we decided to investigate data about past Airbnb�s available in NYC and see what has made them successful. We looked at price, location, and any key amenities that may help accommodations receive higher reviews and be more sought-after properties. We have set out to help future hosts in their Airbnb journeys to learn what will increase their chances of success while hosting an Airbnb. We were interested in Airbnb since it has become such a common or go to resource and have had personal positive experiences with it. 


#
## Source of Data (Description)
We sourced our data from a data mining article from the website [Medium](https://towardsdatascience.com/airbnb-rental-listings-dataset-mining-f972ed08ddec
) that explored the rental landscape in New York City. 


#
## GitHub
## Communication Protocols

We will meet a minimum of two times a week via Zoom to discuss progress, strategize next steps, and perform analysis. We will aso have ad-hoc Zoom meetings as needed if someone requires additional assistance or encounters an issue.  Slack is our primary communication tool where we created a group chat to provide feedback and brainstorm.

#
## Proposed Machine Learning Model
Python Files:
* [simple_airbnb_ml_model.ipynb](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/ML_model/simple_airbnb_ml_model.ipynb)
* [simple_airbnb_ml_model.ipynb](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/ML_model/simple_airbnb_ml_model.ipynb)

Airbnb Listings Dataset Original vs. Clean

<img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/listings_csv_original.png?raw=true" width="200" height="100" >  <img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/clean_listings_csv.png?raw=true" width="200" height="100" >

Airbnb Listings Data Shape Original vs. Clean

<img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/data_shape_original.png?raw=true" width="190" height="100" >  <img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/df_shape_after.png?raw=true" width="110" height="100" >
> Before running any tests, the data was cleaned and paired down from the original dataset. A new column 'is_successful' was made based off of the 'review_scores_value' column and was added to the  dataframe. This will be our target for the model. If the airbnb had a score above a 5 we will consider it successful and label it as a 1. If the score value was less than or equal to 5 it will be labeled as a 0. The rest of the columns will be the features for this model that will predict whether the Airbnb listing will have successful reviews or not.

## Neural Network Model Mock Up
Input Data
![](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/split_data.png?raw=true)
>  The columns that were not already numerical are given dummy variables to be able to be passed through the model. The data was then split into three sets: a training set, test set, and validation set. 

Defining a Model
![](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/define_model.png?raw=true)
> Using `Keras`, a `Sequential` model was chosen with one input layer and two hidden layers. The activation functions chosen were the relu and sigmoid functions. This model was chosen because we have used it in class and past assignments. Since we are classifying the listings as either successful or not, we felt this would be a beneficial model to use.

Compiling the Model and Outputting a Label
![](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/compile_model.png?raw=true)
> To compile the model, since we are checking if the listing is successful or not, the `binary_crossentropy` loss function was chosen and the `adam` optimizer was chosen since that is most familiar at the time. The model is fit using the training and validation sets and the program prints out the predictions of the test set. 

Upcoming Challenge and Suggestions for Improvement
* As we can see, although this model seems to give a high accuracy per epoch, this can mean there may be some features of the model that are telling to this model, making it easier for the predictions to be made. This will have to be considered moving forward. 
* Since this is only a mock up of what we want the final model to resemble, there are a few things we can do to improve the model: 
    * Taking another look at our dataset/re-evaluate the features of the model (possibly remove more columns)
    * Changing the number of neurons in hidden layers
    * Changing the activation functions

---

## Proposed Databases
We have setup a database in Postgres using the [schema](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/database/schema.sql) we created. We did not create any ERD since there's only one table to work with. We used cleaned real dataset to upload it in Postgres. We've [succesfully uploaded](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/record_count_postgress.png?raw=true) the [dataset](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/data%20uploaded_postgress.png) that we will be using throughout the project.

![](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/data%20uploaded_postgress.png?raw=true)
