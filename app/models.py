#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# user ORM对象模型

from app import db
from hashlib import md5

ROLE_USER = 0
ROLE_ADMIN = 1

#创建User类
#字段使用db.Column类创建实例
#__repr__方法告诉Python如何打印class对象，方便我们调试使用。 
class User(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	nickname = db.Column(db.String(64),index = True ,unique = True)
	email = db.Column(db.String(120),index = True,unique = True)
	role = db.Column(db.SmallInteger,default = ROLE_USER)
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime)

	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return self.id
	def avatar(self, size):
		return 'http://www.gravatar.com/avatar/' + md5(self.email.encode('utf8')).hexdigest() + '?d=mm&s=' + str(size)

	#静态方法
	@staticmethod
	def make_unique_nickname(nickname):
		if User.query.filter_by(nickname = nickname).first() == None:
			return nickname
		version = 2
		while True:
			new_nickname = nickname + str(version)
			if User.query.filter_by(nickname = new_nickname).first() == None:
				break
			version += 1
		return new_nickname

	def __repr__(self):
		return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
 
    def __repr__(self):
        return '<Post %r>' % (self.body)
