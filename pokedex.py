from database import Database
from save_json import writeAJson


class Pokedex:
    def __init__(self, db_name, collection_name):
        self.db = Database(db_name, collection_name)

    def get_pokemons_by_type(self, types):
        pokemons = self.db.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemons_by_type")

    def get_pokemon_by_id(self, pokemon_id):
        response =  self.db.collection.find_one({'id': pokemon_id})
        writeAJson(response, "get_pokemon_by_id")

    def get_all_pokemons(self):
        response = list(self.db.collection.find())
        writeAJson(response, "get_all_pokemons")

    def get_pokemons_by_weakness(self, weaknesses):
        pokemons = self.db.collection.find({"weaknesses": {"$in": weaknesses}})
        writeAJson(pokemons, "pokemons_by_weakness.json")

    def get_pokemons_by_candy(self, candy_amount):
        pokemons = self.db.collection.find({"candy_count": {"$lte": candy_amount}})
        writeAJson(pokemons, "pokemons_by_candy.json")

