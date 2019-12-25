#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(120), unique=True, nullable=False)
    joined = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
