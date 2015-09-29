#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 单元测试

import os
import unittest
from datetime import datetime,timedelta
from config import basedir
from app import app, db
from app.models import User, Post


class TestCase(unittest.TestCase):

	def test_follow_posts(self):
		# make four users
		u1 = User(nickname = 'john', email = 'john@example.com')
		u2 = User(nickname = 'susan', email = 'susan@example.com')
		u3 = User(nickname = 'mary', email = 'mary@example.com')
		u4 = User(nickname = 'david', email = 'david@example.com')
		db.session.add(u1)
		db.session.add(u2)
		db.session.add(u3)
		db.session.add(u4)
		# make four posts
		utcnow = datetime.utcnow()
		p1 = Post(body = "post from john", author = u1, timestamp = utcnow + timedelta(seconds = 1))
		p2 = Post(body = "post from susan", author = u2, timestamp = utcnow + timedelta(seconds = 2))
		p3 = Post(body = "post from mary", author = u3, timestamp = utcnow + timedelta(seconds = 3))
		p4 = Post(body = "post from david", author = u4, timestamp = utcnow + timedelta(seconds = 4))
		db.session.add(p1)
		db.session.add(p2)
		db.session.add(p3)
		db.session.add(p4)
		db.session.commit()
		# setup the followers
		u1.follow(u1) # john follows himself
		u1.follow(u2) # john follows susan
		u1.follow(u4) # john follows david
		u2.follow(u2) # susan follows herself
		u2.follow(u3) # susan follows mary
		u3.follow(u3) # mary follows herself
		u3.follow(u4) # mary follows david
		u4.follow(u4) # david follows himself
		db.session.add(u1)
		db.session.add(u2)
		db.session.add(u3)
		db.session.add(u4)
		db.session.commit()
		# check the followed posts of each user
		f1 = u1.followed_posts().all()
		f2 = u2.followed_posts().all()
		f3 = u3.followed_posts().all()
		f4 = u4.followed_posts().all()
		assert len(f1) == 3
		assert len(f2) == 2
		assert len(f3) == 2
		assert len(f4) == 1
		assert f1 == [p4, p2, p1]
		assert f2 == [p3, p2]
		assert f3 == [p4, p3]
		assert f4 == [p4]