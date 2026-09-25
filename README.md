# Titanic Survival Prediction

A complete machine learning classification project for predicting passenger survival on the Titanic using the Kaggle Titanic dataset.

## Overview

This project implements an end-to-end machine learning pipeline including:

* Exploratory Data Analysis (EDA)
* Data Preprocessing
* Feature Engineering
* Model Training
* Model Evaluation
* Prediction on the Kaggle test dataset
* Generation of the Kaggle submission file

## Dataset

The project uses the Titanic dataset from **Kaggle**.

* `train.csv` — training dataset containing the `Survived` target.
* `test.csv` — test dataset used for generating predictions.

## Project Structure

```text
titanic/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── submission/
│   │   └── predictions.csv
│   └── README.md
│
├── models/
│   └── model.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── outputs/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Workflow

```text
train.csv
     ↓
EDA
     ↓
Preprocessing
     ↓
train_processed.csv
     ↓
Model Training
     ↓
model.pkl
     ↓
test.csv
     ↓
Preprocessing
     ↓
test_processed.csv
     ↓
Prediction
     ↓
data/submission/predictions.csv
```

## Models

The following classification models are implemented:

* Random Forest Classifier
* Decision Tree Classifier
* Logistic Regression

Hyperparameter tuning is performed using `GridSearchCV` to find the best configuration for each model.

## Evaluation Metrics

The models are evaluated using the following metrics:

* Accuracy
* Precision
* Recall
* F1 Score

## Submission File

The final prediction file is stored in:

```text
data/submission/predictions.csv
```

`predictions.csv` contains two columns:

| Column        | Description                          |
| ------------- | ------------------------------------ |
| `PassengerId` | Unique passenger identifier          |
| `Survived`    | Predicted survival (0 = No, 1 = Yes) |

The generated file follows the required format for submission to the Kaggle Titanic competition.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
