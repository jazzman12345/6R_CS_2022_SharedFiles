from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    text = 'This is a website!'
    text += '\n<p><a href = "/hello">Hello</a>'
    return text

@app.route('/hello/')
def hello():
    return f'Hello anonymous person.'

@app.route('/hello/<name>')
def greet(name):
    return f'Hello there, {name}'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)