import sqlite3
 
# Função centralizada para conectar ao banco 
def conectar():
   """Retorna uma conexão com o banco de dados SQLite."""
   return sqlite3.connect("database/clientes.db")

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    # Cria a tabela de clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)

    # Cria a tabela de endereços
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enderecos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_codigo TEXT,
            rua TEXT NOT NULL,
            numero TEXT NOT NULL,
            cidade TEXT NOT NULL,
            FOREIGN KEY (cliente_codigo) REFERENCES clientes (codigo)
        )
    """)

    conexao.commit()
    conexao.close()

def inserir_cliente(cliente):
   """Insere um novo cliente e seu endereço no banco de dados."""
   conexao = conectar()
   cursor = conexao.cursor()

   try:
       # Insere na tabela clientes
       cursor.execute(
           "INSERT INTO clientes (codigo, nome) VALUES (?, ?)",
           (cliente["codigo"], cliente["nome"])
       )

       # Insere na tabela enderecos se houver dados
       if cliente["rua"] and cliente["numero"] and cliente["cidade"]:
           cursor.execute(
               "INSERT INTO enderecos (cliente_codigo, rua, numero, cidade) VALUES (?, ?, ?, ?)",
               (cliente["codigo"], cliente["rua"], cliente["numero"], cliente["cidade"])
           )

       conexao.commit()
       return True, "Cliente cadastrado com sucesso no banco de dados."
   
   except sqlite3.IntegrityError:
       return False, "Erro: Já existe um cliente com esse código no banco."
   finally:
       conexao.close()
 
def listar_todos_clientes():
   """Busca e retorna todos os clientes do banco."""
   conexao = conectar()
   cursor = conexao.cursor()
   cursor.execute("""
       SELECT c.codigo, c.nome, e.rua, e.numero, e.cidade
       FROM clientes c
       LEFT JOIN enderecos e ON c.codigo = e.cliente_codigo
   """)
   clientes = cursor.fetchall()
   conexao.close()
   
   return clientes # Retorna os dados crus (lista de tuplas)