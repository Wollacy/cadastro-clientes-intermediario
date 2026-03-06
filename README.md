# 🚀 Sistema de Gestão de Clientes (CRUD) - Arquitetura em 3 Camadas 
 
Este é um projeto desenvolvido em Python focado em boas práticas de Engenharia de Software, utilizando Arquitetura em 3 Camadas, Programação Orientada a Objetos (POO) e persistência de dados com SQLite. 
 
## 🎯 O Projeto 
 
O sistema é uma aplicação de terminal interativa que permite gerenciar o cadastro de clientes e seus endereços, garantindo a integridade dos dados e a fácil exportação de relatórios. O maior foco deste projeto não é apenas "fazer funcionar", mas sim demonstrar um código limpo, escalável e de fácil manutenção. 
 
## 🛠️ Tecnologias e Conceitos Aplicados 
 
- **Python 3.10+**: Utilização de recursos modernos como `match/case`. 
- **SQLite3**: Banco de dados relacional nativo. 
- **Arquitetura em 3 Camadas**: Separação estrita entre Interface (`main.py`), Regras de Negócio (`funcoes.py`) e Persistência de Dados (`banco.py`). 
- **Programação Orientada a Objetos (POO)**: Uso da classe `Cliente` para encapsular dados e comportamentos. 
- **Tratamento de Exceções**: Blocos `try/except/finally` para blindar a aplicação contra falhas de banco de dados e interrupções do usuário. 
- **Exportação de Dados**: Geração automática de relatórios em formato `.csv` utilizando a biblioteca nativa `csv`. 
- **Boas Práticas**: Código formatado com *Black Formatter* e proteção de dados sensíveis com `.gitignore`. 
 
## 📁 Estrutura do Projeto 
 
O código foi refatorado para seguir padrões de mercado, abandonando o modelo de script único e adotando pastas modulares: 
 
* `main.py` -> Ponto de entrada e menu interativo. 
* `/src/funcoes.py` -> Regras de negócio e validações. 
* `/src/models.py` -> Definição da Classe Cliente. 
* `/database/banco.py` -> Conexão centralizada e queries SQL. 
 
## 🚀 Como Executar 
 

Clone o repositório: 
	git clone https://github.com/SEU-USUARIO/cadastro-clientes-intermediario.git 

 

Acesse a pasta do projeto: 
	cd cadastro-clientes-intermediario 
 

Execute o sistema: 
	python main.py

👨‍💻 Autor: Wollacy Willyan de Carvalho
- E-mail: [carvalho_1990@outlook.com](mailto:carvalho_1990@outlook.com)  
- LinkedIn: [Wollacy](https://www.linkedin.com/in/wollacycarvalho/)
- Instagram: [Wollacy](https://www.instagram.com/wollacywcarvalho/)
