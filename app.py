from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

tarefas = []

#------------(Funcao para validar se uma tarefa existe)------------#

def validar_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            return tarefa
    return None

#------------(Funcao para listar tarefas)------------#

@app.get("/tarefas")
def get_tarefas():
    return {"tarefas": tarefas}

#------------(Funcao para adicionar uma tarefa)------------#

@app.post("/adicionar")
def post_tarefa(nome: str = Body(embed=True), descricao: str = Body(embed=True)):
    concluida = False
    if validar_tarefa(nome):
        raise HTTPException(status_code=409, detail="Essa tarefa já existe")
  
    tarefas.append({"nome": nome, "descricao": descricao, "concluida": concluida})
    return {"message": "Tarefa criada com sucesso!"}
    
#------------(Funcao para concluir tarefa)------------#

@app.put("/concluir")
def put_concluir(nome: str = Body(embed=True)):
    tarefa = validar_tarefa(nome)
    
    if tarefa:
        tarefa["concluida"] = True
        return {"message": f"Tarefa '{nome}' marcada como concluída com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    

#------------(Funcao para deletar tarefas)------------#

@app.delete("/delete")
def delete_tarefa(nome: str = Body(embed=True)):
    tarefa = validar_tarefa(nome)

    if tarefa:
        del tarefas[tarefas.index(tarefa)]
        return {"message": f"Tarefa '{nome}' excluída com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
