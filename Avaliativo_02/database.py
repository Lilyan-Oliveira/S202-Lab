from neo4j import GraphDatabase
from querys import Querys

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data

    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

# Inicializa a conexão com o banco de dados
db = Database("bolt://54.208.49.204:7687", "neo4j", "identification-tissue-cupful")
query_instance = Querys(db)

# Questão 1

# 1.a
print("Questão 1")
print(" ")

print("A) Professor Renzo:", query_instance.get_teacher_by_name("Renzo"))
print(" ")

# 1.b
print("B) Professores com nome começando com 'M':", query_instance.get_teachers_by_initial("M"))
print(" ")

# 1.c
print("C) Cidades:", query_instance.get_all_cities())
print(" ")

# 1.d
print("D) Escolas com número entre 150 e 550:", query_instance.get_schools_in_range(150, 550))
print(" ")
# Questão 2

print("Questão 2")
print(" ")

# 2.a
print("A) Ano de nascimento do professor mais jovem e mais velho:", query_instance.get_youngest_and_oldest_teacher_year())
print(" ")

# 2.b
print("B) Média de habitantes das cidades:", query_instance.get_average_city_population())
print(" ")

# 2.c
print("C) Nome da cidade com 'a' substituído por 'A':", query_instance.get_city_name_with_replaced_a("37540-000"))
print(" ")

# 2.d
print("D) Terceiro caractere de cada nome de professor:", query_instance.get_teacher_name_from_third_character())
print(" ")

# Fecha a conexão
db.close()