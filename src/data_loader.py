from pathlib import Path
import pandas as pd

project_root=Path(__file__).resolve().parent.parent
train_data=project_root/'data'/'raw'/'train.csv'
test_data=project_root/'data'/'raw'/'test.csv'
processed_data_path=project_root/'data'/'processed'/'clean_data.csv'

def load_train_data(path=train_data):
    """Load the raw train dataset"""

    if not Path(path).exists():
        raise FileNotFoundError('Dataset train not found !')
    else:
        df=pd.read_csv(path)
        return df

def load_test_data(path=test_data):
    """Load the raw test dataset"""  
    if not Path(path).exists():
        raise FileNotFoundError('Dataset test not found !')      
    else:
        df=pd.read_csv(path)
        return df

def load_preprocessed_data(path=processed_data_path):
    """Load the preprocessed dataset""" 

    if not Path(path).exists():
        raise FileNotFoundError('Preprocessed dataset not found')
    else:
        return pd.read_csv(path)    
