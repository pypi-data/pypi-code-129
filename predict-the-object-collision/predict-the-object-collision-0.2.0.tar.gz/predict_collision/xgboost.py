#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:35:42 2022

@author: smn06
"""

from predict_collision.visualize import *
#function for making the prediction and visualization
def xgb(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    import xgboost as xgb
    model = xgb.XGBClassifier(objective="binary:logistic", random_state=42)
    xgb.fit(X_train,y_train)
    xgb_score = sgd.score (X_test, y_test)
    print("XGBoost =",xgb_score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = xgb.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(xgb, cm, "XGBoost Classifier ", X_train, X_test, y_train, y_test)
    
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    xgb_report = classification_report(y_test, y_test_pred, output_dict=True)
    xgb_macro_precision =  xgb_report['macro avg']['precision']
    xgb_macro_recall = xgb_report['macro avg']['recall']
    xgb_macro_f1 = xgb_report['macro avg']['f1-score']
    xgb_accuracy = xgb_report['accuracy']
    print("XGBoost Accuracy = ", round(xgb_accuracy,3))
    print("XGBoost Macro Precision = ", round(xgb_macro_precision,3))
    print("XGBoost Macro Recall = ", round(xgb_macro_recall,3))
    print("XGBoost Macro F1 = ", round(xgb_macro_f1,3))