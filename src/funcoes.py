from database import banco

# Função para cadastrar um cliente e opcionalmente seu endereço
def cadastrar_cliente(cliente):
   # 1. Regra de Negócio: Validação dos campos obrigatórios
   if not cliente["codigo"]:
       print("❌ Erro: O código do cliente não pode estar vazio.")
       return
   if not cliente["nome"]:
       print("❌ Erro: O nome do cliente não pode estar vazio.")
       return
   
   # 2. Persistência: Passamos a bola para o banco.py fazer o trabalho sujo de SQL
   sucesso, mensagem = banco.inserir_cliente(cliente)

   # 3. Retorno visual para o usuário
   if sucesso:
       print(f"✅ Sucesso: {mensagem} ({cliente['nome']})")
   else:
       print(f"⚠️ {mensagem}")

# Função para listar clientes com seus endereços (se houver)
def listar_clientes(): 
   # Pede os dados crus para a camada de banco 
   clientes = banco.listar_todos_clientes() 
    
   # Regra de negócio: O que fazer se não houver clientes? 
   if not clientes: 
       print("Nenhum cliente cadastrado.") 
       return 
 
   # Formatação e Exibição 
   print("\nLista de Clientes:") 
   for codigo, nome, rua, numero, cidade in clientes: 
       endereco = f"{rua}, {numero} - {cidade}" if rua else "Sem endereço cadastrado" 
       print(f"Código: {codigo} - Nome: {nome} - Endereço: {endereco}")

def alterar_cliente(codigo, novo_nome=None, rua=None, numero=None, cidade=None):
    conexao = banco.conectar()
    cursor = conexao.cursor()

    # Buscar o cliente pelo código
    cursor.execute("SELECT codigo, nome FROM clientes WHERE codigo = ?", (codigo,))
    cliente = cursor.fetchone()

    if not cliente:
        print(f"Erro: Cliente com código {codigo} não encontrado.")
        conexao.close()
        return

    cliente_codigo, nome_atual = cliente

    # Se o usuário não digitou um novo nome, mantém o nome atual
    novo_nome = novo_nome.strip() if novo_nome and novo_nome.strip() else nome_atual

    cursor.execute("UPDATE clientes SET nome = ? WHERE codigo = ?", (novo_nome, codigo))

    # Atualizar ou inserir endereço, se fornecido
    if rua or numero or cidade:
        cursor.execute("SELECT id FROM enderecos WHERE cliente_codigo = ?", (cliente_codigo,))
        endereco = cursor.fetchone()

        if endereco:
            # Atualiza apenas os campos fornecidos
            cursor.execute("""
                UPDATE enderecos 
                SET rua = COALESCE(?, rua), 
                    numero = COALESCE(?, numero), 
                    cidade = COALESCE(?, cidade) 
                WHERE cliente_codigo = ?
            """, (rua, numero, cidade, cliente_codigo))
        else:
            # Insere um novo endereço apenas se todos os campos forem fornecidos
            if rua and numero and cidade:
                cursor.execute("""
                    INSERT INTO enderecos (cliente_codigo, rua, numero, cidade) 
                    VALUES (?, ?, ?, ?)
                """, (cliente_codigo, rua, numero, cidade))
            else:
                print("Aviso: Para cadastrar um novo endereço, todos os campos (rua, numero, cidade) devem ser fornecidos.")

    conexao.commit()
    print(f"Cliente {codigo} atualizado para {novo_nome} com sucesso!")

    conexao.close()

# Função para remover um cliente e seu endereço correspondente
def remover_cliente(codigo):
    conexao = banco.conectar()
    cursor = conexao.cursor()
    
    # Remover o endereço antes do cliente para evitar erro de integridade
    cursor.execute("DELETE FROM enderecos WHERE cliente_codigo = ?", (codigo,))
    cursor.execute("DELETE FROM clientes WHERE codigo = ?", (codigo,))
    
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Cliente {codigo} removido com sucesso!")
    else:
        print(f"Erro: Cliente com código {codigo} não encontrado.")

    conexao.close()

# Função para buscar clientes pelo código ou nome
def buscar_cliente(termo):
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT c.codigo, c.nome, e.rua, e.numero, e.cidade 
        FROM clientes c 
        LEFT JOIN enderecos e ON c.codigo = e.cliente_codigo
        WHERE c.codigo = ? OR c.nome LIKE ?
    """, (termo, f"%{termo}%"))
    
    clientes = cursor.fetchall()
    conexao.close()

    if clientes:
        print("\nClientes encontrados:")
        for codigo, nome, rua, numero, cidade in clientes:
            endereco = f"{rua}, {numero} - {cidade}" if rua else "Sem endereço cadastrado"
            print(f"Código: {codigo} - Nome: {nome} - Endereço: {endereco}")
    else:
        print(f"Nenhum cliente encontrado com o termo: {termo}.")