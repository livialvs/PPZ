usuário = input('Usuário: ')
senha = input('Senha: ')
while usuário == senha:
    print('Erro: usuário e senha não podem ser iguais. Tente novamente.')
    usuário = input('Usuário: ')
    senha = input('Senha: ')
    
