import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
session = sessionmaker(bind=MEU_BANCO)
session = session()

# Criando tabela.

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"

    # Definindo campos da tabela.
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    #Definindo atibutos da classe.
    def __init__(selt, nome:str, email:str, senha:str):
        selt.nome = nome
        selt.email = email
        selt.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)  

# Salva no banco dados.
os.system("cls || clear")

# Create
print("Solicitando dados para o usuario")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu e-mail: ")
inserir_senha = input("digite seu senha: ")

usuario = Usuario(nome="Maria", email="maria@gamil.com", senha="456")
session.add(usuario)
session.commit()

# Listando todos os usuarios do banco de dados.
print("|nExibindo todos os usuario do banco de dados.")
lista_usuario = session.query(Usuario).all()

# Read
for usuario in lista_usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

# Delete
print("\nExcluindo um usuario.")
email_usuario = input("Informe o email do usuario para ser excluindo: ")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print(f"{usuario.nome} excluido com sucesso.")

# Listando todos os usuarios do banco de dados.
print("|nExibindo todos os usuario do banco de dados.")
lista_usuario = session.query(Usuario).all()

# Read
for usuario in lista_usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

#Update
print("\nAtualizando dados do usuario.")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()

novos_dados = usuario(
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite seu senha: ")
)

usuario = novos_dados
session.add(usuario)
session.commit()


# Fechando conexão.    
session.close()