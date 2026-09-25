from pathlib import Path
import pandas as pd

project_root=Path(__file__).resolve().parent.parent
train_data=project_root/'data'/'raw'/'train.csv'
test_data=project_root/'data'/'raw'/'test.csv'
train_processed=project_root/'data'/'processed'/'train_processed.csv'
test_processed=project_root/'data'/'processed'/'test_processed.csv'

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

def load_preprocessed_train(path=train_processed):
    """Load the preprocessed dataset""" 

    if not Path(path).exists():
        raise FileNotFoundError('Preprocessed train dataset not found')
    else:
        return pd.read_csv(path)    


def load_preprocessed_test(path=test_processed):
    """Load the preprocessed dataset""" 

    if not Path(path).exists():
        raise FileNotFoundError('Preprocessed test dataset not found')
    else:
        return pd.read_csv(path)    
    
