from . import bp as main_bp
from flask import render_template

@main_bp.route('/')
def index():
    
    return render_template('index.jinja', title='Home')

@main_bp.route('/')
def about():
    return render_template('home.jinja')
