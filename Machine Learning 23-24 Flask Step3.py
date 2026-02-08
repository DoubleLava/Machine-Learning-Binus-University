# setting
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

## Step 3: Use HTTP Methods (GET vs POST)

from flask import request
# Import request:
# - Represents the incoming HTTP request
# - Contains data sent by the client (browser, Python script, Postman, etc.)

@app.route("/greet", methods=["POST"])
# Define a URL endpoint called "/greet"
# - This endpoint accepts ONLY POST requests
# - POST is used when the client needs to SEND data to the server
def greet():
    # This function runs when a POST request is sent to /greet

    data = request.get_json()
    # Read JSON data from the request body
    # Example incoming JSON:
    # {
    #   "name": "Alice"
    # }
    # After this line:
    # data == {"name": "Alice"}

    name = data["name"]
    # Extract the value associated with the key "name"
    # Store it in the variable 'name'

    return {"message": f"Hello, {name}!"}
    # Create a Python dictionary
    # Flask automatically converts it to JSON
    # Sends it back as the response to the client

if __name__ == "__main__":
    app.run(debug=True)