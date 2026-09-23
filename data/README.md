# Dataset

This folder contains the datasets used for the Titanic Survival Prediction project.

## Dataset Source

The dataset was obtained from Kaggle:

[ Titanic Dataset – Kaggle ](https://www.kaggle.com/c/titanic/data)

## Directory Structure

```text
data/
├── raw/
│   ├── .gitkeep
│   ├── train.csv
│   └── test.csv
│
├── processed/
│   ├── .gitkeep
│   ├── train_processed.csv
│   └── test_processed.csv
│
└── README.md
```

## Raw Data

### `raw/train.csv`

The original training dataset provided by Kaggle.

This dataset contains the target variable:

`Survived`

The training data is used for:

* Exploratory Data Analysis
* Data preprocessing
* Feature engineering
* Model training
* Model validation

### `raw/test.csv`

The original test dataset provided by Kaggle.

This dataset does not contain the `Survived` column.

It is used to generate predictions after the model has been trained.

## Processed Data

### `processed/train_processed.csv`

The processed training dataset generated after preprocessing and feature engineering.

This dataset is used as input for model training.

### `processed/test_processed.csv`

The processed test dataset generated using the same preprocessing steps applied to the training data.

This dataset is used for generating final predictions.

## Data Processing Workflow

```text
train.csv
    ↓
Data Cleaning & Preprocessing
    ↓
train_processed.csv
    ↓
Model Training
```

```text
test.csv
    ↓
Data Cleaning & Preprocessing
    ↓
test_processed.csv
    ↓
Trained Model
    ↓
Predictions
```

## Git Tracking

The original and processed CSV files are excluded from Git tracking because of their file size.

The dataset files should be downloaded separately and placed inside the appropriate directories.
