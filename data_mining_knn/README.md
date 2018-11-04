# Income prediction using kNN algorithm (Python)


**Description**
- Implementation of the k-Nearest Neighbour (denoted k-NN) algorithm on a sub-sample of the Adult / Census Income data. The model is to predict if a person earns more than 50k (see "earns" attribute). A description of the attributes can be found from the UCI data repository https://archive.ics.uci.edu/ml/datasets/adult.

The results are being printed to a grid.results.txt



**preprocessing**
- Load the data (csv) into a Pandas DataFrame
- Clean the training and testing datasets by removing invalid and duplicate data points
- Normalize dataset to give equal weight to each feature
- Split data into training/testing features and training/testing labels
- One hot encode categorical columns

**classification**
- implementation of kNN algorithm in Python: build a k-NN model on the training dataset and evaluate several performance measures on the test dataset
- compute the confusion matrix and classification performances: precision, sensitivity (recall), and specificity with respect to the class <=50K

**Task**
- Implement the k-Nearest Neighbour (kNN) algorithm on a sub-sample of the Adult / Census Income data. The model is to predict if a person earns more than 50k (see "earns" attribute). A description of the attributes can be found from the UCI data repository https://archive.ics.uci.edu/ml/datasets/adult. Note that the training dataset has a new column called "fold" which indicates the 5 folds that you must use in the 5-Cross Validation (denoted 5CV) for model optimisation. This is an auxiliary column and should not be used as a predictor, but just to indicate the fold. Your code should find the parameter value for k from a grid of values [1, 3, 5, 7, ..., 35, 37, 39] that maximises the accuracy of the 5CV.

Regarding parameter optimisation, your code will save in a file called grid.results.txt a table with 2 columns showing each value of k and the accuracy of the 5CV for that value of k. Of course the code will display the best k and accuracy.

With the best value k found above, your code has to build a k-NN model on the training dataset and evaluate several performance measures on the test dataset: confusion matrix, precision, sensitivity (recall), and specificity with respect to the class <=50K.
