# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# profile

class ProfileForm(FlaskForm):
    username = StringField('Username',
                         id='username_profile',
                         validators=[DataRequired()])
    username2 = StringField('Username2',
                         id='username2_profile',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_profile',
                      validators=[DataRequired(), Email()])
    firstN = StringField('Firstname',
                             id='firstN_profile',
                             validators=[])
    lastN = StringField('Lastname',
                             id='lastN_profile',
                             validators=[])
