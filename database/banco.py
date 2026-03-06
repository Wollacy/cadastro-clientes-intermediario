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
   """Insere um objeto Cliente e seu endereço no banco de dados.""" 
   conexao = conectar() 
   cursor = conexao.cursor() 
    
   try: 
       # Acessamos os dados usando a sintaxe de objeto (ponto) 
       cursor.execute( 
           "INSERT INTO clientes (codigo, nome) VALUES (?, ?)",  
           (cliente.codigo, cliente.nome) 
       ) 
        
       # Usamos a "inteligência" do objeto para saber se ele tem endereço! 
       if cliente.possui_endereco(): 
           cursor.execute( 
               "INSERT INTO enderecos (cliente_codigo, rua, numero, cidade) VALUES (?, ?, ?, ?)",  
               (cliente.codigo, cliente.rua, cliente.numero, cliente.cidade) 
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

def deletar_cliente(codigo):
    """Remove um cliente e seu endereço do banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Remover o endereço antes do cliente para evitar erro de integridade no banco
    cursor.execute("DELETE FROM enderecos WHERE cliente_codigo = ?", (codigo,))
    cursor.execute("DELETE FROM clientes WHERE codigo = ?", (codigo,))
    
    # O rowcount nos diz quantas linhas foram apagadas
    linhas_afetadas = cursor.rowcount 
    
    conexao.commit()
    conexao.close()

    # Se apagou 1 ou mais linhas, retorna True (sucesso). Se apagou 0, retorna False.
    return linhas_afetadas > 0

def buscar_cliente(termo):
    """Busca clientes por código ou parte do nome e retorna os dados brutos."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
        SELECT c.codigo, c.nome, e.rua, e.numero, e.cidade 
        FROM clientes c 
        LEFT JOIN enderecos e ON c.codigo = e.cliente_codigo
        WHERE c.codigo = ? OR c.nome LIKE ?
    """, (termo, f"%{termo}%"))
    
    clientes = cursor.fetchall()
    conexao.close()

    # Retorna a lista de tuplas (vazia se não achar ninguém, ou com os dados se achar)
    return clientes

def atualizar_cliente(codigo, novo_nome, rua, numero, cidade):
    """Atualiza os dados de um cliente e seu endereço no banco."""
    conexao = conectar()
    cursor = conexao.cursor()

    # 1. Verifica se o cliente existe e pega o nome atual
    cursor.execute("SELECT codigo, nome FROM clientes WHERE codigo = ?", (codigo,))
    cliente = cursor.fetchone()

    if not cliente:
        conexao.close()
        return False, f"Cliente com código {codigo} não encontrado."

    nome_atual = cliente[1]
    # Se não passou nome novo, mantém o antigo
    nome_final = novo_nome if novo_nome else nome_atual

    # Atualiza o nome na tabela clientes
    cursor.execute("UPDATE clientes SET nome = ? WHERE codigo = ?", (nome_final, codigo))

    # 2. Lógica do endereço
    if rua or numero or cidade:
        cursor.execute("SELECT id FROM enderecos WHERE cliente_codigo = ?", (codigo,))
        endereco = cursor.fetchone()

        if endereco:
            # Já tem endereço, então atualiza (usando COALESCE para ignorar os vazios)
            cursor.execute("""
                UPDATE enderecos 
                SET rua = COALESCE(?, rua), 
                    numero = COALESCE(?, numero), 
                    cidade = COALESCE(?, cidade) 
                WHERE cliente_codigo = ?
            """, (rua, numero, cidade, codigo))
        else:
            # Não tem endereço, tenta inserir um novo
            if rua and numero and cidade:
                cursor.execute("""
                    INSERT INTO enderecos (cliente_codigo, rua, numero, cidade) 
                    VALUES (?, ?, ?, ?)
                """, (codigo, rua, numero, cidade))
            else:
                conexao.close()
                return False, "Para cadastrar um novo endereço, todos os campos (rua, num, cid) devem ser fornecidos."

    conexao.commit()
    conexao.close()
    
    return True, f"Cliente {codigo} atualizado com sucesso!"