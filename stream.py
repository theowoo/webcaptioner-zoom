# stream.py
# initial proof of concept to
# demonstrate Web Captioner's Webhooks

import os, sys, json
from flask import Flask, request, make_response

# global constants/flags
DEBUG = True
PORT = 80

# clear function
def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

# define a flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Hello world!"

# main post request handler
@flask_app.route('/transcribe', methods=['POST'])
def result():
    reqBody = request.get_json()
    print(reqBody['transcript'], end=" ")
    return make_response(json.dumps({"message": "recieved"}), 200, {"Content-Type": 'application/json'})

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', debug=DEBUG, port=PORT)
