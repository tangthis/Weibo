#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# 发送邮件
from flask.ext.email import Message
from app import mail

def send_email(subject,sender,recipients,text_body,html_body):
    msg = Message(subject,sender,recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)