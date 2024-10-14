from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__) 

model = joblib.load("RandomForestRegressor.joblib")

@app.route('/')
def hello_world() : 
    return render_template('crypto_exchange.html')



@app.route('/predict', methods = ['GET', 'POST'])  
def predict() : 
    int_features=[np.double(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output = prediction 

    return render_template('crypto_exchange.html', pred='Prediction of the Volume is {}'.format(output))
    
    

if __name__ == '__main__' : 
    app.run()