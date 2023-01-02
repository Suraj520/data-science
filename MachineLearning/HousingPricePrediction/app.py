from flask import Flask,request,render_template
import pickle
import numpy as np
app = Flask(__name__)

with open('model/fitted_model.pkl', 'rb') as file:
    model = pickle.load(file)
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/input_post',methods=['POST','GET'])
def login():
    area_type=request.form['area']
    availability=request.form['avail']
    total_sqft=request.form['total_sqft']
    bath=request.form['bath']
    balcony=request.form['balcony']
    bhk=request.form['bhk']
    bed=request.form['bed']
    feature_vector = [area_type,availability,total_sqft,bath,balcony,bhk,bed]
    feature_vector = np.reshape(feature_vector,(1,7))
    out = model.predict(feature_vector)[0]
    out = np.round(out,2)
    return render_template('index.html',output=out)

if __name__ == '__main__':
    app.run()
