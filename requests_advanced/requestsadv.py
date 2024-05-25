

import requests
url = "https://google.com"
try:
    # Make a request
    response = requests.post(url)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        print("Request succeeded")
        print(response.content)
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