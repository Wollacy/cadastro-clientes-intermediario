import banco
import funcoes

banco.criar_tabelas()

# Menu interativo
while True:
    funcoes.exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nCadastrar Cliente\n")
        codigo = input("Digite o código do cliente: ")
        nome = input("Digite o nome do cliente: ")
        endereco_opcional = input("Deseja cadastrar o endereço? (S/N): ").strip().upper()

        if endereco_opcional == "S":
            rua = input("Digite o nome da rua: ")
            numero = input("Digite o número: ")
            cidade = input("Digite a cidade: ")
            funcoes.cadastrar_cliente(codigo, nome, rua, numero, cidade)
        else:
            funcoes.cadastrar_cliente(codigo, nome)

    elif opcao == "2":
        print("\nListar Clientes\n")
        funcoes.listar_clientes()

    elif opcao == "3":
        print("\nAlterar Cliente\n")
        codigo = input("Digite o código do cliente que deseja alterar: ")
        novo_nome = input("Digite o novo nome do cliente: ")
        alterar_endereco = input("Deseja alterar o endereço? (S/N): ").strip().upper()

        if alterar_endereco == "S":
            rua = input("Digite o novo nome da rua: ")
            numero = input("Digite o novo número: ")
            cidade = input("Digite a nova cidade: ")
            funcoes.alterar_cliente(codigo, novo_nome, rua, numero, cidade)
        else:
            funcoes.alterar_cliente(codigo, novo_nome)

    elif opcao == "4":
        print("\nRemover Cliente\n")
        codigo = input("Digite o código do cliente que deseja remover: ")
        funcoes.remover_cliente(codigo)

    elif opcao == "5":
        print("\nBuscar Cliente\n")
        termo = input("Digite o código ou nome do cliente: ")
        funcoes.buscar_cliente(termo)

    elif opcao == "0":
        print("\nSaindo do sistema. Até mais!\n")
        break

    else:
        print("\nA opção escolhida não existe. Por favor, tente novamente.")

    # Eu analisei e compreendi a estrutura do projeto!
