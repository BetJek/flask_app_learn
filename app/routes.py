# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse

@login_required
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'miguel'}
    posts = [
        {
            'author' : {'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author' : {'username':'Susan'},
            'body': 'Avengers so cool!'
        },
        {
            'author' : {'username':'Ипполит'},
            'body': 'Гадость ваша рыба'
        },
    ]
    return render_template("index.html", title='Home Page', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))