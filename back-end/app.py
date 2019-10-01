from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources = {r'/*': {'origins': '*'}})

input_file = "E:/work/Login-techlab-board/back-end/email.txt"


# sanity check route
@app.route('/ping', methods = ['GET'])
@cross_origin()
def ping_pong():
    return jsonify('welcome!')


def check_email(email):
    check = False
    with open(input_file, 'r') as file:
        for line in file:
            print(line)
            if email.strip() == line.strip():
                check = True
                break
                # print('the email is valid')
        return check


@app.route('/login', methods = ['POST'])
@cross_origin()
def authenticate_email():
    email = request.get_json()['email']

    if check_email(email):
        return jsonify({
            "success": True,
            "errors": []
        })
    else:
        return jsonify({
            "success": False,
            "errors": [{
                "field": "email",
                "message": "Email is not registered."
            }]
        })


if __name__ == '__main__':
  
    app.run()

