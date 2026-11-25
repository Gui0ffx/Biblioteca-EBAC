<div align="center">

# 📚 Biblioteca EBAC

**Projeto principal do curso de Back-end da EBAC.**<br>
Exercícios de Python, do terminal à primeira API.

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20estudo-F2B705)

</div>

---

## 🗂️ O que tem aqui

| Arquivo | O que é |
|---|---|
| [`biblioteca.py`](biblioteca.py) | Sistema de biblioteca no terminal: cadastro de livros, estoque e empréstimos |
| [`app.py`](app.py) | API de tarefas com FastAPI: criar, listar, concluir e excluir |
| [`Dockerfile`](Dockerfile) | Receita da imagem: instala o Poetry e as dependências e define como a API é iniciada |
| [`docker-compose.yml`](docker-compose.yml) | Sobe o container da API com porta, volume e variáveis de ambiente configurados |
| [`pyproject.toml`](pyproject.toml) | Configuração do projeto e lista de dependências (Poetry) |
| [`poetry.lock`](poetry.lock) | Versões exatas de cada dependência, para todo mundo instalar exatamente as mesmas |
| [`.env.example`](.env.example) | Modelo das variáveis de ambiente (copie para `.env`) |

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

API REST simples para gerenciar uma lista de tarefas, guardada em SQLite

Para rodar, siga a seção [🐳 Rodando com Docker](#-rodando-com-docker). Com o servidor no ar, abra **http://localhost:8000/docs** para testar tudo pelo navegador (Swagger).

**Senha**
```bash
usuario: admin
senha: admin
```

**Rotas**

| Método | Rota | Corpo (JSON) | O que faz |
|---|---|---|---|
| `GET` | `/tarefas` | — | Lista todas as tarefas |
| `POST` | `/adicionar` | `{"nome": "...", "descricao": "..."}` | Cria uma tarefa (retorna **409** se o nome já existir) |
| `PUT` | `/concluir` | `{"nome": "..."}` | Marca a tarefa como concluída (**404** se não existir) |
| `DELETE` | `/deletar` | `{"nome": "..."}` | Exclui a tarefa (**404** se não existir) |

**Exemplo**

```bash
curl -X POST http://localhost:8000/adicionar \
  -H "Content-Type: application/json" \
  -d '{"nome": "estudar", "descricao": "revisar FastAPI"}'
```

```json
{ "message": "Tarefa criada com sucesso!" }
```

---

## 🐳 Rodando com Docker

O Docker sobe a **API de tarefas** num container, com todas as dependências já instaladas. Você **não precisa** ter Python nem Poetry na sua máquina.

> [!TIP]
> Usa Podman? Troque `docker` por `podman` nos comandos: `podman compose up --build -d`

### 1. Pré-requisitos

Você só precisa do **Docker** com o **Docker Compose**. Confira no terminal:

```bash
docker --version          # confere o Docker
docker compose version    # confere o Docker Compose
```

### 2. Clonar o repositório

```bash
git clone https://github.com/Gui0ffx/Biblioteca-EBAC
cd Biblioteca-EBAC
```

### 3. Criar o arquivo de variáveis de ambiente

```bash
cp .env.example .env      # Linux / macOS
copy .env.example .env    # Windows
```

### 4. Construir e subir

```bash
docker-compose up --build -d
```

| Parte do comando | O que faz |
|---|---|
| `up` | Sobe os containers |
| `--build` | (Re)constrói a imagem a partir do Dockerfile |
| `-d` | (de *detached*) Roda em segundo plano e libera o terminal |

### 5. Conferir se está rodando

```bash
docker-compose ps         # lista os containers e o status de cada um
docker-compose logs -f    # mostra os logs da API ao vivo (saia com Ctrl+C; o container continua rodando)
```

### 6. Acessar

- API: [http://localhost:8000](http://localhost:8000)
- Documentação interativa (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)

### 7. Parar

```bash
docker-compose down
```

> [!TIP]
> Se o `docker-compose` (com hífen) der "comando não encontrado", use `docker compose` (com espaço), que é a versão nova. Os dois funcionam igual!

### ⚙️ Configuração do container

| O quê | Valor | Para quê |
|---|---|---|
| Porta | `8000:8000` | A porta 8000 do container fica acessível na porta 8000 do seu computador |
| Volume | `.:/app` | Sincroniza a pasta do projeto com a pasta `/app` do container |
| `PYTHONUNBUFFERED` | `1` | Faz os `print` e os logs aparecerem na hora no `docker-compose logs` |
| `.env` | arquivo | Variáveis extras da aplicação (veja o modelo em `.env.example`) |

### 🔁 Recarregamento automático

Graças ao volume, o código da sua máquina é o mesmo que está dentro do container. Com o `--reload` do uvicorn, a API reinicia sozinha sempre que você salva um arquivo, sem precisar reconstruir a imagem.

Só é preciso rodar `docker-compose up --build -d` de novo quando você **muda as dependências** (o `pyproject.toml`).

### 🧰 Extras úteis

| Comando | O que faz |
|---|---|
| `docker-compose restart` | Reinicia sem reconstruir |
| `docker-compose up --build -d` | Reconstrói depois de mudar o `pyproject.toml` (dependência nova) |
| `docker-compose exec app bash` | Entra dentro do container (se der erro, troque `bash` por `sh`) |
| `docker-compose down -v` | Para e apaga também os volumes nomeados (cuidado: os dados de banco somem!) |

---

## 🛠️ Rodando sem Docker (opcional)

Para rodar direto na sua máquina, você precisa do **Python 3.14** e do **Poetry**:

```bash
poetry install --no-root
poetry run uvicorn app:app --reload
```

Editor usado no projeto: VS Code, com o Poetry configurado como gerenciador de ambiente (`.vscode/settings.json`).

<div align="center">
<br>
<sub>Feito por <a href="https://github.com/Gui0ffx">Gui0ffx</a> durante o curso de Back-end da <b>EBAC</b></sub>
</div>