# Team Airbnb (Capstone-Project)

## Segment 2 Presentation

### [Our Google presentation](https://docs.google.com/presentation/d/1T547BrGVOcnZ-Ra_A7yQJQpM_mZYjYGBYauYgHVS4ok/edit?usp=sharing)

#
## Team Members
1. Amy V. (Square)
1. Anna S. (Triangle)
1. Neeraj (Nick) J. (Circle)
1. Zoe F. (X)

---
## Purpose
Airbnb has grown tremendously over the past few years offering users a convenient way to find accommodations other than traditional hotels. For this project, we decided to investigate data about past Airbnb's available in NYC and see what has made them successful. We looked at price, location, and any key amenities that may help accommodations receive higher reviews and be more sought-after properties. We have set out to help future hosts in their Airbnb journeys to learn what will increase their chances of success while hosting an Airbnb. We were interested in Airbnb since it has become such a common or go to resource and have had personal positive experiences with it. 


---
## Source of Data (Description)
We sourced our data from a data mining article from the website [Medium](https://towardsdatascience.com/airbnb-rental-listings-dataset-mining-f972ed08ddec
) that explored the rental landscape in New York City. 


---
## GitHub
## Communication Protocols

We will meet a minimum of two times a week via Zoom to discuss progress, strategize next steps, and perform analysis. We will also have ad-hoc Zoom meetings as needed if someone requires additional assistance or encounters an issue.  Slack is our primary communication tool where we created a group chat to provide feedback and brainstorm.

---
## Proposed Machine Learning Model
Since out outcome is binary (whether or not the rental was successful), we propose to use logistic regression model for this project. Based on our outcomes we may implement other model(s) as needed.

Python File:
* [model_rework.ipynb](https://github.com/AValenti12/Capstone-Project/blob/main/Segment%202/ML_model/model_rework.ipynb)

Airbnb Listings Dataset Original vs. Clean

<img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/listings_csv_original.png?raw=true" width="200" height="100" >  <img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/clean_listings_csv.png?raw=true" width="200" height="100" >

Airbnb Listings Data Shape Original vs. Clean

<img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/data_shape_original.png?raw=true" width="190" height="100" >  <img src="https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/ML_model/df_shape_after.png?raw=true" width="110" height="100" >
> Before running any tests, the data was cleaned and paired down from the original dataset. A new column 'is_successful' was made based off of the 'review_scores_value' column and was added to the  dataframe. This will be our target for the model. If the airbnb had a score above a 5 we will consider it successful and label it as a 1. If the score value was less than or equal to 5 it will be labeled as a 0. The rest of the columns will be the features for this model that will predict whether the Airbnb listing will have successful reviews or not.

## Logistic Regression Model

![](https://github.com/AValenti12/Capstone-Project/blob/main/Segment%202/ML_model/model_images/Screen%20Shot%202022-01-09%20at%209.13.19%20PM.png?raw=true)
>  The columns that were not already numerical are given dummy variables to be able to be passed through the model. The data was then split into three sets: a training set and test set. 

![](https://github.com/AValenti12/Capstone-Project/blob/main/Segment%202/ML_model/model_images/Screen%20Shot%202022-01-09%20at%209.14.29%20PM.png?raw=true)
> The model is able to predict the outcome with about 80% accuracy.

![](https://github.com/AValenti12/Capstone-Project/blob/main/Segment%202/ML_model/model_images/Screen%20Shot%202022-01-09%20at%204.36.45%20PM.png?raw=true)
> This is a chart representing feature importance, after review we decided to remove the Superhost variable to avoid skewing results.

---

## Proposed Databases
We changed our strategy to use MongoDB instead of Postgress as we proposed earlier. Illustrated below is our [updated ERD](https://github.com/AValenti12/Capstone-Project/blob/main/Resources/QuickDBD-export.png). Although this ERD is not needed with MongoDB but still it is helpful to see all the collections with relevant columns in one place.

<img src="https://github.com/AValenti12/Capstone-Project/blob/main/Resources/QuickDBD-export.png?raw=true" width="900" height="400">

We have successfully created MongoDB database loaded up with relevant static data. Also, we have integrated this database with our mainstream data modeling. Here's a [snap shot](https://github.com/AValenti12/Capstone-Project/blob/main/Resources/Images/db_collections.png) of how our collections (four main collections) look like.

<img src="https://github.com/AValenti12/Capstone-Project/blob/main/Resources/Images/db_collections.png?raw=true" width="900" height="500">

We also [joined the two collections](https://github.com/AValenti12/Capstone-Project/blob/main/Resources/Images/Join.png) `(not Pandas joins)` and created a new collection out of it. "host_details_review" in the above illustration is the result of this aggregation activity.
<img src="https://github.com/AValenti12/Capstone-Project/blob/main/Resources/Images/Join.png?raw=true" width="900" height="500">

`We have hosted our MongoDB at remote site using AWS. Our data is accessible directly using the API.`

#
### Originally proposed Databases
We have setup a database in Postgres using the [schema](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/database/schema.sql) we created. We did not create any ERD since there's only one table to work with. We used cleaned real dataset to upload it in Postgres. We've [succesfully uploaded](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/record_count_postgress.png?raw=true) the [dataset](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/data%20uploaded_postgress.png) that we will be using throughout the project.

![](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/data%20uploaded_postgress.png?raw=true)

---

## Technology Used

We intend to use the following set of diversified **[technologies](https://github.com/AValenti12/Capstone-Project/blob/nj-new/ABNB%20-%20Segment%201/tech_used/tech.md)**.

![](https://github.com/AValenti12/Capstone-Project/blob/main/ABNB%20-%20Segment%201/images/technology_used.png?raw=true)

---

