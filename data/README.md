# Dataset

This folder contains the raw and processed datasets used in the Titanic Survival Prediction project.

## Dataset Source

The dataset was obtained from the Kaggle Titanic competition:

https://www.kaggle.com/c/titanic/data

## Directory Structure

```text
data/
├── raw/
│   ├── train.csv
│   └── test.csv
│
├── processed/
│   ├── train_processed.csv
│   └── test_processed.csv
│
└── README.md
```

## Raw Data

### `raw/train.csv`

The original training dataset.

It contains passenger information and the `Survived` target variable.

### `raw/test.csv`

The original test dataset.

It contains passenger information but does not contain the `Survived` target variable.

## Processed Data

The preprocessing steps are implemented in:

```text
src/preprocessing.py
```

The processed datasets are generated using the preprocessing pipeline and saved separately:

* `train_processed.csv`
* `test_processed.csv`

The processed datasets are used in the modeling and prediction stages.

## Data Workflow

```text
train.csv
    ↓
Preprocessing
    ↓
train_processed.csv
    ↓
Model Training


test.csv
    ↓
Preprocessing
    ↓
test_processed.csv
    ↓
Prediction
```

The raw and processed CSV files are excluded from Git tracking using `.gitignore`.

