from flask import Flask, request, jsonify
import bcrypt
import json
app = Flask(__name__)

def hellodeepak():
    return "hello deepak"

@app.route('/')
def hello_world():
    return hellodeepak()

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Verify a password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

# Example route for registering a user
@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    username = user_data['username']
    password = user_data['password']

    # Hash the user's password before storing it in the database
    hashed_password = hash_password(password)

    # Store the username and hashed_password in the database
    # (You would typically use a database here)

    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    username = user_data['username']
    password = user_data['password']

    # Retrieve the stored hashed password for the given username from the database
    # (You would typically use a database here)

    # Verify the entered password against the stored hashed password
    if verify_password(password, stored_hashed_password):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

if __name__ == '__main__':
    app.run()

