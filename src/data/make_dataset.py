import pandas as pd
data_path = "data/raw/AAPL.csv"

def load_and_preprocess_data(data_path):
    
    # Import the data from 'credit.csv'
    data = pd.read_csv(data_path)
    data['Date'] = pd.to_datetime(data['Date'])
    
    df = data.set_index('Date')
    # Univariate analysis - We will only use 'Apple' variable.
    
    return df
