from flask import Flask 
from flask import jsonify
from flask import request
from flask import Response


# app = Flask(__name__)
from .settings import *
from .models import *

import uuid

# test
@app.route("/")
def test():
	return "Little success"

# POST register user
@app.route("/register", methods=['POST'])
def register_user():
	request_data = request.get_json()
	if (validate_login(request_data) and validate_register(request_data)):
		if (UserCredentials.is_unique_login (request_data['login'])):
			UserCredentials.login_user(request_data['login'], request_data['password'])
			UserInfomation.register_user(UserCredentials.get_user_id(request_data['login'], request_data['password']),
	                                     request_data['user_name'], request_data['user_surname'], 
	                                     request_data['avatar_url'])
			return Response("Success")
		else:
			return Response("Not unique login", status=401, mimetype='application/json')
	else:
		return Response("Not valid input", status=401, mimetype='application/json')
	

# POST login user
@app.route("/login", methods=['POST'])
def login_user():
	request_data = request.get_json()
	if (UserCredentials.login_password_match(request_data['login'], request_data['password'])):
		# such user is found, return token
		token = uuid.uuid4()
		return str(token)
	else:
		return Response("", status=401, mimetype='application/json')


# GET user information from UserInformation table
@app.route("/user/<int:user_id>")
def get_user_by_id(user_id):
	user = UserInfomation.get_user_by_id(user_id)
	return jsonify(user)


def validate_login(request_data):
	return ("login" in request_data and "password" in request_data)


def validate_register(request_data):
	return ("user_name" in request_data and "user_surname" in request_data and "avatar_url" in request_data)
