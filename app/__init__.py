#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

#创建Flask类应用对象，导入views视图模块
from flask import Flask 

app = Flask(__name__) 
app.config.from_object('config')

from app import views