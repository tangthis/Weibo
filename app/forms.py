#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 使用Flask-WTF创建表单
from flask.ext.wtf import Form
from wtforms import StringField,BooleanField,TextField,TextAreaField
from wtforms.validators import Required,Length

#从Form类继承
class LoginForm(Form):
	openid = TextField('openid',validators = [Required()])
	remember_me = BooleanField('remember_me',default = False)

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
