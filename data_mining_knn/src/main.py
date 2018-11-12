from preprocess import *
from knn import *
import datetime

def preprocess_datasets():
    """
    Load, normalize and preprocess our datasets.
    Args:
        None
    Returns:
        X_train: Training features as Pandas DataFrame.
        y_train: Training labels as Pandas Series.
        X_test: Testing features as Pandas DataFrame.
        y_test: Testing labels as Pandas Series.
    """
    # load data
    train_data, test_data = loadData('data/adult.train.5fold.csv', 'data/adult.test.csv')
    # clean data
    train_clean, test_clean = cleanData(train_data, test_data)
    # drop insignificant predictors
    train_clean.drop('fnlwgt', axis=1, inplace=True)
    test_clean.drop('fnlwgt', axis=1, inplace=True)
    train_clean.drop('capital_gain', axis=1, inplace=True)
    test_clean.drop('capital_gain', axis=1, inplace=True)
    train_clean.drop('capital_loss', axis=1, inplace=True)
    test_clean.drop('capital_loss', axis=1, inplace=True)
    # normalize data
    normalized_train = normalize(train_clean)
    normalized_test = normalize(test_clean)

    # slice test dataframe - use first 5000 rows
    sliced_test = normalized_test[:5000]
    # split data
    X_train, y_train, X_test, y_test = split_data(normalized_train, sliced_test)
    # One hot encode categorical data
    X_train, y_train, X_test, y_test = ohe_data(X_train, y_train, X_test, y_test)

    return X_train, y_train, X_test, y_test

def printConfusionMatrix(k, accuracy, cm, file):
    """
    Print confusion matrix to txt file
    Args:
        k: the number of nearest neighbours considered for classification
        accuracy: the accuracy of our model’s predictions
        cm: the confusion matrix
        file: destination file (txt)
    """
    true_0_pred_0 = cm[0][0]
    true_0_pred_1 = cm[1][0]
    true_1_pred_0 = cm[0][1]
    true_1_pred_1 = cm[1][1]

    #sensitivity = recall
    class_precision0 = (true_0_pred_0/(true_0_pred_0+true_1_pred_0)) * 100
    class_precision1 = (true_1_pred_1/(true_1_pred_1+true_0_pred_1)) * 100
    class_recall0 = (true_0_pred_0/(true_0_pred_0+true_0_pred_1)) * 100 # Sensitivity
    class_recall1 = (true_1_pred_1/(true_1_pred_1+true_1_pred_0)) * 100 # Specificity

    print('=' * 70, file=file)
    print('\nValue of k: {}, accuracy: {:.2f}% \n'
    'confusion matrix: \n \t\t|  true <=50k \t|  true >50k \t|  class precision \n'
    'predicted <=50k\t|  {:.0f}\t\t|  {:.0f}\t\t|  {:.2f}%\n'
    'predicted >50k\t|  {:.0f}\t\t|  {:.0f}\t\t|  {:.2f}%\n'
    'class recall\t|  {:.2f}%\t|  {:.2f}%\n'
    .format(k, accuracy, cm[0][0], cm[0][1], class_precision0, cm[1][0], cm[1][1], 
    class_precision1, class_recall0, class_recall1), file=file)
    

def main():
    """
    Run main program
    """
    X_train, y_train, X_test, y_test = preprocess_datasets()
    # create txt to save results
    text_file = open("grid.results.txt", "w")
    # print the size of datasets to the text file
    print('Results \n\nTraining data size: {}\ntest data size: {}\n'.format(len(X_train), len(X_test)), file=text_file)
    # record start time
    start = datetime.datetime.now()
    print('started at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # run the program for each value of k between 1 and 39, odd numbers only
    for k in range(1, 40, 2):
        # record start time
        start = datetime.datetime.now()
        predictions = []
        # Train kNN algorithm on the census income dataset (adult.train) to predict whether income exceeds $50k per year
        kNN(X_train, y_train, X_test, predictions, k)
        # calculate accuracy
        accuracy = getAccuracy(y_test, predictions)
        # create confusion matrix
        cm = confMatrix(y_test, predictions)
        # print accuracy and confusion matrix to file
        #printConfusionMatrix(k, accuracy, cm, text_file)
        # Alternatively, if we just want to print the value of k and accuracy
        print('-' * 35, file=text_file)
        print(' Value of k: {}\t| accuracy: {:.2f}%'.format(k, accuracy), file=text_file)
        # calculate runtime (in seconds), convert it to hours, minutes and seconds
        total_runtime = (datetime.datetime.now() - start).total_seconds()
        hours, remainder = divmod(total_runtime, 3600)
        minutes, seconds = divmod(remainder, 60)
        # print the runtime to the text file
        #print('runtime: {:.0f} hours {:.0f} minutes {:.2f} seconds\n'.format(hours, minutes, seconds), file=text_file)
        
    print('finished at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # close the text file
    text_file.close()
    
main()