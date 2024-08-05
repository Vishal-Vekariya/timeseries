import statsmodels
from statsmodels.tsa.arima.model import ARIMA

def arima_apple(df):
    arima = ARIMA(df.AAPL, order=(1,1,1))
    ar_model = arima.fit()
    print(ar_model.summary())
    
    return ar_model