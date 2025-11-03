usuario_correto = 'admin'
senha_correta = '12345'

tentativas = 3
while tentativas > 0:
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    
    if usuario == usuario_correto and senha == senha_correta:
        print('Login sucedido')
        break

    else:
        tentativas = tentativas - 1
        print('Usuário e/ou senha incorretos')
        print(f'Você tem mais {tentativas} restantes')

if tentativas == 0:
    print('Acesso bloqueado. Você excedeu o número de tentativas')