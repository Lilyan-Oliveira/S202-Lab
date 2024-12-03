from queries import *
class CharacterCRUD:
    def __init__(self, db):
        self.db = db
    
    def create_character(self, name, age, skill, race, additional_info=None):
        query = """
        CREATE (c:Character {name: $name, age: $age, skill: $skill, race: $race, extra_info: $additional_info})
        """
        self.db.execute_query(query, {
        "name": name,
        "age": age,
        "skill": skill,
        "race": race,
        "additional_info": additional_info
    })

    def get_all_characters(self):
        query = get_all_characters_query()
        result = self.db.execute_query(query)
        return result  # Não é mais necessário usar list(), pois o resultado já é uma lista

    def get_character_by_name(self, name):
        query = get_character_by_name_query()
        result = self.db.execute_query(query, {"name": name})
        return result  # Também já retorna uma lista aqui
    
    def update_character(self, name, attribute, value):
    # Constrói dinamicamente a consulta com o atributo
        query = f"""
        MATCH (c:Character {{name: $name}})
        SET c.{attribute} = $value
        RETURN c
        """
        return self.db.execute_query(query, {"name": name, "value": value})


    def delete_character(self, name):
        query = delete_character_query()
        return self.db.execute_query(query, {"name": name})
