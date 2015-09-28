#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 使用Flask-WTF创建表单
from flask.ext.wtf import Form
from wtforms import StringField,BooleanField,TextField
from wtforms.validators import Required

#从Form类继承
class LoginForm(Form):
	openid = TextField('openid',validators = [Required()])
	remember_me = BooleanField('remember_me',default = False)
