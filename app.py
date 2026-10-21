from fastapi import FastAPI, HTTPException

app = FastAPI()

tarefas = []

#------------(Funcao para validar se uma tarefa existe)------------#

def validar_tarefa(nome_tarefa: str):
    for tarefa in tarefas:
        if tarefa["nome_tarefa"] == nome_tarefa:
            return tarefa
    return None

#------------(Funcao para listar tarefas)------------#

@app.get("/tarefas")
def get_tarefas():
    return {"tarefas": tarefas}

#------------(Funcao para adicionar uma tarefa)------------#

@app.post("/adicionar")
def post_tarefa(nome_tarefa: str, descricao_tarefa: str, tarefa_concluida: bool = False):

    if validar_tarefa(nome_tarefa):
        raise HTTPException(status_code=409, detail="Essa tarefa já existe")
  
    tarefas.append({"nome_tarefa": nome_tarefa, "descricao_tarefa": descricao_tarefa, "tarefa_concluida": tarefa_concluida})
    return{"message": "Tarefa criada com sucesso!"}
    
#------------(Funcao para concluir tarefa)------------#

@app.put("/concluir/{nome_tarefa}")
def put_concluir(nome_tarefa: str):
    tarefa = validar_tarefa(nome_tarefa)

    if tarefa:
        tarefa["tarefa_concluida"] = True
        return {"message": f"Tarefa '{nome_tarefa}' marcada como concluída com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    

#------------(Funcao para deletar tarefas)------------#

@app.delete("/deletar-tarefa/{nome_tarefa}")
def delete_tarefa(nome_tarefa: str):
    tarefa = validar_tarefa(nome_tarefa)

    if tarefa:
        tarefas.remove(tarefa)
        return {"message": f"Tarefa '{nome_tarefa}' excluída com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
