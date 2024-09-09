from database import Database
from modelBooks import BookModel
from cli import BookCLI

# Conecte ao banco de dados e à coleção de livros
db = Database(database="Relatório5-MongoDBpt4", collection="Livros")
bookModel = BookModel(database=db)

# Inicia a interface de linha de comando para interagir com os livros
bookCLI = BookCLI(bookModel)
bookCLI.run()
