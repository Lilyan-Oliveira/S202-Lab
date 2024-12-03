# queries.py

# Consulta para criar um personagem
def create_character_query():
    return """
    CREATE (c:Character {name: $name, age: $age, skill: $skill, race: $race})
    RETURN c
    """

# Consulta para obter todos os personagens ordenados por raça
def get_all_characters_query():
    return """
    MATCH (c:Character)
    RETURN c
    ORDER BY c.race
    """

# Consulta para obter um personagem pelo nome
def get_character_by_name_query():
    return """
    MATCH (c:Character {name: $name})
    RETURN c
    """

# Consulta para atualizar um atributo de um personagem
def update_character_query():
    return """
    MATCH (c:Character {name: $name})
    SET c.$attribute = $value
    RETURN c
    """

# Consulta para deletar um personagem pelo nome
def delete_character_query():
    return """
    MATCH (c:Character {name: $name})
    DETACH DELETE c
    """
