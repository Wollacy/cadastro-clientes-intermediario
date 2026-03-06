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

def alterar_cliente(cliente_dict):
    codigo = cliente_dict["codigo"]
    
    # 1. Validação (Regra de negócio principal)
    if not codigo:
        print("❌ Erro: O código do cliente é obrigatório para a alteração.")
        return

    # 2. Persistência (Envia os dados desempacotados para o banco)
    sucesso, mensagem = banco.atualizar_cliente(
        codigo, 
        cliente_dict["novo_nome"], 
        cliente_dict["rua"], 
        cliente_dict["numero"], 
        cliente_dict["cidade"]
    )

    # 3. Exibição / Interface
    if sucesso:
        print(f"✅ Sucesso: {mensagem}")
    else:
        print(f"⚠️ Erro: {mensagem}")

# Função para remover um cliente e seu endereço correspondente
def remover_cliente(codigo):
    # 1. Validação (Regra de Negócio)
    if not codigo.strip():
        print("❌ Erro: O código do cliente não pode estar vazio.")
        return

    # 2. Persistência (Pede para o banco tentar deletar)
    sucesso = banco.deletar_cliente(codigo)

    # 3. Exibição / Interface
    if sucesso:
        print(f"✅ Cliente {codigo} removido com sucesso!")
    else:
        print(f"⚠️ Erro: Cliente com código {codigo} não encontrado no sistema.")

def buscar_cliente(termo):
    # 1. Validação
    if not termo.strip():
        print("❌ Erro: O termo de busca não pode estar vazio.")
        return

    # 2. Persistência (Pega os dados crus lá do banco)
    clientes = banco.buscar_cliente(termo)

    # 3. Exibição / Interface
    if clientes:
        print("\n🔍 Clientes encontrados:")
        for codigo, nome, rua, numero, cidade in clientes:
            endereco = f"{rua}, {numero} - {cidade}" if rua else "Sem endereço cadastrado"
            print(f"Código: {codigo} - Nome: {nome} - Endereço: {endereco}")
    else:
        print(f"⚠️ Nenhum cliente encontrado com o termo: '{termo}'.")