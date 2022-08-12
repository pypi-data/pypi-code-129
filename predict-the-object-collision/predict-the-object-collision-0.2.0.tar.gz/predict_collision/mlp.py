#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:07:51 2022

@author: smn06
"""

from predict_collision.visualize import *

#function for making the prediction and visualization
def mlp(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.neural_network import MLPClassifier
    mlp = MLPClassifier(random_state=45, max_iter=3000, learning_rate= 'adaptive' ).fit(X_train, y_train)
    mlp_score = mlp.score(X_test, y_test)
    print("MLP = ", mlp_score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = mlp.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(mlp, cm, "Multi-Layer Perceptron", X_train, X_test, y_train, y_test)
    
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    mlp_report = classification_report(y_test, y_test_pred, output_dict=True)
    mlp_macro_precision = mlp_report['macro avg']['precision']
    mlp_macro_recall = mlp_report['macro avg']['recall']
    mlp_macro_f1 = mlp_report['macro avg']['f1-score']
    mlp_accuracy = mlp_report['accuracy']
    print("Multi Layer Perceptron Accuracy = ", round(mlp_accuracy,3))
    print("Multi Layer Perceptron Macro Precision = ", round(mlp_macro_precision,3))
    print("Multi Layer Perceptron Macro Recall = ", round(mlp_macro_recall,3))
    print("Multi Layer Perceptron Macro F1 = ", round(mlp_macro_f1,3))
    