import mysql.connector

conexao=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="sistema"
)

cursor=conexao.cursor()

class Usuario:
    def __init__(self, nome, email, ids, senha):
        self.nome = nome
        self.email = email
        self.ids = ids
        self.senha = senha

    def cadastro(self, cursor, conexao):
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (self.email))
        if cursor.fetchone():
            print("Já existe um usuário com este email.")
            return
        
        cursor.execute 
        ("INSERT INTO usuarios(nome, email, senha) VALUES (%s, %s, %s)", 
        (self.nome, self.email, self.senha)
        )

        conexao.commit()
        print(f"{self.nome} cadastrado com sucesso")

    def login(self,cursor):
        cursor.execute(
            "SELECT nome FROM usuarios WHERE email = %s AND senha = %s",
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