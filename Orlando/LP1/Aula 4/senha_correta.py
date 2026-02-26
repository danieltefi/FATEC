senha_usuario = int(input('Digite a senha (3 números): '))
senha_correta = 456

while senha_usuario != senha_correta:
    print('Senha inválida, digite novamente!')
    senha_usuario = int(input('Digite a senha novamente: '))

print('Senha correta! Acesso permitido')