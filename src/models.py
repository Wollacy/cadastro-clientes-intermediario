class Cliente:
   # O método __init__ é o nosso "fabricante". Ele constrói o objeto quando é chamado.
   def __init__(self, codigo, nome, rua=None, numero=None, cidade=None):
       # O 'self' representa o próprio objeto sendo criado.
       # Aqui definimos os ATRIBUTOS (as características do cliente)
       self.codigo = codigo
       self.nome = nome
       self.rua = rua
       self.numero = numero
       self.cidade = cidade

   # Este é um MÉTODO (um comportamento). O próprio cliente sabe dizer se tem endereço!
   def possui_endereco(self):
       return bool(self.rua and self.numero and self.cidade)
 