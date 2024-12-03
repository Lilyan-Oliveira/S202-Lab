from database import Database
from character_crud import CharacterCRUD


def main():
    db = Database("bolt://3.234.144.16:7687", "neo4j", "funding-body-azimuth")
    character_crud = CharacterCRUD(db)

    print("\n--- Bem-vindo ao acervo da Terra Média ---")

    while True:
        print("\nO que gostaria de fazer?")
        print("1. Criar personagem")
        print("2. Listar personagens")
        print("3. Buscar personagem")
        print("4. Atualizar personagem")
        print("5. Deletar personagem")
        print("6. Observar a Terra Média")
        print("7. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome do personagem: ")
            age = int(input("Idade do personagem: "))
            skill = input("Habilidade do personagem: ")
            race = input("Raça do personagem (elfo, humano, mago, hobbit, anao): ").lower()

            # Coleta de informações adicionais baseadas na raça
            additional_info = None
            if race == "mago":
                additional_info = input("Escolha a cor do mago: ")
            elif race == "anao":
                additional_info = input("Escolha a ferramenta de mineirar do anão: ")
            elif race == "hobbit":
                additional_info = input("Escolha um livro para o hobbit levar: ")
            elif race == "elfo":
                additional_info = input("Escolha a tribo do elfo: ")
            elif race == "humano":
                additional_info = input("Escolha o reino do humano: ")
            else:
                print("Raça inválida, tente novamente!")
                continue

            character_crud.create_character(name, age, skill, race, additional_info)
            print("Personagem adicionado com sucesso!")

        elif choice == "2":
            characters = character_crud.get_all_characters()
            if characters:
                grouped_characters = {}
                for record in characters:
                    race = record['c']['race']
                    if race not in grouped_characters:
                        grouped_characters[race] = []
                    grouped_characters[race].append(record['c'])

                for race, chars in grouped_characters.items():
                    print(f"\n--- {race.capitalize()}s ---")
                    for char in chars:
                        print(
                            f"Nome: {char['name']}, Idade: {char['age']}, Habilidade: {char['skill']}, Extra: {char.get('extra_info', 'N/A')}"
                        )
            else:
                print("Nenhum personagem encontrado.")

        elif choice == "3":
            name = input("Nome do personagem para buscar: ")
            characters = character_crud.get_character_by_name(name)
            if characters:
                for record in characters:
                    print(
                        f"Nome: {record['c']['name']}, Idade: {record['c']['age']}, Habilidade: {record['c']['skill']}, Raça: {record['c']['race']}, Extra: {record['c'].get('extra_info', 'N/A')}"
                    )
            else:
                print("Personagem não encontrado.")

        elif choice == "4":
            name = input("Nome do personagem para atualizar: ")
            attribute = input("Atributo para atualizar (name, age, skill, race, extra_info): ")
            value = input("Novo valor: ")
            character_crud.update_character(name, attribute, value)
            print("Atributo atualizado!")

        elif choice == "5":
            name = input("Nome do personagem para deletar: ")
            character_crud.delete_character(name)
            print("Personagem deletado com sucesso!")

        elif choice == "6":
            print("\n--- Observando a Terra Média ---")
            characters = character_crud.get_all_characters()
            if characters:
                grouped_characters = {}
                for record in characters:
                    race = record['c']['race']
                    if race not in grouped_characters:
                        grouped_characters[race] = []
                    grouped_characters[race].append(record['c'])

                for race, chars in grouped_characters.items():
                    names = [char['name'] for char in chars]
                    if race == "hobbit":
                        print(f"Os Hobbits {', '.join(names)} estão festejando!")
                    elif race == "anao":
                        print(f"Os Anões {', '.join(names)} estão minerando nas montanhas!")
                    elif race == "mago":
                        print(f"O Mago {', '.join(names)} está conjurando feitiços poderosos!")
                    elif race == "elfo":
                        print(f"Os Elfos {', '.join(names)} estão viajando pelas florestas!")
                    elif race == "humano":
                        print(f"Os Humanos {', '.join(names)} estão cultivando nos campos!")
            else:
                print("Não há personagens para observar na Terra Média.")

        elif choice == "7":
            print("Volte sempre!")
            db.close()
            break

        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    main()

