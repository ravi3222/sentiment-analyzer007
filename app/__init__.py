#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:47:05 2017

@author: Mashimo
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config') # configuration file


from app import views