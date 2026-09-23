# Titanic Survival Prediction

A machine learning project for predicting passenger survival on the Titanic using the Titanic dataset from Kaggle.

## Project Overview

The goal of this project is to build a classification model that predicts whether a passenger survived the Titanic disaster based on passenger and travel information.

The project follows a structured machine learning workflow including:

* Exploratory Data Analysis (EDA)
* Data preprocessing
* Feature engineering
* Model training
* Hyperparameter tuning
* Model evaluation
* Prediction

## Dataset

The dataset used in this project is the Titanic dataset from Kaggle.

The dataset contains information about Titanic passengers, including:

* Passenger class
* Sex
* Age
* Number of siblings/spouses aboard
* Number of parents/children aboard
* Ticket information
* Fare
* Cabin
* Port of embarkation

The target variable is:

`Survived`

where:

* `0` = Did not survive
* `1` = Survived

The original dataset contains two CSV files:

* `train.csv`
* `test.csv`

## Project Structure

```text
titanic-survival-prediction/
│
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   ├── train.csv
│   │   └── test.csv
│   │
│   ├── processed/
│   │   ├── .gitkeep
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
train.csv
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
Trained Model
    ↓
test.csv
    ↓
Prediction
```

## Notebooks

### 01_eda.ipynb

This notebook performs exploratory data analysis on the Titanic training dataset.

The analysis includes:

* Dataset structure
* Descriptive statistics
* Missing values
* Target variable distribution
* Categorical feature analysis
* Numerical feature analysis
* Relationships between features and survival

### 02_preprocessing.ipynb

This notebook prepares the data for machine learning.

The preprocessing steps include:

* Handling missing values
* Removing or transforming unnecessary columns
* Feature engineering
* Encoding categorical variables
* Preparing the training and test datasets

The processed datasets are saved inside:

```text
data/processed/
```

### 03_modeling.ipynb

This notebook focuses on training and evaluating classification models.

The main steps include:

* Loading the processed training dataset
* Splitting the training data into training and validation sets
* Training classification models
* Hyperparameter tuning using `GridSearchCV`
* Evaluating model performance
* Comparing models
* Saving the trained model

## Models

The project uses tree-based classification algorithms such as:

* Random Forest Classifier
* XGBoost Classifier

Additional models can be added in the future.

## Evaluation Metrics

The models are evaluated using classification metrics including:

* Accuracy
* Precision
* Recall
* F1 Score

These metrics provide different perspectives on classification performance.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/USERNAME/titanic-survival-prediction.git
cd titanic-survival-prediction
```

Install the dependencies:

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

The trained model is saved in:

```text
models/model.pkl
```

## Dataset Files

The original dataset files are not included in the GitHub repository because they are excluded through `.gitignore`.

To reproduce the project, download the Titanic dataset from Kaggle and place the files inside:

```text
data/raw/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
