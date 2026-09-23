# Titanic Survival Prediction

## Overview

This project focuses on predicting passenger survival on the Titanic using machine learning classification models.

The project includes data exploration, preprocessing, feature engineering, model training, evaluation, and prediction.

## Dataset

The dataset is obtained from the Kaggle Titanic competition.

The dataset contains two main files:

* `train.csv` — contains passenger information and the `Survived` target variable.
* `test.csv` — contains passenger information without the `Survived` target variable.

## Project Structure

```text
titanic-survival-prediction/
│
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   └── test.csv
│   │
│   ├── processed/
│   │   ├── train_processed.csv
│   │   └── test_processed.csv
│   │
│   └── README.md
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── models/
│   └── model.pkl
│
├── outputs/
│   └── figures/
│
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## Project Workflow

```text
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Data Preprocessing
     ↓
Feature Engineering
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Prediction
```

## Exploratory Data Analysis

The `01_eda.ipynb` notebook is used to explore the Titanic dataset.

The analysis includes:

* Dataset structure
* Missing values
* Numerical feature distributions
* Categorical feature distributions
* Survival distribution
* Survival by sex
* Survival by passenger class
* Age and survival
* Fare and survival
* Correlation analysis

## Data Preprocessing

The preprocessing steps are implemented in `src/preprocessing.py`.

The preprocessing pipeline contains three main classes:

* `AgeImputer`
* `FeatureEncoder`
* `FeaturesDropper`

These classes are combined into a preprocessing pipeline and applied to the training and test datasets.

The processed datasets are saved as:

```text
data/processed/train_processed.csv
data/processed/test_processed.csv
```

## Machine Learning Models

The project uses classification models to predict passenger survival.

The planned models include:

* Random Forest Classifier
* XGBoost Classifier
* LightGBM Classifier

## Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* LightGBM
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook

## Installation

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the notebooks in the following order:

```text
01_eda.ipynb
      ↓
02_preprocessing.ipynb
      ↓
03_modeling.ipynb
```

The preprocessing notebook generates the processed training and test datasets, which are then used during the modeling stage.

## License

This project is licensed under t
