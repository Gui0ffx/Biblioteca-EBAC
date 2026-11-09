<div align="center">

# 📚 Biblioteca EBAC

**Projeto principal do curso de Back-end da EBAC.**<br>
Exercícios de Python, do terminal à primeira API.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20estudo-F2B705)

</div>

---

## 🗂️ O que tem aqui

| Arquivo | O que é |
|---|---|
| [`biblioteca.py`](biblioteca.py) | Sistema de biblioteca no terminal: cadastro de livros, estoque e empréstimos |
| [`app.py`](app.py) | API de tarefas com FastAPI: criar, listar, concluir e excluir |
| [`git-atalhos.md`](git-atalhos.md) | Guia rápido dos comandos de Git usados no dia a dia |

---

## 📖 Sistema de biblioteca (terminal)

Programa de menu no terminal para controlar o acervo e os empréstimos de uma biblioteca.

```text
1 - Adicionar livro
2 - Listar livros
3 - Remover livro
4 - Atualizar quantidade livro
5 - Registrar empréstimo
6 - Histórico de empréstimos
7 - Sair
Escolha uma opção:
```

**Funcionalidades**
- **Cadastro de livros** com título, autor e quantidade. Títulos e autores são padronizados em MAIÚSCULAS, e títulos repetidos não são aceitos.
- **Listagem em ordem alfabética**, com autor e quantidade disponível.
- **Remoção e atualização de estoque** de um livro já cadastrado.
- **Empréstimos** que descontam do estoque e bloqueiam pedidos acima do disponível.
- **Histórico** de todos os empréstimos feitos na sessão.
- **Validação de entrada:** campos vazios, números inválidos e quantidades zero ou negativas mostram uma mensagem de erro no lugar da linha digitada, sem poluir a tela.

**Como executar**

```bash
python biblioteca.py
```

> [!NOTE]
> Os dados ficam em memória: ao sair do programa, livros e empréstimos são apagados.

---

## ✅ API de tarefas (FastAPI)

API REST simples para gerenciar uma lista de tarefas, guardada em uma lista de dicionários em memória.

**Como executar**

```bash
pip install fastapi uvicorn
uvicorn app:app --reload
```

Com o servidor no ar, abra **http://127.0.0.1:8000/docs** para testar tudo pelo navegador (Swagger).

**Rotas**

| Método | Rota | Corpo (JSON) | O que faz |
|---|---|---|---|
| `GET` | `/tarefas` | — | Lista todas as tarefas |
| `POST` | `/adicionar` | `{"nome": "...", "descricao": "..."}` | Cria uma tarefa (retorna **409** se o nome já existir) |
| `PUT` | `/concluir` | `{"nome": "..."}` | Marca a tarefa como concluída (**404** se não existir) |
| `DELETE` | `/deletar` | `{"nome": "..."}` | Exclui a tarefa (**404** se não existir) |

**Exemplo**

```bash
curl -X POST http://127.0.0.1:8000/adicionar \
  -H "Content-Type: application/json" \
  -d '{"nome": "estudar", "descricao": "revisar FastAPI"}'
```

```json
{ "message": "Tarefa criada com sucesso!" }
```

---

<div align="center">
<br>
<sub>Feito por <a href="https://github.com/Gui0ffx">Gui0ffx</a> durante o curso de Back-end da <b>EBAC</b></sub>
</div>
