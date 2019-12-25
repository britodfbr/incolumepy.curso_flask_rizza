#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'))
    user = db.relationship('User', foreing_keys=['user_id'])

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.id

