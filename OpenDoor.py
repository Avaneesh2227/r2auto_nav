#OpenDoor.py
import requests

# Define the URL for the POST request
url = "http://192.168.60.159/openDoor"

# Define the JSON payload
payload = {
    "action": "openDoor",
    "parameters": {
        "robotId": "<TurtleBot3_ID>"
    }
}

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_response = response.json()

    # Extract the message from the response
    message = json_response["data"]["message"]

    # Print the message
    print("Received message:", message)

    # If the message contains "door1", you can store it as "door 1"
    stored_message = message
    print("Stored message:", stored_message)
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
