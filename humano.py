class Pessoa:
    def __init__(self, name, email, phone, cpf, data_nascimento):
        self.name = name
        self.email = email
        self.phone = phone
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        return f"Pessoa = {self.name}, Email = {self.email}, Telefone = {self.phone}, CPF = {self.cpf}, Data de Nascimento = {self.data_nascimento}"
