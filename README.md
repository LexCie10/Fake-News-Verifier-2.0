# Fake-News-Verifier-2.0

A brief description of our project.

**Table of Contents**

* Introduction
* Dataset
* Preprocessing
* Model Development and Evaluation
* Model Deployment
* Findings and Observations
* Recommendations

**Introduction:**

In this repository, we have built a pipeline model using a combination of PassiveAggressiveClassifier and Tfidfvectorizer to create a webapp that can identify and classify news into Real or Fake News categories by analyzing, news article text, title and url/domain. This project is justified as it is intended to contribute to the fight against Fake and unverified news.

**Dataset:**

The dataset used was obtained from DataFlair and has a dimension of 6335x4, meaning it consists of 6335 rows and 4 columns. we analyzed text from the "text" and "title" columns to predict outcomes in the "label" columns.

**Preprocessing:**

Preprocessing steps involved:

* Naming an unnamed column in our dataset

* Handling missing values

* Removed Text from numeric columns

* Cleaned our "label" column as it had unwanted text categories in it

* Mapped our "Fake" and "Real" categories in our "label" category to "0" and "1", essentially converting our categorical column to numeric.


**Model Development**

The process of building our model into a pipeline involved:
* splitting our data in to train and test sets with 70% of our data used for training the model and 30% to test the model
* defining our X and y
* defining a list of some trusted domains and training our model to extract these domains if present
* setting up a pipeline of our model of choice and the tfidfvectorizer, and fitting our training data to it
* using StratifiedKFold Cross-Valifdation technique to train our model repeatedly so as to help improve prediction accuracy, print the cv_score
* fitting the pipeline to the train data
* testing our pipeline with the test data
* further evaluation of our pipeline using accuracy score and classification report

**Model Deployment**

This project was deployed on streamlit cloud using pandas, pickle, re and tldextract. CSS was used to further enhance the look of our webapp interface.

**Findings and Observations**

* This model achieves 92.37% accuracy, which is high for Fake News detection.
* It consistently performed well across different data splits during cross-validation (~92.6%).
* It balances precision and recall, ensuring it detects fake news while minimizing false alarms and errors.
* The low standard deviation shows reliability across datasets.
  
**Recommendation**

Although our model has a high accuracy score and is performing relatively well, there is still room fro improve, as the closer we are to a 100% accuracy, the better for us. Below are recommendations for further work to improve the model:
* We could try out more models like Ensemble Learning, XGBoost, Deep Learning and even a combination of models.
* Further feature engineering can be conducted, we can add trusted authors, publication dates, more relevant columns and even implement a readability score.
* We could fine tune our hyper parameter using GridSearchCV.
* Ee can implement a feedback system to track misclassification where users can report wrong predictions.
* We can also use Explainable AI to automatically explain why our model classified an article as Fake or Real.

**Contributing**

* Fork the repository.
* Create a new branch.
* Make changes and commit.
* Submit a pull request.

**License:**

MIT License

**Acknowledgments**

GOD ALMIGHTY
Pluralcode Academy
