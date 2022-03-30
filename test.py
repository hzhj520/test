from unittest import result
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_login", methods=['POST', 'GET'])
def get_login():
    
    if request.method == "GET":
        user = request.args.get("user")
        password = request.args.get("password")
    elif request.method == "POST":
        if request.content_type.startswith('application/json'):   
            user = request.json.get('user') 
            password = request.json.get('password')
        elif request.content_type.startswith('multipart/form-data'):
            user = request.form.get('user')
            password = request.form.get('password')
        else:
            user = request.values.get("user")
            password = request.values.get("password")

    if user == "admin123" and password == "admin123":
        results = {"code": 200, "result": {"user": "admin123", "password": "admin123"}}
        return json.dumps(results)
    else:
        error = 'Invalid username/password'
        return jsonify(error)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333, debug=True)
