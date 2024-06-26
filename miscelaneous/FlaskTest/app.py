from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regression', methods=['POST'])
def regression_form():
    test = request.form['test']
    app_name = request.form['app']
    return redirect(url_for('regression', test=test, app=app_name))

@app.route('/regression/<test>/<app>')
def regression(test, app):
    # Your existing code to handle the regression logic
    return f'Regression test {test} for app {app}'

if __name__ == '__main__':
    app.run(debug=True)
