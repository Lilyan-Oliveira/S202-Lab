from database import Database
from helper.writeAJson import writeAJson

db = Database(database="Relatório3-MongoDBpt2", collection="Pokemons")
# db.resetDatabase()

def getPokemonByCandyType(candy_type: str):
    return db.collection.find({"candy": candy_type})

pikachu_candy_pokemons = getPokemonByCandyType("Pikachu Candy")
writeAJson(pikachu_candy_pokemons, "PikachuCandyPokemons")
