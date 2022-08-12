#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:30:03 2022

@author: smn06
"""

from predict_collision.visualize import *
#function for making the prediction and visualization
def knn(X_train, X_test, y_train, y_test):
    #importing and fitting the model from sklearn
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors= 7, algorithm= 'kd_tree')
    knn.fit(X_train,y_train)
    knn_score = knn.score(X_test, y_test)
    print("KNN_score = ",knn_score)
    
    #importing confusion matrix from sklearn
    from sklearn.metrics import confusion_matrix
    y_test_pred = knn.predict(X_test)
    cm = confusion_matrix(y_test, y_test_pred)
    visualize(knn, cm, "K - Nearest Neighbors Classifier ", X_train, X_test, y_train, y_test)
    
    
    # saving the classification report values for comparison at last
    from sklearn.metrics import classification_report
    knn_report = classification_report(y_test, y_test_pred, output_dict=True)
    knn_macro_precision =  knn_report['macro avg']['precision']
    knn_macro_recall = knn_report['macro avg']['recall']
    knn_macro_f1 = knn_report['macro avg']['f1-score']
    knn_accuracy = knn_report['accuracy']
    knn_accuracy = knn_report['accuracy']
    print("KNN Accuracy = ", round(knn_accuracy,3))
    print("KNN Macro Precision = ", round(knn_macro_precision,3))
    print("KNN Macro Recall = ", round(knn_macro_recall,3))
    print("KNN Macro F1 = ", round(knn_macro_f1,3))