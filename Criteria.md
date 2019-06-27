# Criteria for Project
In this project I would like you to demonstrate the Text Preprocessing methods and some basic NLP Machine Learning models in a `Juptyer Notebook`. If you complete the following project with extra time I will add an additional segment of Deep Learning with NLP.


## Text Preprocessing
In this segment you will implement the following text preprocessing pieces prior to the models. In each of these segments you will take the original data and process it and store the new value in a new column of the Pandas DataFrame.

The following Preprocessing methods should be as follows:
* Removal of Stop Words
* Tokenization
* Stemming
* Lemmatization


After each of the methods performed please store the end result into the Pandas Dataframe as a new feature and save updated Pandas doc as a CSV to the `data` directory with a distinct name.


## Machine Learning Models

In this segment please use the Scikit-learn and NLTK to perform some if not most of the actions.

### Bag of Words Model
In this segment you will use the Bag of Words with a type Bayes Classifier. Please set the random state for the `train_test_split` to 1.

Please get the Accuracy Metrics.

### TF-IDF
In this segment you will convert the collection of documents to a matrix of TF-IDF. Then use a type of Bayes Classifer.

Please set the randome state in the `train_test_split` to 123.

Please get the Accuracy Metrics

### Logistic Regression
Use the collection of documents in matrix of TF-IDF and use a Logistic Regression classifier and find the best regularization for the LR.

Please get the Accuracy Metrics.

### Extra Credit

Transform the rating to a binary representation and run through the steps again. 

If time allows try using the lemmatization and segmentation values in the given models and see if the Accuracy improves.

If you want to move on to DL then let me know.

