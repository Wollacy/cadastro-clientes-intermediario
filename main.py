from database import banco
from src import funcoes

def exibir_menu():
   """Função auxiliar apenas para imprimir as opções na tela."""
   print("\n" + "="*20)
   print("   MENU INICIAL")
   print("="*20)
   print("1. Cadastrar cliente")
   print("2. Listar clientes")
   print("3. Alterar cliente")
   print("4. Remover cliente")
   print("5. Buscar cliente")
   print("0. Sair")
   print("="*20)

def main():
    """Ponto de entrada principal do sistema."""
    # Garante que as tabelas existam antes de iniciar
    banco.criar_tabelas()

    # Menu interativo
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("\nCadastrar Cliente\n")
                novo_cliente = { 
                   "codigo": input("Digite o código do cliente: ").strip(), 
                   "nome": input("Digite o nome do cliente: ").strip(), 
                   "rua": None, 
                   "numero": None, 
                   "cidade": None 
                } 
                endereco_opcional = input("Deseja cadastrar o endereço? (S/N): ").strip().upper()

                if endereco_opcional == "S": 
                   novo_cliente["rua"] = input("Digite o nome da rua: ").strip() 
                   novo_cliente["numero"] = input("Digite o número: ").strip() 
                   novo_cliente["cidade"] = input("Digite a cidade: ").strip() 
 
                # Agora enviamos APENAS UMA variável: a entidade cliente inteira 
                funcoes.cadastrar_cliente(novo_cliente)
            
            case "2":
                print("\nListar Clientes\n")
                funcoes.listar_clientes()
            
            case "3":
                print("\n[ Alterar Cliente ]")
                
                # 1. Montamos o "pacote" (dicionário) base do cliente
                cliente_alterado = {
                    "codigo": input("Digite o código do cliente que deseja alterar: ").strip(),
                    "novo_nome": input("Digite o novo nome do cliente: ").strip(),
                    "rua": None,
                    "numero": None,
                    "cidade": None
                }

                alterar_endereco = input("Deseja alterar o endereço? (S/N): ").strip().upper()

                # 2. Preenchemos o endereço apenas se o usuário quiser
                if alterar_endereco == "S":
                    cliente_alterado["rua"] = input("Digite o novo nome da rua: ").strip()
                    cliente_alterado["numero"] = input("Digite o novo número: ").strip()
                    cliente_alterado["cidade"] = input("Digite a nova cidade: ").strip()

                # 3. Enviamos o dicionário inteiro para a camada de regras!
                funcoes.alterar_cliente(cliente_alterado)

            case "4":
                print("\nRemover Cliente\n")
                codigo = input("Digite o código do cliente que deseja remover: ")
                funcoes.remover_cliente(codigo)

            case "5":
                print("\nBuscar Cliente\n")
                termo = input("Digite o código ou nome do cliente: ")
                funcoes.buscar_cliente(termo)

            case "0":
                print("\nSaindo do sistema. Até mais!\n")
                break

            case _:
                print("\nA opção escolhida não existe. Por favor, tente novamente.")

if __name__ == "__main__":
   main()