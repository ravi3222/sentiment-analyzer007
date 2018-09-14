#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Class definition for text web form

Created on Mon Apr 24 11:44:44 2017

@author: Mashimo
"""

from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField
from wtforms.validators import DataRequired

class InputTextForm(FlaskForm):
    inputText = TextAreaField(validators=[DataRequired()])
    ignoreCase = BooleanField('ignore case', default=True)
    ignoreStopWords = BooleanField('ignore stopwords', default=True)