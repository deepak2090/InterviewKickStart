from flask import Flask, redirect, url_for, session, render_template
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    trigger_history = session.get('trigger_history', [])
    return render_template('indextrigger.html', trigger_history=trigger_history)

@app.route('/trigger_multiple_times/<int:num_times>')
def trigger_multiple_times(num_times):
    trigger_history = session.get('trigger_history', [])
    
    for _ in range(num_times):
        # Generate a unique identifier for each trigger
        trigger_id = str(uuid.uuid4())
        trigger_history.append(trigger_id)

    # Store the trigger history in the session
    session['trigger_history'] = trigger_history

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
