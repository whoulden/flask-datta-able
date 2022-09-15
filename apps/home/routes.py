# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps import db, login_manager
from apps.home.forms import ProfileForm
from flask import render_template, request
from flask_login import (current_user, login_required)
from jinja2 import TemplateNotFound
from apps.authentication.models import Users
from apps.home.models import Experiment, Dashboard

@blueprint.route('/index')
@login_required
def index():
    dashboard = Dashboard()
    dashboard.calc()
    dashboard.exs = '3'
    last_exp = Experiment.query.filter_by(key='ai19-zh-360t').first()
    all_exp = Experiment.query.all()
    return render_template('home/index.html', dash=dashboard, last_experiment=last_exp, all_experiments=all_exp, segment='index')

@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile_form = ProfileForm(request.form)

    if 'firstN' in request.form:

        username = profile_form.username
        email = profile_form.email
        lastN = profile_form.lastN
        firstN = profile_form.firstN

        user = Users.query.filter_by(username=current_user.username).first()
        i = user.id

        user.lastname = lastN.data
        user.firstname = firstN.data

        Users.save(user)

        return render_template('home/profile.html',
                               msg='User updated successfully.',
                               success=True,
                               form=profile_form)

    else:
        return render_template('home/profile.html', form=profile_form)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


