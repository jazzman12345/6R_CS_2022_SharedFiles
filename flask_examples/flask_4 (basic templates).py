from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def greet(name=''):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)