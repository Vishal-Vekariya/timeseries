from src.data.make_dataset import load_and_preprocess_data
from src.models.train_model import arima_apple
from src.models.predict_model import evaluate_model

if __name__ == "__main__":
    # Load and preprocess the data
    data_path = "data/raw/AAPL.csv"
    
    df = load_and_preprocess_data(data_path)
    
    ar_model = arima_apple(df)
    
    ypred,conf_int = evaluate_model(ar_model, steps=2)
    
    ypred
    conf_int
    
    
    