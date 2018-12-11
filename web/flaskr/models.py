from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import json
from .settings import app

db = SQLAlchemy(app)

class UserCredentials(db.Model):
	__tablename__ = 'User_Credentials'
	user_id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String, nullable=False) # TODO: ask limitations
	password = db.Column(db.String, nullable=False)


	def login_user(login, password):
		user_log = UserCredentials(login=login, password=password)
		db.session.add(user_log)
		db.session.commit()

	def login_password_match(login, password):
		user = UserCredentials.query.filter_by(login=login).filter_by(password=password).first()
		return not (user is None)

	def get_user_id(login, password):
		user = UserCredentials.query.filter_by(login=login).filter_by(password=password).first()
		return user.user_id

	def is_unique_login(login):
		user = UserCredentials.query.filter_by(login=login).first()
		return (user is None)


class UserInfomation(db.Model):
	__tablename__ = 'User_Information'
	information_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('User_Credentials.user_id'), nullable=False)
	user_name = db.Column(db.String, nullable=False)
	user_surname = db.Column(db.String, nullable=False)
	avatar_url = db.Column(db.String, nullable=True) #TODO: May url be NULL?

	def json(self):
		return {'user_name': self.user_name,
		        'user_surname': self.user_surname,
		        'avatar_url': self.avatar_url}


	def register_user(user_id, name, surname, avatar_url):
		user_reg = UserInfomation(user_id=user_id, user_name=name, user_surname=surname, avatar_url=avatar_url)
		db.session.add(user_reg)
		db.session.commit()


	def get_user_by_id(user_id):
		return UserInfomation.json(UserInfomation.query.filter_by(user_id=user_id).first())


	def __repr__(self):
		user = {
		'user_name': self.user_name,
		'user_surname': self.user_surname,
		'avatar_url': self.avatar_url
		}
		return json.dumps(user)
