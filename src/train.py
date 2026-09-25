from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV,train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler


def split_data(df):
    """Split data into train and test."""
    x=df.drop(['Survived'],axis=1)
    y=df['Survived'].to_numpy()

    x_train,x_test,y_train,y_test=train_test_split(
        x,y,
        test_size=0.2,
        random_state=42)
    
    return x_test,x_train,y_test,y_train

def standardisation(x_train,x_test):
    """Standardize the training and testing data."""

    scaler=StandardScaler()
    scaler.fit(x_train)

    x_train_scaled=scaler.transform(x_train)
    x_test_scaled=scaler.transform(x_test)

    return x_train_scaled,x_test_scaled