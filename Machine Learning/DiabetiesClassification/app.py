from flask import Flask,request,render_template
import pickle
import numpy as np
app = Flask(__name__)

with open('model/diabeties_classification_model.pkl', 'rb') as file:
    model = pickle.load(file)
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/input_post',methods=['POST','GET'])
def login():
    pregnancy=request.form['preg']
    glucose=request.form['gluc']
    bp=request.form['bp']
    skinthick=request.form['skinthick']
    insulin=request.form['insulin']
    bmi=request.form['bmi']
    diabetes_ped=request.form['diabetes_ped']
    age=request.form['age']
    feature_vector = [pregnancy,glucose,bp,skinthick,insulin,bmi,diabetes_ped,age]
    feature_vector = np.reshape(feature_vector,(1,8))
    out = model.predict(feature_vector)[0]
    print(out)
    return render_template('index.html',output=out)

if __name__ == '__main__':
    app.run()
