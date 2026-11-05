from fastapi import FastAPI, HTTPException, Body, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional, Literal
import secrets

meu_usuario = "admin" #Teste para autenticação
minha_senha = "admin" #Teste para autenticação

security = HTTPBasic()

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
    description="API para gerenciar tarefas com autenticação básica",
    version="1.0.0",
    contact={
        "name": "Guilherme Pimenta",
        "email": "guilhermepimenta970@gmail.com"
    },
    dependencies=[Depends(autenticar_usuario)]
)

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False

tarefas: list[Tarefa] = []


#------------(Funcao para buscar e validar se uma tarefa existe)------------#

def buscar_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa.nome == nome:
            return tarefa
    return None

#------------(Funcao para listar tarefas)------------#

@app.get("/tarefas")
def listar_tarefas(page: int = 1, size: int = 10, order_by: Optional[Literal["nome", "descricao"]] = None):
    lista_tarefas = tarefas

    if page < 1 or size < 1:
        raise HTTPException(
            status_code=400,
            detail="Page ou Size inválidos!"
        )

    if order_by:
        lista_tarefas = sorted(tarefas, key=lambda x: getattr(x, order_by).lower())

    start = (page - 1) * size
    end = start + size

    no_tarefas = len(tarefas)
    if start >= no_tarefas and page > 1:
        raise HTTPException(
            status_code=404,
            detail="Página não encontrada"
        )

    tarefas_paginadas = lista_tarefas[start:end]
    return{
        "page": page,
        "size": size,
        "total_tarefas": len(tarefas),
        "tarefas": tarefas_paginadas
    }
#------------(Funcao para adicionar uma tarefa)------------#

@app.post("/adicionar", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    if buscar_tarefa(tarefa.nome):
        raise HTTPException(status_code=409, detail="Essa tarefa já existe") 
    tarefas.append(tarefa)
    return {"message": "Tarefa criada com sucesso!"}
    
#------------(Funcao para concluir tarefa)------------#

@app.put("/concluir")
def concluir_tarefa(nome: str = Body(embed=True)):
    tarefa = buscar_tarefa(nome)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
  
    tarefa.concluida = True
    return {"message": f"Tarefa '{nome}' marcada como concluída com sucesso!"}

#------------(Funcao para deletar tarefas)------------#

@app.delete("/deletar")
def deletar_tarefa(nome: str = Body(embed=True)):
    tarefa = buscar_tarefa(nome)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
         
    tarefas.remove(tarefa)
    return {"message": f"Tarefa '{nome}' excluída com sucesso!"}
