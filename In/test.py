from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('web01.html')

@app.route('/web02.html', methods=['GET', 'POST'])
def web2():
    return render_template('web02.html')

@app.route('/web03.html', methods=['GET', 'POST'])
def web3():
    return render_template('web03.html')

if __name__ == '__main__':
    app.run()
    
