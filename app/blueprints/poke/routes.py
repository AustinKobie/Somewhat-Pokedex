from . import bp as poke_bp
from .models import User, Pokemon
from app.forms import PostForms
from flask import redirect, render_template, url_for
from flask_login import login_required, current_user

@poke_bp.route('/user/<name>')
def user(name):
    user_match = User.query.filter_by(name=name).first()
    if not user_match:
        redirect('/')
    posts = user_match.pokemon
    return render_template('user.jinja', user=user_match, posts=posts)

@poke_bp.route('/pokemon', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForms()
    if form.validate_on_submit():
        body = form.postblock.data
        p = Pokemon(description=body, user_id=current_user.id)
        p.commit()
        return redirect(url_for('poke.user', name=current_user.name))
    return render_template('pokemon.jinja', post_form=form)