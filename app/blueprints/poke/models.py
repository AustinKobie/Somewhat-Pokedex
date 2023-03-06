from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import ForeignKey

@login.user_loader
def load_user(id):
    return User.query.get(id)

pokedex = db.Table('pokedex',
                   db.Column('id', db.Integer, db.ForeignKey('user.id')),
                   db.Column('poke_id', db.Integer, db.ForeignKey('pokemon.id'))    
                   
                   )


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=True) 
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    pokemon = db.relationship('Pokemon', secondary=pokedex ,backref='pokedex', lazy='dynamic')
    
    
    def __repr__(self):
        return f'<User: {self.name}>'
        
    
    def __str__(self):
        return f'User: {self.name}|{self.name}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        
        
    
    
class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=True)
    description = db.Column(db.String(200))
    type_ = db.Column(db.String(40))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    
    def __repr__(self):
        return f'<Pokemon {self.name}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        