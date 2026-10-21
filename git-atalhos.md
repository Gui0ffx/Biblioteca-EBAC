# Atalhos e comandos úteis do Git

Este guia reúne os principais comandos do Git em um formato simples para facilitar o uso no dia a dia.

## 1) Iniciar um repositório

- `git init` — cria um repositório Git na pasta atual.
- `git clone <url>` — copia um repositório remoto para o computador.

## 2) Verificar e preparar alterações

- `git status` — mostra a branch atual e os arquivos modificados.
- `git diff` — mostra as alterações ainda não enviadas para o stage.
- `git add <arquivo>` — adiciona um arquivo específico à área de preparação.
- `git commit -m "<mensagem>"` — salva as alterações preparadas em um commit.
- `git reset <arquivo>` — remove um arquivo do stage, sem apagar as alterações do arquivo.
- `git rm <arquivo>` — remove o arquivo do projeto e prepara a exclusão para o próximo commit.

## 3) Trabalhar com branches

- `git branch ` — lista as branches locais e marca a branch atual.
- `git checkout <branch>` — troca para a branch indicada.
- `git checkout -b <branch>` — cria uma nova branch e entra nela imediatamente.
- `git merge <branch>` — junta as alterações da branch indicada na branch atual.
- `git rebase <branch>` — reaplica os commits da branch atual sobre a branch indicada.

## 4) Sincronizar com o repositório remoto

- `git remote -v` — lista os repositórios remotos configurados.
- `git remote add <nome> <url>` — adiciona um repositório remoto ao projeto.
- `git fetch <nome>` — busca atualizações do remoto sem aplicá-las localmente.
- `git pull <nome> <branch>` — busca e incorpora as alterações do remoto na branch atual.
- `git push` — envia os commits locais para o repositório remoto.

## 5) Histórico e commits

- `git log` — mostra o histórico de commits.
- `git show <tag>` — exibe detalhes de uma tag ou de um commit específico.
- `git cherry-pick <commit>` — aplica um commit específico em outra branch.
- `git revert <commit>` — cria um novo commit que desfaz as alterações de um commit anterior.

## 6) Guardar alterações temporariamente (stash)


O comando `stash` é útil quando você precisa guardar mudanças sem fazer commit.

- `git stash` — guarda as alterações locais e limpa o diretório de trabalho.
- `git stash list` — lista todos os stashes salvos.
- `git stash show <stash>` — mostra as alterações de um stash, por exemplo `stash@{0}`.
- `git stash apply <stash>` — reaplica um stash sem removê-lo da lista.
- `git stash pop` — reaplica o stash mais recente e o remove da lista se funcionar.
- `git stash drop <stash>` — remove um stash específico.
- `git stash clear` — remove todos os stashes salvos.

## 7) Trabalhar com tags

- `git tag <nome>` — cria uma tag no ponto atual do repositório.
- `git show <tag>` — mostra detalhes da tag e do commit relacionado.

## 8) Remover arquivos não rastreados

Os comandos `git clean` removem arquivos que o Git não está rastreando. Antes de remover, use `git clean -n` para visualizar o que será apagado.

- `git clean -n` — mostra uma simulação do que seria removido.
- `git clean -f` — remove arquivos não rastreados.
- `git clean -fd` — remove também diretórios não rastreados.
- `git clean -fx` — remove também arquivos ignorados pelo Git.
- `git clean -fdx` — remove arquivos, diretórios e itens ignorados.

## Dica prática

Uma sequência comum no fluxo diário é:

1. `git status`
2. `git add <arquivo>`
3. `git commit -m "<mensagem>"`
4. `git push`

Isso ajuda a manter o projeto organizado e facilita a revisão das mudanças.
