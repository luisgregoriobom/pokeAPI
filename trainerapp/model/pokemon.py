from database.db import db

class Pokemons(db.Model):
    __tablename__ = 'trainer_pokemon'
    trainer_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, primary_key=True, nullable=False)

    def __init__(self, name, level, pokemon_id, trainer_id):
        self.trainer_id = trainer_id
        self.name = name
        self.level = level
        self.pokemon_id = pokemon_id