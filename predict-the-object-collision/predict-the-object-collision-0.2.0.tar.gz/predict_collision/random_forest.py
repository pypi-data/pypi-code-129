#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:33:43 2022

@author: smn06
"""

from predict_collision.visualize import *
#function for making the prediction and visualization
def forest(X_train, X_test, y_train, y_test):
    from sklearn.ensemble import RandomForestClassifier
    rfm = RandomForestClassifier(criterion='log_loss', n_estimators= 100, oob_score= True, n_jobs = 1, random_state=100, max_features= 'sqrt', min_samples_leaf= 20)                    
    rfm.fit(X_train,y_train)
    rfm_score = rfm.score(X_test, y_test)
    print("RFC_score = ",rfm_score)
    from sklearn.metrics import confusion_matrix
    y_test_pred = rfm.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(rfm, cm, "Random Forest Classifier ", X_train, X_test, y_train, y_test)
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    rfc_report = classification_report(y_test, y_test_pred, output_dict=True)
    rfc_macro_precision =  rfc_report['macro avg']['precision']
    rfc_macro_recall = rfc_report['macro avg']['recall']
    rfc_macro_f1 = rfc_report['macro avg']['f1-score']
    rfc_accuracy = rfc_report['accuracy']
    print("Random Forest Accuracy = ", round(rfc_accuracy,3))
    print("Random Forest Macro Precision = ", round(rfc_macro_precision,3))
    print("Random Forest Macro Recall = ", round(rfc_macro_recall,3))
    print("Random Forest Macro F1 = ", round(rfc_macro_f1,3))