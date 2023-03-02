from flask import Flask, redirect, request, render_template, session

app = Flask(__name__)

@app.route('/')
@app.route('/getname', methods = ['POST', 'GET'])
def get_name():
    if request.method == 'POST':
        typed_name = request.form['name']
    else:
        typed_name = ''

    return render_template('hello_form.html', name=typed_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

    