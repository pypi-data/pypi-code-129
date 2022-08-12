#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:14:05 2022

@author: smn06
"""

from predict_collision.visualize import *
#function for making the prediction and visualization
def perceptron(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.linear_model import Perceptron
    per = Perceptron(alpha=0.0001, l1_ratio=0.15, fit_intercept=True, max_iter=10000, tol=0.001, shuffle=True, verbose=0, eta0=1.0, random_state=0)
    per.fit(X_train,y_train)
    per_score = per.score(X_test, y_test)
    print("Perceptron = ",per_score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = per.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(per, cm, "Linear Perceptron Classifier ", X_train, X_test, y_train, y_test)
    
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    per_report = classification_report(y_test, y_test_pred, output_dict=True)
    per_macro_precision =  per_report['macro avg']['precision']
    per_macro_recall = per_report['macro avg']['recall']
    per_macro_f1 = per_report['macro avg']['f1-score']
    per_accuracy = per_report['accuracy']
    print("perceptron Accuracy = ", round(per_accuracy,3))
    print("perceptron Macro Precision = ", round(per_macro_precision,3))
    print("perceptron Macro Recall = ", round(per_macro_recall,3))
    print("perceptron Macro F1 = ", round(per_macro_f1,3))
