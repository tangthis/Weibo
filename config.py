#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 配置

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir,'search.db')
# SQLALCHEMY_DATABASE_URI是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径。
# SQLALCHEMY_MIGRATE_REPO 是用来存储SQLAlchemy-migrate数据库文件的文件夹。 

CSRF_ENABLED = True #启用了跨站请求攻击保护
SECRET_KEY = 'you-will-never-guess' #token供表单验证

POSTS_PER_PAGE = 3

OPENID_PROVIDERS = [
	{ 'name': 'OpenID', 'url': 'http://tangthis.openid.org.cn/' },
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' }
    ]

#=========== Mail配置========
MAIL_SERVER = 'stmp.163.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USENAME = 'tangthis'
MAIL_PASSWORD = 'pwd'

ADMINS = ['tangthis@163.com']