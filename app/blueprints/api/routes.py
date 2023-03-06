from . import bp as api_bp
from app.blueprints.poke.models import Pokemon, User

@api_bp.get('/pokemon')
def api_posts():
    result= []
    pokemon = Pokemon.query.all()
    for poke in pokemon:
        result.append({
            'id':poke.id,
            'description':poke.description,
            'timestamp':poke.timestamp,
            'user_id': poke.author
        })
    return result 

@api_bp.route('/pokemon/<id>', methods=['GET'])
def api_post(id):
    poke = Pokemon.query.get(int(id))
    return {
            'id':poke.id,
            'description':poke.description,
            'timestamp':poke.timestamp,
            'user_id': poke.author
    }
    
    
@api_bp.get('/user_pokemon/<name>')
def api_user_posts(username):
    result= []
    user = User.query.filter_by(username=username).first()
    for post in user.posts:
        result.append({
            'id':post.id,
            'description':post.description,
            'timestamp':post.timestamp,
            'user_id': post.author
        })
    return result 

