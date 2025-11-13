from humano import Pessoa
from val import validar_email, validar_telefone, validar_cpf, validar_data_nascimento
from banco import criar_tabela, inserir_usuario, listar_usuarios, editar_usuario, remover_usuario, reativar_usuario, exportar_excel

def main():
    criar_tabela()

    while True:
        print('\n' + '='*40)
        print('        SISTEMA DE CLIENTES')
        print('='*40)
        print('1 - Listar clientes')
        print('2 - Cadastrar novo cliente')
        print('3 - Editar cliente')
        print('4 - Remover cliente')
        print('5 - Exportar clientes para Excel')
        print('6 - Sair')

        abertura = input('Escolha uma opção: ')

        if abertura == '1':
            usuarios = listar_usuarios()
            print(f'\n Clientes cadastrados: ({len(usuarios)})')
            for u in usuarios:
                status = 'Ativo' if u[6] == 1 else 'Inativo'
                print(f'ID: {u[0]} | Nome: {u[1]} | Email: {u[2]} | Telefone: {u[3]} | CPF: {u[4]} | Data de Nascimento: {u[5]} | Status: {status}')
            
        elif abertura == '2':
        
            while True:
                nome = input('Digite seu nome: ')

                while True:
                    email = input('Digite seu email: ')
                    if validar_email(email):
                        break
                    else:
                        print('Email inválido! Insira um E-mail válido. ')

                while True:
                    telefone = input('Digite seu número de telefone: ')
                    if validar_telefone(telefone):
                        break
                    else:
                        print('Número de telefone inválido! Digite um número válido.')
                
                while True:
                    cpf = input('Digite seu CPF: ')
                    if validar_cpf(cpf):
                        break
                    else:
                        print('CPF inválido! Digite um CPF válido. ')
                
                while True:
                    data_nascimento = input('Digite sua data de nascimento(dd/mm/aaaa): ')
                    if validar_data_nascimento(data_nascimento):
                        break
                    else:
                        print('Data de nascimento inválida! Digite uma data de nascimento válida!')
                

                usuario = Pessoa(name = nome, email = email, phone = telefone, cpf = cpf, data_nascimento = data_nascimento)
                print('Cliente cadastrado com sucesso!!!')
                print('\n', usuario)
                    
                resultado = inserir_usuario(nome, email, telefone, cpf, data_nascimento)
                print(resultado)

                usuarios = listar_usuarios()

                print(f'\nA lista de clientes cadastrados: Total de {len(usuarios)}')
                for u in usuarios:
                    status = 'Ativo' if u[6] == 1 else 'Inativo'
                    print(f'ID: {u[0]} | Nome: {u[1]} | Email: {u[2]} | Telefone: {u[3]} | CPF: {u[4]} | Data de Nascimento: {u[5]} | Status: {status}')

                ask1 = input('\n 1. Deseja adicionar outro cliente na lista? \n 2. Sair \n ')
                if(ask1 == '2'):
                    print('Voltando ao menu principal')
                    break
                
                print(f'A lista de clientes cadastrados: Total de {len(usuarios)}')
                for u in usuarios:
                    print(u)

        elif abertura == '3':
            print('\n1. Editar informações de um cliente existente')
            print('\n2. Editar status de atividade de um clientes inativo')
            ask2 = input('Escolha uma opção: ')
            if ask2 == '1':
                editar_usuario()
            elif ask2 == '2':
                reativar_usuario()
            else:
                print('Opção inválida! Selecione uma opção válida')
        
        elif abertura == '4':
            remover_usuario()

        elif abertura == '5':
            exportar_excel()

        elif abertura == '6':
            print('Programa encerrado!')
            break

        else:
            print('Resposta inválida! Digite uma resposta válida!')

if __name__ == '__main__':
    main()
