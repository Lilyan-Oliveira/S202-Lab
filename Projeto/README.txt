O projeto é um sistema de gerenciamento de personagens da Terra Média, inspirado no universo de O Senhor dos Anéis. Ele utiliza o banco de dados Neo4j, que permite representar e gerenciar as relações entre personagens de forma gráfica, capturando a riqueza de conexões do mundo criado por J.R.R. Tolkien.

O sistema permite realizar operações de CRUD (Create, Read, Update, Delete) nos personagens, organizados em diferentes raças (Elfos, Humanos, Magos, Hobbits e Anões). Além disso, inclui funcionalidades que simulam ações dos personagens no universo da Terra Média, como "observar" o que cada raça está fazendo com base em comportamentos típicos.
--------------------------------------------------------------------------------------------------------------------------------------------------------
Gerenciamento de Personagens:

Criar: Adicionar novos personagens, definindo atributos como nome, idade, habilidade e raça. Dependendo da raça, características adicionais podem ser incluídas, como:
Magos: Cor do robe.
Anões: Ferramenta usada para minerar.
Hobbits: Livro preferido.

Ler: Listar todos os personagens, agrupando-os por raça.

Atualizar: Alterar qualquer atributo de um personagem existente.

Deletar: Remover personagens do banco de dados.
--------------------------------------------------------------------------------------------------------------------------------------------------------
Observar a Terra Média:

Ação especial que exibe uma mensagem personalizada para cada raça, destacando seus comportamentos típicos e listando os personagens envolvidos. Por exemplo:
"Os hobbits Frodo e Sam estão festejando."
"O mago Gandalf está executando algum poder."
"Os anões Gimli e Thorin estão minerando."
--------------------------------------------------------------------------------------------------------------------------------------------------------
Conceitos Utilizados

Programação Orientada a Objetos (POO):

Classes e Objetos: Cada personagem é representado como um objeto, encapsulando suas propriedades (atributos) e comportamentos (métodos).

Herança: As diferentes raças (Elfo, Humano, Hobbit, etc.) herdam de uma classe base Character, compartilhando atributos e comportamentos comuns, mas com suas próprias características.

Polimorfismo: As raças têm métodos específicos que se comportam de forma diferente. Por exemplo, "festejar" é exclusivo dos Hobbits e "mineirar" dos Anões.

Encapsulamento: Atributos e métodos são protegidos, garantindo que alterações sejam feitas apenas por meio de métodos controlados.

Banco de Dados Neo4j:

Modelo de Grafo: Representação de personagens como nós e seus relacionamentos (amizades, alianças, etc.) como arestas.
Cypher Query Language: Linguagem usada para realizar operações no banco, como criar personagens e relacionamentos ou buscar informações.
--------------------------------------------------------------------------------------------------------------------------------------------------------
Estrutura do Código

main.py:
Gerencia o fluxo principal do programa.
Exibe o menu e chama as funções correspondentes da classe CharacterCRUD.

database.py:
Gerencia a conexão com o banco de dados Neo4j.
Fornece métodos para abrir e fechar conexões, além de executar consultas.

character_crud.py:
Contém a lógica de CRUD para gerenciar os personagens.
Inclui métodos específicos para cada operação.

Banco de Dados (Neo4j):
Armazena os personagens e seus relacionamentos.