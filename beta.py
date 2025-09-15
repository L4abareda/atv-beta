import mysql.connector

conexao=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="sistema"
)

cursor=conexao.cursor()

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastro(self, cursor, conexao):
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (self.email,))

        if cursor.fetchone():
            print("Já existe um usuário com este email.")
            return
        
        cursor.execute(
        "INSERT INTO usuario(nome, email, senha) VALUES (%s, %s, %s)",  (self.nome, self.email, self.senha))

        conexao.commit()
        print(f"{self.nome} cadastrado com sucesso")

    def login(self,cursor):
        cursor.execute(
            "SELECT nome FROM usuario WHERE email = %s AND senha = %s",
            (self.nome, self.senha)
        )
        resultado = cursor.fetchone()
        if resultado:
            nome_real = resultado[0]
            print(f"Bem vindo(a) {nome_real}.")
            return True

        else:
            print("E-mail ou senha incorretos")
            return False
        
while True:
    print("/n===MENU===")
    print("1 - Cadastrar usuário.")
    print("2 - Fazer login.")
    print("3 - Sair")
    opcao = input("Insira uma opcao de 1 a 3: ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = int(input("Digite sua senha: "))
        usuario = Usuario(nome, email, senha)
        usuario.cadastro(cursor, conexao)
    
    elif opcao == '2':
        email = input("Digite seu email: ")
        senha = int(input("Digite sua senha: "))
        usuario = Usuario("", email, senha)
        usuario.login(cursor)

    elif opcao == '3':
        cursor.close()
        conexao.close()
        print("Encerrando sistema...")
        break

    else:
        print("Opcao invalida.")


