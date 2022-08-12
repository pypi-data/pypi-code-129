#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:10:25 2022

@author: smn06
"""


from predict_collision.visualize import *
#function for making the prediction and visualization
def sgd(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.linear_model import SGDClassifier
    sgd = SGDClassifier(loss="log_loss", eta0=1, learning_rate="adaptive", penalty=None)
    sgd.fit(X_train,y_train)
    sgd_score = sgd.score (X_test, y_test)
    print("SGD =",sgd_score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = sgd.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(sgd, cm, "SGD Classifier ", X_train, X_test, y_train, y_test)
    
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    sgd_report = classification_report(y_test, y_test_pred, output_dict=True)
    sgd_macro_precision =  sgd_report['macro avg']['precision']
    sgd_macro_recall = sgd_report['macro avg']['recall']
    sgd_macro_f1 = sgd_report['macro avg']['f1-score']
    sgd_accuracy = sgd_report['accuracy']
    print("Stochastic Gradient Descent Accuracy = ", round(sgd_accuracy,3))
    print("Stochastic Gradient Descent Macro Precision = ", round(sgd_macro_precision,3))
    print("Stochastic Gradient Descent Macro Recall = ", round(sgd_macro_recall,3))
    print("Stochastic Gradient Descent Macro F1 = ", round(sgd_macro_f1,3))