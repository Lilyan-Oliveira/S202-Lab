from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        # Estabelece a conexão com o Neo4j usando o driver
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Fecha a conexão com o banco
        self.driver.close()

    def execute_query(self, query, parameters=None):
        # Executa uma consulta no banco de dados e retorna todos os resultados em uma lista
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]  # Coleta todos os registros em uma lista
