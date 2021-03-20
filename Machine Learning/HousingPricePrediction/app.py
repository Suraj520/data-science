from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/input_post',methods=['POST','GET'])
def login():
    area_type=request.form['area']
    availability=request.form['avail']
    total_sqft=request.form['total_sqft']
    bath=request.form['bath']
    balcony=request.form['balcony']
    bhk=request.form['bhk']
    bed=request.form['bed']

    string = area_type+availability+total_sqft+bath+balcony+bed+bhk
    return render_template('index.html',output=string)

if __name__ == '__main__':
    app.run()
