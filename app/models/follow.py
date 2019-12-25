#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db


class Follower(db.Model):
    __tablename__ = "followers"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeingKey('user.id'))
    user = db.relationship('User', foreing_keys=['user_id'])
    follower = db.relationship('User', foreing_keys=['follower_id'])

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.id

