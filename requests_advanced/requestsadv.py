from flask import Flask
import requests

app =  Flask(__name__)

url = "https://google.com1111"
try:
    # Make a request
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        print("Request succeeded")
    else:
        # Request failed with an error status code
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Request encountered an exception
    print("An error occurred during the request:")
    #print(type(e))  # Print the type of the exception
    print(e)
except requests.exceptions.ConnectionError as conne:
    print("connection error")