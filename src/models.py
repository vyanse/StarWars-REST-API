from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    personajes_fav = db.relationship("FavoriteCharacters", backref="user")
    favorite_planets = db.relationship("FavoritePlanets", backref="user")
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    __tablename__ ='personajes'
    id = db.column(db.Integer,primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    favorite_characters = db.()
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

class Planets(db.Model):
    __tablename__ ='planetas'
    id =db.Column(db.Integer,primary_key-True)
    name = db.column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    favorite_planet_id = db.column(db.Integer, db.Foreignkey('planetsfavorite'))
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

class favoriteCharacters(db.Model):
    __tablename__ = 'personajes_favoritos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'))
    Characters = db.relationship("Characters", backref="favorite")
    # character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    
    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
        }

class FavoritePlanets(db.Model):
    __tablename__ = 'planeta_favorito'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'))
    # planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet =db.relationship("Planets", backref= "favorites")
 

    def serialize(self):
        return{
            "id": self.id,
            "user_id":  self.user_id,
            "planet_id": self.planet_id,
        }

