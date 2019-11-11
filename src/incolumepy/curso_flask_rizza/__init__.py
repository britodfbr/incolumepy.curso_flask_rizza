#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
__package__ = 'incolumepy.curso_flask_rizza'
file_version = 'version.txt'
with open(os.path.join(os.path.dirname(__file__), file_version)) as file:
    __version__ = file.read().strip()
