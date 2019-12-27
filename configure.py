#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'storage.db')}"
SECRET_KEY = r'4d0f58ca6423f3b21577d7af4db4e526'
