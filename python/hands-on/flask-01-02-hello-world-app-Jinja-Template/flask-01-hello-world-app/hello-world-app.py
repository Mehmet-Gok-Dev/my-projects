from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from Flask!!!'

@app.route('/second')
def second():
    return 'Second Page!!!'

@app.route('/third')
def third():
    return 'Third Page!!!'

@app.route('/forth/<string:id>')
def forth(id):
    return f'id number is {id}'

if __name__ == '__main__':
    app.run(debug=True, port=5000)