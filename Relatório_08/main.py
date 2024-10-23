from neo4j import GraphDatabase

class Neo4jDriver:
    neo4j_host = "bolt://54.91.186.70:7687"
    neo4j_user = "neo4j"
    neo4j_password = "walks-bureaus-gardens"
    
    driver = None

    @staticmethod
    def get_driver():
        if not Neo4jDriver.driver:
            Neo4jDriver.driver = GraphDatabase.driver(
                Neo4jDriver.neo4j_host, auth=(Neo4jDriver.neo4j_user, Neo4jDriver.neo4j_password)
            )
        return Neo4jDriver.driver


class Player:
    def __init__(self, name, age, skill_level):
        self.name = name
        self.age = age
        self.skill_level = skill_level

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "skill_level": self.skill_level
        }


class Match:
    def __init__(self, player1_name, player2_name, result):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.result = result  # Can be 'player1', 'player2' or 'draw'


class PlayerDAO:
    def __init__(self):
        self.neo4j_driver = Neo4jDriver.get_driver()

    def create_player(self, player: Player):
        with self.neo4j_driver.session() as session:
            session.run(
                """
                CREATE (p:Player {name: $name, age: $age, skill_level: $skill_level})
                """, 
                name=player.name, 
                age=player.age, 
                skill_level=player.skill_level
            )

    def get_player(self, name):
        with self.neo4j_driver.session() as session:
            result = session.run(
                """
                MATCH (p:Player {name: $name})
                RETURN p.name AS name, p.age AS age, p.skill_level AS skill_level
                """, 
                name=name
            )
            return result.single()

    def update_player(self, name, new_age=None, new_skill_level=None):
        with self.neo4j_driver.session() as session:
            query = "MATCH (p:Player {name: $name}) "
            params = {"name": name}
            
            if new_age:
                query += "SET p.age = $age "
                params["age"] = new_age

            if new_skill_level:
                query += "SET p.skill_level = $skill_level "
                params["skill_level"] = new_skill_level

            session.run(query, **params)

    def delete_player(self, name):
        with self.neo4j_driver.session() as session:
            session.run(
                """
                MATCH (p:Player {name: $name})
                DETACH DELETE p
                """, 
                name=name
            )


class MatchDAO:
    def __init__(self):
        self.neo4j_driver = Neo4jDriver.get_driver()

    def create_match(self, match: Match):
        with self.neo4j_driver.session() as session:
            session.run(
                """
                MATCH (p1:Player {name: $player1_name}), (p2:Player {name: $player2_name})
                CREATE (m:Match {result: $result})
                CREATE (p1)-[:PLAYED]->(m)
                CREATE (p2)-[:PLAYED]->(m)
                """,
                player1_name=match.player1_name,
                player2_name=match.player2_name,
                result=match.result
            )

    def get_matches_for_player(self, player_name):
        with self.neo4j_driver.session() as session:
            result = session.run(
                """
                MATCH (p:Player {name: $player_name})-[:PLAYED]->(m:Match)
                RETURN m.result AS result, p.name AS player
                """,
                player_name=player_name
            )
            return [{"result": record["result"]} for record in result]

    def delete_match(self, player1_name, player2_name):
        with self.neo4j_driver.session() as session:
            session.run(
                """
                MATCH (p1:Player {name: $player1_name})-[:PLAYED]->(m:Match)<-[:PLAYED]-(p2:Player {name: $player2_name})
                DETACH DELETE m
                """,
                player1_name=player1_name,
                player2_name=player2_name
            )


# Teste de criação de jogador e partida
player_dao = PlayerDAO()
match_dao = MatchDAO()

# Criação de jogadores
player1 = Player(name="Jogador 1", age=30, skill_level="Intermediário")
player2 = Player(name="Jogador 2", age=25, skill_level="Avançado")

player_dao.create_player(player1)
player_dao.create_player(player2)

# Criação de uma partida
match = Match(player1_name="Jogador 1", player2_name="Jogador 2", result="player1")
match_dao.create_match(match)

# Recuperar informações de uma partida
print(match_dao.get_matches_for_player("Jogador 1"))

# Atualização de jogador
player_dao.update_player(name="Jogador 1", new_age=31)

# Remoção de uma partida
match_dao.delete_match(player1_name="Jogador 1", player2_name="Jogador 2")

# Remoção de jogador
player_dao.delete_player(name="Jogador 1")
