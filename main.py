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
print("Solicitando dados para o usuario")
usuario = Usuario(nome="Marta", email="marta@gamil.com", senha="123")
session.add(usuario)
session.commit()

usuario = Usuario(nome="Maria", email="maria@gamil.com", senha="456")
session.add(usuario)
session.commit()

# Listando todos os usuarios do banco de dados.
print("|nExibindo todos os usuario do banco de dados.")
lista_usuario = session.query(Usuario).all()

for usuario in lista_usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

# Fechando conexão.    
session.close()