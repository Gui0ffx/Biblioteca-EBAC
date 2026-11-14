from fastapi import FastAPI, HTTPException, Body, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional, Literal
from sqlalchemy import create_engine, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, Session, declarative_base
import secrets

DATABASE_URL = "sqlite:///./tarefas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() #Ativa o modelo de dados para o banco de dados

meu_usuario = "admin" #Teste para autenticação
minha_senha = "admin" #Teste para autenticação  

security = HTTPBasic()
 
class TarefaBd(Base):
    #modelo de dados para o banco de dados
    __tablename__ = "tarefas"
    nome: Mapped[str] = mapped_column(String,primary_key= True, index=True, unique=True)
    descricao: Mapped[str] = mapped_column(String, index=True)
    concluida: Mapped[bool] = mapped_column(Boolean, default=False) # True para concluída, False para pendente

class TarefaModel(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False  # True para concluída, False para pendente

Base.metadata.create_all(bind=engine) #iniciando o banco de dados

#------------(Funcao para abrir uma sessao)------------#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#------------(Funcao para autenticar um usuario)------------#

def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, meu_usuario)
    is_password_correct = secrets.compare_digest(credentials.password, minha_senha)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401, 
            detail="Usuário ou senha incorretos!",
            headers={"WWW-Authenticate": "Basic"}
            )

#------------(Instancia do FastAPI)------------#

app = FastAPI(
    title="API de Tarefas",
    description="API para gerenciar Tarefas com autenticação básica",
    version="1.0.0",
    contact={
        "name": "Guilherme Pimenta",
        "email": "guilhermepimenta970@gmail.com"
    },
    dependencies=[Depends(autenticar_usuario)]
)

#------------(Funcao para listar Tarefas)------------#

@app.get("/tarefas", status_code=200)
def listar_tarefas(page: int = 1, size: int = 10, db: Session = Depends(get_db), order_by: Optional[Literal["nome","descricao","concluida"]] = None):
    if page < 1 or size < 1:
        raise HTTPException(
            status_code=400,
            detail="Page ou Size inválidos!"
        )

    query = db.query(TarefaBd)
    if order_by in ["nome", "descricao"]:
        query = query.order_by(func.lower(getattr(TarefaBd, order_by)))
    elif order_by:
        query = query.order_by(getattr(TarefaBd, order_by))

        

    db_tarefas = query.offset((page - 1) * size).limit(size).all()

    if not db_tarefas and page > 1:
        raise HTTPException(
            status_code=404,
            detail="Página não encontrada!"
        )

    db_total_tarefas = db.query(TarefaBd).count()
    return {
        "page": page,
        "size": size,
        "total_tarefas": db_total_tarefas,
        "tarefas": [
            {
                "nome": tarefa.nome,
                "descricao": tarefa.descricao,
                "concluida": tarefa.concluida,
            }
            for tarefa in db_tarefas
        ]
    }

#------------(Funcao para adicionar uma Tarefa)------------#

@app.post("/adicionar", status_code=201)
def criar_tarefa(Tarefa: TarefaModel, db: Session = Depends(get_db)):
    db_tarefa = db.query(TarefaBd).filter(TarefaBd.nome == Tarefa.nome).first()

    if db_tarefa:
        raise HTTPException(status_code=409, detail="Essa Tarefa já existe")

    nova_tarefa = TarefaBd(

        nome=Tarefa.nome,
        descricao=Tarefa.descricao,
        concluida=Tarefa.concluida
    )
    db.add(nova_tarefa)
    db.commit()
    return {"message": f"Tarefa '{Tarefa.nome}' adicionada com sucesso!"}

#------------(Funcao para concluir tarefa)------------#
@app.put("/concluir")
def concluir_tarefa(nome: str = Body(embed=True), db: Session = Depends(get_db)):
    db_tarefa = db.query(TarefaBd).filter(TarefaBd.nome == nome).first()

    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db_tarefa.concluida = True
    db.commit()
    db.refresh(db_tarefa)
    return {"message": f"Tarefa '{db_tarefa.nome}' concluída com sucesso!"}

#------------(Funcao para deletar Tarefas)------------#

@app.delete("/deletar")
def deletar_tarefa(nome: str = Body(embed=True), db: Session = Depends(get_db)):
    db_tarefa = db.query(TarefaBd).filter(TarefaBd.nome == nome).first()

    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db.delete(db_tarefa)
    db.commit()
    return {"message": f"Tarefa '{db_tarefa.nome}' excluída com sucesso!"}