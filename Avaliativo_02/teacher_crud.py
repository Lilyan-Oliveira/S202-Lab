class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' created successfully.")

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]
        else:
            print(f"Teacher '{name}' not found.")
            return None

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf RETURN t"
        parameters = {"name": name, "newCpf": newCpf}
        result = self.db.execute_query(query, parameters)
        if result:
            print(f"Teacher '{name}' updated successfully.")
        else:
            print(f"Teacher '{name}' not found.")

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' deleted successfully.")
