import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
import math
from statistics import mode

def predict(X_train, y_train, X_test, k):
    """
    Classify our data point as the majority class between K samples in the dataset having minimum distance to the sample
    Args:
        X_train: Training features as Pandas DataFrame
        y_train: Training labels as Pandas Series
        X_test: Testing features as Pandas DataFrame
        k: the number of nearest neighbours considered for classification
    Returns:
        mostCommon: Predicted label for our data point (0 or 1)
    """
    distances = [0] * len(X_train) # to store Euclidean distances
    labels = [0] * k # to store k nearest neighbours associated labels
    df_train = X_train.values
    # Go through each item in my training dataset, and calculate the distance from that data item to my specific sample
    for i in range(len(X_train)):
        # compute Euclidean distance
        # With a numpy array we can eliminate the nested for loops by inserting a new singleton dimension 
        # and broadcasting the subtraction over it. The rest we can also do using vectorized operations:
        distance = np.sqrt(((X_test- df_train[i, :, None].T) ** 2).sum(1))
        # add it to list of Euclidean distances (distance, index pairs)
        distances[i] = [distance, i]

    # sort the list by distance, in increasing order.
    distances = sorted(distances)

    # take the first k distances from this sorted list
    for i in range(k):
        # Find those k-points (by index) corresponding to these k-distances
        index = distances[i][1]
        # look up the associated label (value in 'earns' column), add it to list of labels
        labels[i] = y_train[index]
    # get majority label (Calculate the mode and return that value)    
    mostCommon = mode(labels)
    # return the most common label (most common value for 'earns' for k nearest neighbour: 0 or 1)
    return mostCommon

def kNN(X_train, y_train, X_test, predictions, k):
    """
    Make a prediction for every data point in the test dataset
    Store them in a list (predictions)
    Args:
        X_train: Training features as Pandas DataFrame
        y_train: Training labels as Pandas Series
        predictions: list to store predicted labels
        k: the number of nearest neighbours considered for classification
    """
    # loop over all test instances
    for i in range(len(X_test)):
        # make a prediction and add it to the list of predictions
        predictions.append(predict(X_train, y_train, X_test.values[i, :], k))
    
def getAccuracy(y_test, predictions):
    """
    Evaluate the accuracy of our model’s predictions
    Args:
        y_test: Test labels as Pandas Series
        predictions: Predicted labels as Python list
    Returns:
        The classification accuracy (%)
    """
    # calculate accuracy using numpy.sum
    accuracy = ((np.sum(y_test == predictions))/float(len(y_test))) * 100
    return accuracy

def confMatrix(y_test, predictions):
    """
    Compute confusion matrix to evaluate the accuracy of a classification
    Args:
        y_test: Test labels as Pandas Series
        predictions: Predicted labels as Python list
    Returns:
        The confusion matrix
    """
    labels = np.array(['>50k', '<=50k'])
    # calculate the confusion matrix; labels is numpy array of classification labels
    cm = np.zeros((len(labels), len(labels)))
    for a, p in zip(y_test, predictions):
        cm[p][a] += 1
    return cm

