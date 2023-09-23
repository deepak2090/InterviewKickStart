from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '1234'
#Session(app)

@app.route('/')
def index():
    return 'Welcome to the login page!'
@app.route('/login', methods=['GET', 'POST'])
def login():
    import subprocess
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check credentials (replace with your logic)
        if username == 'admin' and password == 'password':
            # Valid login, redirect to the dashboard
            session['authenticated'] = True
            return redirect(url_for('dashboardx'))
        else:
            # Invalid login, show an error message
            session['authenticated'] = False
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/dashboardx')
def dashboardx():
    if not session.get('authenticated'):
        return redirect('/login')
    return 'Welcome to the dashboard function route!'
if __name__ == '__main__':
    app.run(debug=True)


