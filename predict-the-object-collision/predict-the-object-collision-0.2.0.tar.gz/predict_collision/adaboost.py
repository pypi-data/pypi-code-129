#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:42:27 2022

@author: smn06
"""
from predict_collision.visualize import *

def adaboost(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.ensemble import AdaBoostClassifier
    ada = AdaBoostClassifier(n_estimators=100, random_state=0)
    ada.fit(X_train,y_train)
    score = ada.score(X_test, y_test)
    print("Adaboost Score = ", score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = ada.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(ada,cm, "adaboost", X_train, X_test, y_train, y_test)
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    ada_report = classification_report(y_test, y_test_pred, output_dict=True)
    ada_macro_precision =  ada_report['macro avg']['precision']
    ada_macro_recall = ada_report['macro avg']['recall']
    ada_macro_f1 = ada_report['macro avg']['f1-score']
    ada_accuracy = ada_report['accuracy']
    print("Adaboost Accuracy = ", round(ada_accuracy,3))
    print("Adaboost Macro Precision = ", round(ada_macro_precision,3))
    print("Adaboost Macro Recall = ", round(ada_macro_recall,3))
    print("Adaboost Macro F1 = ", round(ada_macro_f1,3))
    