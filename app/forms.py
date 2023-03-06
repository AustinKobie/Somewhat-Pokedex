from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    
class SignInForms(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('password', message="Passwords must match")])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
class PostForms(FlaskForm):
    postblock = StringField('Post', validators=[DataRequired()])
    submit = SubmitField('Post')
    
    