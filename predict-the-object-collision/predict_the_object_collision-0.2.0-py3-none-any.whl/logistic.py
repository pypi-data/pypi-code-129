#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:02:15 2022

@author: smn06
"""

from predict_collision.visualize import *

#function for making the prediction and visualization
def logistic(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.linear_model import LogisticRegression
    logreg = LogisticRegression(solver='newton-cg', max_iter=1000)
    logreg.fit(X_train,y_train)
    score = logreg.score(X_test, y_test)
    print("Log Score = ", score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = logreg.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(logreg, cm, "Logistic Regression", X_train, X_test, y_train, y_test)
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    log_report = classification_report(y_test, y_test_pred, output_dict=True)
    log_macro_precision =  log_report['macro avg']['precision']
    log_macro_recall = log_report['macro avg']['recall']
    log_macro_f1 = log_report['macro avg']['f1-score']
    log_accuracy = log_report['accuracy']
    print("logistic Accuracy = ", round(log_accuracy,3))
    print("logistic Macro Precision = ", round(log_macro_precision,3))
    print("logistic Macro Recall = ", round(log_macro_recall,3))
    print("logistic Macro F1 = ", round(log_macro_f1,3))
    