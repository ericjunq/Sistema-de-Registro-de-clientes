import re
from email_validator import validate_email, EmailNotValidError
from datetime import datetime

def validar_email(email):
    try:
        valid = validate_email(email)
        return True
    except EmailNotValidError:
        return False

def limpar_numeros(texto):
    return re.sub(r'\D', '', texto)

def validar_cpf(cpf):
    cpf_limpo = re.sub(r'\D', '', cpf)
    return len(cpf_limpo) == 11

def validar_idade(idade):
    if idade.isdigit():
        idade_num = int(idade)
        return 0 < idade_num < 120
    return False

def validar_telefone(telefone):
    telefone_limpo = limpar_numeros(telefone)
    return telefone_limpo.isdigit() and len(telefone_limpo) == 11

def validar_data_nascimento(date_str):
    try:
        data = datetime.strptime(date_str, "%d/%m/%Y")
        if data > datetime.now():
            print('Data de nascimento inválida! Digite uma data de nascimento válida!')
            return False

        idade = (datetime.now() - data).days /365
        if idade > 120:
            print('Idade inválida! Verifique a data informada!')
            return False
        return True
      
    except ValueError:
        return False

def normalizar_cpf(cpf):
    return limpar_numeros(cpf)

def normalizar_telefone(telefone):
    return limpar_numeros(telefone)
