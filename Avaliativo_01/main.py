from database import Database
from motoristaCLI import MotoristaCLI
from motoristaDAO import MotoristaDAO

# Conectar ao banco de dados e à coleção de motoristas
db = Database(database="SistemaCorridas", collection="Motoristas")

# Resetar o banco de dados e inserir os dados iniciais
# db.resetDatabase()

motorista_dao = MotoristaDAO(db)
cli = MotoristaCLI(motorista_dao)
cli.menu()