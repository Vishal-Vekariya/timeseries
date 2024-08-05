
def evaluate_model(ar_model, steps=2):
    forecast = ar_model.get_forecast(2)
    ypred = forecast.predicted_mean
    conf_int = forecast.conf_int(alpha=0.05)
    
    return ypred,conf_int