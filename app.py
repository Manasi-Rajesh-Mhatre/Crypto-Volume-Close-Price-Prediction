from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__) 

model = joblib.load("xgboost.joblib")
model2 = joblib.load("RandomForestRegressorCP.joblib")

@app.route('/')
def hello_world():
    return render_template('crypto_exchange.html', active_tab='volume')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [np.double(x) for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model.predict(final)
    output = prediction[0]
    
    return render_template(
        'crypto_exchange.html', 
        pred=f'Predicted volume is {output}', 
        active_tab='volume', 
        open_value=request.form.get('Open'), 
        high_value=request.form.get('High'), 
        low_value=request.form.get('Low'), 
        close_value=request.form.get('Close'), 
        adj_close_value=request.form.get('Adj Close'), 
        type_value=request.form.get('Type')
    )

@app.route('/predict2', methods=['POST'])
def predict2():
    int_features = [np.double(x) for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model2.predict(final)
    output = prediction[0]
    
    return render_template(
        'crypto_exchange.html', 
        pred2=f'Predicted closing price is {output}', 
        active_tab='closePrice', 
        open_value=request.form.get('Open'), 
        high_value=request.form.get('High'), 
        low_value=request.form.get('Low'), 
        volume_value=request.form.get('Volume'), 
        type_value=request.form.get('Type')
    )

@app.route('/volume/reset')
def reset_volume():
    return render_template('crypto_exchange.html', active_tab='volume')

@app.route('/closePrice/reset')
def reset_close_price():
    return render_template('crypto_exchange.html', active_tab='closePrice')


if __name__ == '__main__':
    app.run()
