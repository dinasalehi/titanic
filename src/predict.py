from pathlib import Path
import joblib

PROJECT_ROOT=Path(__file__).parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "model.pkl"

def load_model(path=MODEL_PATH):
    """Load trained model"""
    if not Path(path).exists:
        raise FileNotFoundError(f'Model not found :{path}')
    else:
        return joblib.load(path)

def predict(model,df):
    """Make predictions using the trained model."""

    predictions=model.predict(df)
    return predictions