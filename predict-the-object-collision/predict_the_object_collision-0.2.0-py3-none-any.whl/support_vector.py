#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:21:33 2022

@author: smn06
"""

from predict_collision.visualize import *
#function for making the prediction and visualization
def Support_Vector_Classifier(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.svm import SVC
    svc = SVC(kernel = 'sigmoid', C = 0.025, random_state=100, probability=True)
    svc.fit(X_train,y_train)
    svc_score = svc.score (X_test, y_test)
    print("svc = ", svc_score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = svc.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(svc, cm, "Support Vector Classification ", X_train, X_test, y_train, y_test)
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    svc_report = classification_report(y_test, y_test_pred, output_dict=True)
    svc_macro_precision =  svc_report['macro avg']['precision']
    svc_macro_recall = svc_report['macro avg']['recall']
    svc_macro_f1 = svc_report['macro avg']['f1-score']
    svc_accuracy = svc_report['accuracy']
    print("Support Vector Classifier Accuracy = ", round(svc_accuracy,3))
    print("Support Vector Classifier Macro Precision = ", round(svc_macro_precision,3))
    print("Support Vector Classifier Macro Recall = ", round(svc_macro_recall,3))
    print("Support Vector Classifier Macro F1 = ", round(svc_macro_f1,3))