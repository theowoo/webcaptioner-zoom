# stream.py
# initial proof of concept to
# demonstrate Web Captioner's Webhooks

import os, sys, json
from flask import Flask, request, make_response

# global constants/flags
DEBUG = True
PORT = 9999

# clear function
def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

# define a flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Hello world!"

@flask_app.route('/transcribe', methods=['GET'])
def transcribe_get():
    return "Can access /transcribe just fine"

# main post request handler
@flask_app.route('/transcribe', methods=['POST', 'PUT'])
def transcribe_post():
    reqBody = request.get_json()
    print(reqBody['transcript'], end=" ")
    return make_response(json.dumps({"message": "recieved"}), 200, {"Content-Type": 'application/json'})

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', debug=DEBUG, port=PORT)
