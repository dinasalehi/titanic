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

def tree_models(model,param_grid,x_train,x_test,y_train,y_test):
    """ Train and tune a tree-based regression model using GridSearchCV."""

    grid_search=GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring='accuracy',
        return_train_score=True,
        n_jobs=-1)
    grid_search.fit(x_train,y_train) 
    best_model=grid_search.best_estimator_
    y_pred=best_model.predict(x_test)
    acc=accuracy_score(y_pred,y_test)
    return best_model,y_pred,acc
   
   