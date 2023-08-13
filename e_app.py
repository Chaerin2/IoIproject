from flask import Flask, render_template, request, url_for, redirect
from flask_cors import CORS, cross_origin
from DataClass import DataClass
import pandas as pd
import re

app = Flask(__name__)

dataClass = DataClass()


@app.route('/', methods=['POST'])
def predict():
    print("ok")
    gender = request.form['gender']
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    fit = request.form['fit']
    temp = request.form['temp']
    requestObject = {
        "gender" : gender,
        "height" : height,
        "weight" : weight,
        "fit" : fit,
        "temp" : temp
    }
    # print(requestObject)
    return requestObject


@app.route('/onclick', methods=['GET', 'POST'])
def on_click_test():
    requestObject = request.json
    dataClass.get_data(requestObject['height'], requestObject['weight'], requestObject['fit'], requestObject['gender'], requestObject['temp'])
    return requestObject


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('web01.html')

@app.route('/web01.html', methods=["GET", "POST"])
def web1():
    return render_template('web01.html')

@app.route('/web02.html', methods=["GET", "POST"])
def web2():
    return render_template('web02.html')

@app.route('/web03.html', methods=["GET", "POST"])
def web3():
    return render_template('web03.html')

# model = pickle.load(open('rf.pickle','rb'))
# scale = pickle.load(open('standard_scaler.pickle','rb'))
# ohe = pickle.load(open('one_hot_encoder.pickle','rb'))

@app.route('/test')
def test_2():
    value1 = dataClass.toValue()
    print(value1['temp'])
    return value1['temp']

@app.route('/test1')
def test_1():
    print("--------")
    # dataClass.print_data()
    result = dataClass.return_data()
    result_size = result[0]
    # print(result_size)
    return result_size[0]

@app.route('/test2')
def test_3():
    result = dataClass.return_data()
    result_num = result[1]
    
    df = pd.read_csv('image_matching.csv')
    pd.set_option('display.max_colwidth', None)

    links = df[df['number'] == int(result_num)]
    image_link = links['image_link']
    image_link = str(image_link)

    pattern_image = r'(//\S+)'
    image_link = re.search(pattern_image, image_link).group()
    
    purchase = links['purchase']
    purchase = str(purchase)

    pattern_purchase = r'(http\S+)'
    purchase_link = re.search(pattern_purchase, purchase).group()

    return image_link

@app.route('/test3')
def test_4():
    result = dataClass.return_data()
    result_num = result[1]
    
    df = pd.read_csv('image_matching.csv')
    pd.set_option('display.max_colwidth', None)

    links = df[df['number'] == int(result_num)]
    
    purchase = links['purchase']
    purchase = str(purchase)

    pattern_purchase = r'(http\S+)'
    purchase_link = re.search(pattern_purchase, purchase).group()

    return purchase_link

if __name__ == '__main__':
    app.run(port=5000)