#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:15:01 2022

@author: smn06
"""
"""The goal of this project is to predict the collision of nearest objects around the mighty EARTH"""


#importing the models from the user defined modules
from predict_collision.adaboost import *
from predict_collision.logistic import *
from predict_collision.mlp import *
from predict_collision.sgd import *
from predict_collision.xgboost import *
from predict_collision.perceptron import *
from predict_collision.support_vector import *
from predict_collision.grad_boost import *
from predict_collision.knn import *
from predict_collision.random_forest import *
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import confusion_matrix

#At first, switch the computational power to GPU from CPU using CUDA
#import tensorflow as tf
#physical_devices = tf.config.list_physical_devices('GPU') 
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

#remove warnings from future and user
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)



"""The official dataset is from NASA's official website https://cneos.jpl.nasa.gov/ca/ .
 And the modified version of this dataset is available on Kaggle.
 Link : https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects . """
# After saving the CSV file we will read it using panda

#load dataset and reading
import pandas as pd

# str = "/home/mosfak/Desktop/Predict-the-Collision-and-Save-the-Earth-master/src/data/neo.csv"

# str = ""
def readd(str):
    

    datas = pd.read_csv("{}".format(str))
    return datas


#making a function where a passed specific value helps to run the model
def predict(X_train, X_test, y_train, y_test, a):

    # a = int(input("Enter the value : "))
    
    if a == 1:
        adaboost(X_train, X_test, y_train, y_test)
    
    elif a == 2:
        logistic(X_train, X_test, y_train, y_test)
    
    elif a == 3:
        mlp(X_train, X_test, y_train, y_test)
        
    elif a == 4:
        sgd(X_train, X_test, y_train, y_test)
        
    elif a == 5:
        perceptron(X_train, X_test, y_train, y_test)
        
    elif a == 6:
        Support_Vector_Classifier(X_train, X_test, y_train, y_test)

    elif a == 7:
        grad_boost(X_train, X_test, y_train, y_test)
        
    elif a == 8:
        xgb(X_train, X_test, y_train, y_test)

    elif a == 9:
        knn(X_train, X_test, y_train, y_test)

    elif a == 10:
        forest(X_train, X_test, y_train, y_test)

    else:
        print("Wrong Input. Run the Program Again")
        return
        
        
def main_fun(str,a):
    
    welcome = """Hurry!!!!, Predict the Collision from the Nearest Object around this world
          and Save the Earth.
          From the NASA's official data, this program is developed for doing the prediction. 
          Top 10 machine learning model is used to make the prediction with evaluation metrics
          such as Accuracy, Precision, Recall, F1-Score.
          All you have to do is just pressing a number range from 1 to 10. The values defines
          the model that have used in this program.
          
          Model Name --------------------------------Number have to press
          _______________________________________________________________
          Adaboost Classifier ---------------------------- 1
          Logistic Regression ---------------------------- 2
          Multi-Layer Perceptron ------------------------- 3
          Stochastic Gradient Descent -------------------- 4
          XGBoost Classifier ----------------------------- 5
          Linear Perceptron Classifier ------------------- 6
          Support Vector Classification ------------------ 7
          Gradient Boosting Classifier ------------------- 8
          K-Nearest Neighbors ---------------------------- 9
          Random Forest Classifier ----------------------- 10
          """
          
    # print(welcome)
    data = readd(str)
    #Exploring the labels and types.
    dc = data.copy()
    # print(dc.dtypes)

    #Checking is there any null value or not.
    # print(dc.isnull().sum())



    #From the dataset, we can see that "Sentry_Object" and "Hazardous" labels data are in Boolean form.
    #Where those are filled with 'True' and 'False'. We are going to encode them with 1 and 0
    features = list(dc.columns)
    features = [a for a in features if a in ('sentry_object','hazardous')]
    le=LabelEncoder()
    for f in features:
        dc[f]=le.fit_transform(dc[f])



    #We can also see from the dataset that data from some of the labels are higher than the others, 
    #this can lead to a high covariance. So, we are going to use minmax scaler in the following 
    #columns - 'relative_velocity', 'miss_distance', 'absolute_magnitude'. But first, 
    #we need to drop 'id','name','orbiting_body' because of irrelevency.
    dc.drop(['id','name','orbiting_body'], axis = 1, inplace = True)


    #importing minmax scaling from sklearn and scaling to desired features
    minmax = [ 'relative_velocity', 'miss_distance', 'absolute_magnitude']
    scaled_data = dc.copy()
    features = scaled_data[minmax]
    scaler = MinMaxScaler().fit(features.values)
    features = scaler.transform(features.values)
    scaled_data[minmax] = features

    #Now we are going to visualize the dataset using Autoviz. It can find the most 
    #important features and plot impactful visualizations for the dataset
    # from autoviz.AutoViz_Class import AutoViz_Class
    # AV = AutoViz_Class()
    # %matplotlib inline
    # target = 'hazardous'
    # dft = AV.AutoViz('',
    #                   ',',
    #                   target,
    #                   data_copy,
    #                   max_rows_analyzed=99999,
    #                   max_cols_analyzed=30
    #                   )

    #Now it's the time for getting the prediction result using classifier algorithms. 
    #But first, we need the train, test values.

    X = scaled_data.drop(['hazardous'], axis = 1)
    y = scaled_data.hazardous
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)


    
    predict(X_train, X_test, y_train, y_test, a )
    














