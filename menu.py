from beta import cursor, conexao

print("===MENU===")
print("1 - Cadastrar usuário.")
print("2 - Fazer login.")
print("3 - Sair")
opcao = int(input("Insira uma opcao de 1 a 3: "))

while opcao != 3:
    if opcao == 1:
        nome = input()
