from database import Database
from save_json import writeAJson


class Pokedex:
    def __init__(self, db_name, collection_name):
        self.db = Database(db_name, collection_name)

    def get_pokemons_by_type(self, types):
        pokemons = self.db.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemons_by_type")

    def get_pokemon_by_id(self, pokemon_id):
        pokemons =  self.db.collection.find_one({'id': pokemon_id})
        writeAJson(pokemons, "get_pokemon_by_id")

    def get_all_pokemons(self):
        pokemons = list(self.db.collection.find())
        writeAJson(pokemons, "get_all_pokemons")


    def get_pokemon_by_name(self, name):
        response = self.db.collection.find_one({'name.english': name})
        writeAJson(response, "get_pokemon_by_name")

    def get_pokemon_by_HP(self, base):
        pokemons = self.db.collection.find_one({'base.HP': base})
        writeAJson(pokemons, "get_pokemon_by_HP")

