import pandas as pd
from pathlib import Path
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

project_root=Path(__file__).resolve().parent.parent
processed_train_path=project_root/'data'/'processed'/'train_processed.csv'
processed_test_path=project_root/'data'/'processed'/'test_processed.csv'


class AgeImputer(BaseEstimator,TransformerMixin):

    def __init__(self):
        self.imputer=SimpleImputer(strategy='mean')

    def fit(self,x,y=None):
        self.imputer.fit(x[['Age']]) 
        return self   
    
    def transform(self,x):
        x=x.copy()
        x['Age']=self.imputer.fit_transform(x[['Age']])
        return x 


class FeatureEncoder(BaseEstimator,TransformerMixin):

    def fit(self,x,y=None):
        self.embarked_encoder=OneHotEncoder(handle_unknown='ignore',sparse_output=False).fit(x[['Embarked']])
        self.sex_encoder=OneHotEncoder(handle_unknown='ignore',sparse_output=False).fit(x[['Sex']])
        return self
    
    def transform(self,x):

     

        matrix=self.embarked_encoder.transform(x[['Embarked']])
        column_names=["C","S","Q","N"]
        for i in range(len(matrix.T)):
            x[column_names[i]]=matrix.T[i]

        matrix=self.sex_encoder.transform(x[['Sex']])
        column_names=['Female','Male']
        for i in range(len(matrix.T)):
            x[column_names[i]]=matrix.T[i]
        return x    


class FeaturesDropper(BaseEstimator,TransformerMixin):
    def fit(self,x,y=None):
        return self
    def transform(self,x):
        return x.drop([ 'Name', 'Sex',
      'Ticket','Cabin', 'Embarked','N'],axis=1,errors='ignore')    



def preprocess_data(df):
    """ Clean and preprocess 
    the titanic datasets"""

    pipe=Pipeline([('AgeImputer',AgeImputer()),('FeatureEncoder',FeatureEncoder()),('FeaturesDropper',FeaturesDropper())])
    df=pipe.fit_transform(df)
    return df

def save_processed_train(df):
    """Save the processed dataset as csv file"""
    processed_train_path.parent.mkdir(parents=True,exist_ok=True)

    df.to_csv(processed_train_path,index=False)


def save_processed_test(df):
    """Save the processed dataset as csv file"""
    processed_test_path.parent.mkdir(parents=True,exist_ok=True)

    df.to_csv(processed_test_path,index=False)    
