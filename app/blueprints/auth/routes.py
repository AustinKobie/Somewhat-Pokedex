from . import bp as auth_bp
from app.forms import RegisterForm, SignInForms
from app.blueprints.poke.models import User
from flask import render_template, redirect, flash
from flask_login import login_user, logout_user, login_required

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        password=form.password.data
        u = User(name=name, email=email, password_hash='')
        user_match = User.query.filter_by(name=name).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {name} already exists, try again')
            return redirect('/signup')
        elif email_match:
            flash(f'Email {email} already exists, try again')
            return redirect('/signup')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {name} succesful')
            return redirect('/')
        
    return render_template('signup.jinja', form=form)

@auth_bp.route('/signin', methods=['GET','POST'])
def signin():
    form = SignInForms()
    if form.validate_on_submit():
        name=form.name.data
        password=form.password.data
        user_match=User.query.filter_by(name=name).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or Password was incorrect, try again')
            return redirect('/signin')
        flash(f'{name} successfully signed in!')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')
    return render_template('signin.jinja', signin_form=form)

@auth_bp.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')

