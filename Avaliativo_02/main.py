from database import Database
from teacher_crud import TeacherCRUD

# Inicializa a conexão com o banco de dados
db = Database("bolt://54.208.49.204:7687", "neo4j", "identification-tissue-cupful")
teacher_crud = TeacherCRUD(db)

def main():
    print("Questão 3")
    print("Escolha a opção: create, read, update, delete, quit")

    while True:
        command = input("\nDigite a opção desejada: ").strip().lower()

        if command == "create":
            name = input("Nome do professor: ").strip()
            ano_nasc = int(input("Ano de nascimento: ").strip())
            cpf = input("CPF: ").strip()
            teacher_crud.create(name, ano_nasc, cpf)

        elif command == "read":
            name = input("Nome do professor a ser lido: ").strip()
            teacher = teacher_crud.read(name)
            if teacher:
                print(f"Name: {teacher['name']}, Year of Birth: {teacher['ano_nasc']}, CPF: {teacher['cpf']}")

        elif command == "update":
            name = input("Nome do professor a ser atualizado: ").strip()
            new_cpf = input("Enter the new CPF: ").strip()
            teacher_crud.update(name, new_cpf)

        elif command == "delete":
            name = input("Nome do professor a ser deletado ").strip()
            teacher_crud.delete(name)

        elif command == "quit":
            print("Até mais!")
            break

        else:
            print("Invalid command. Please try again.")

    # Fecha a conexão com o banco de dados ao finalizar
    db.close()

# Executa o CLI
if __name__ == "__main__":
    main()
