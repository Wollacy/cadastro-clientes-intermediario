import banco
import funcoes

banco.criar_tabelas()

# Menu interativo
while True:
    funcoes.exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        funcoes.fluxo_cadastrar_cliente()

    elif opcao == "2":
        print("\nListar Clientes\n")
        funcoes.listar_clientes()

    elif opcao == "3":
        funcoes.fluxo_alterar_cliente()

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
