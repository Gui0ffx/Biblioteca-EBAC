from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel


app = FastAPI()


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
def listar_tarefas():
    return {"tarefas": tarefas}

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
