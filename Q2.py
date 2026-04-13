# 2. Faça um programa que leia um nome de usuário
# e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.


nome_usu = input('Insira seu nome: ')
senha_usu = input('Insira sua senha: ')
while senha_usu == nome_usu:
    print('Erro, tente novamente')
    nome_usu = input('Insira seu nome: ')
    senha_usu = input('Insira sua senha: ')

print('usuário cadastrado!')
