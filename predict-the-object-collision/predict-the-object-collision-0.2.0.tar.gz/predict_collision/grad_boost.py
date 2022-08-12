#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:30:52 2022

@author: smn06
"""

from predict_collision.visualize import *
#function for making the prediction and visualization
def grad_boost(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.ensemble import GradientBoostingClassifier
    grad = GradientBoostingClassifier(loss='log_loss', n_estimators=150, learning_rate=0.0005, max_depth=1, random_state=45).fit(X_train, y_train)
    grad_score = grad.score(X_test, y_test)
    print("grad_score = ",grad_score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = grad.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(grad, cm, "Gradient Boosting Classifier ", X_train, X_test, y_train, y_test)
    
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    gbc_report = classification_report(y_test, y_test_pred, output_dict=True)
    gbc_macro_precision =  gbc_report['macro avg']['precision']
    gbc_macro_recall = gbc_report['macro avg']['recall']
    gbc_macro_f1 = gbc_report['macro avg']['f1-score']
    gbc_accuracy = gbc_report['accuracy']
    print("Gradient Boosting Accuracy = ", round(gbc_accuracy,3))
    print("Gradient Boosting Macro Precision = ", round(gbc_macro_precision,3))
    print("Gradient Boosting Macro Recall = ", round(gbc_macro_recall,3))
    print("Gradient Boosting Macro F1 = ", round(gbc_macro_f1,3))
