#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:51:14 2022

@author: smn06
"""
"""function for visualize the result, first parameter is the model, second parameter is the 
confusion matrix, third parameter is the name of model and from the fourth to seventh are the values"""


def visualize(bayes, cm, strr, X_train, X_test, y_train, y_test):

  import seaborn as sns
  import numpy as np
  import matplotlib.pyplot as plt

  t = "Confusion Matrix for {}".format(strr)
  names = ['True Neg','False Pos','False Neg','True Pos']
  val_count = ["{0:0.0f}".format(value) for value in cm.flatten()]
  percentages = ["{0:.2%}".format(value) for value in cm.flatten()/np.sum(cm)]
  labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(names,val_count,percentages)]
  labels = np.asarray(labels).reshape(2,2)
  ax = sns.heatmap(cm, annot=labels, fmt='', cmap='OrRd')
  ax.set_title(t)
  ax.set_xlabel('\nPredicted Values')
  ax.set_ylabel('Actual Values ')

  # Ticket labels - List must be in alphabetical order
  ax.xaxis.set_ticklabels(['False','True'])
  ax.yaxis.set_ticklabels(['False','True'])

  # Display the visualization of the Confusion Matrix.
  plt.show()

  from yellowbrick.classifier import ClassificationReport

  classes = ["False","True"]
  # Instantiate the classification model and visualizer
  visualizer = ClassificationReport(bayes, classes=classes, support=True)
  visualizer.fit(X_train, y_train)  # Fit the visualizer and the model
  visualizer.score(X_test, y_test)  # Evaluate the model on the test data
  visualizer.show()
