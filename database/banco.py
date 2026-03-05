import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect("clientes.db")
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