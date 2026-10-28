# Sistema de gerenciamento de biblioteca

# Autor: Guilherme
# Data: 2026-09-10
# Versão: 1.8

#------------(Local para adicionar bibliotecas)------------#
import os
import time

#------------(Inicialização das estruturas de dados)------------#

livros = {}
emprestimos = []

#------------(Função para mostrar erros)------------#

def mostrar_erro(mensagem, segundos=2):
    print("\033[1A\033[2K", end="")  # apaga a linha que o usuário digitou
    print(mensagem)                  # mostra o erro no lugar dela
    time.sleep(segundos)             # deixa o erro visível
    print("\033[1A\033[2K", end="")  # apaga o erro; o prompt volta nessa linha

#------------(Função para exibir o menu principal)------------#

def exibir_menu(): 
    
    return(
        "1 - Adicionar livro \n"
        "2 - Listar livros \n"
        "3 - Remover livro \n"
        "4 - Atualizar quantidade livro \n"
        "5 - Registrar empréstimo \n"
        "6 - Histórico de empréstimos \n"
        "7 - Sair \n"
        "Escolha uma opção: "
        )
        
#------------(Função para adicionar um livro)------------#

def adicionar_livro(): #função que adiciona um livro ao sistema
    os.system("cls" if os.name == "nt" else "clear")
    while True:
 
        titulo = input("Título: ").strip().upper() 
        if not titulo: 
            mostrar_erro("Erro: O título não pode estar vazio.")

            continue
        elif titulo in livros:
            mostrar_erro("Erro: Este livro já está cadastrado.")
            return
        break    
    while True:

        autor = input("Autor: ").strip().upper()
        if not autor:
            mostrar_erro("Erro: O autor não pode estar vazio.")
            continue
        break

    while True:

        try:
            quantidade = int(input("Quantidade: "))
            if not quantidade:
                mostrar_erro("Erro: A quantidade não pode ser zero.")
                continue
        except ValueError:
            mostrar_erro("Erro: A quantidade deve ser um número inteiro.")  
            continue

        if quantidade <= 0:
            mostrar_erro("Erro: A quantidade deve ser maior que zero.")
            continue
        break
    
    os.system("cls" if os.name == "nt" else "clear")
    livros[titulo] = {"autor": autor, "quantidade": quantidade}
    print(f"Livro '{titulo}' adicionado com sucesso.\n")
    print("Pressione Enter para continuar...")
    input()
    os.system("cls" if os.name == "nt" else "clear")

#------------(Função para listar todos os livros cadastrados)------------#

def listar_livros():

    os.system("cls" if os.name == "nt" else "clear")
    while True:
        if not livros:
            print("Nenhum livro cadastrado.")
            print("Pressione Enter para continuar...")
            input()
            break
        for titulo, info in sorted(livros.items()):
            print(f"Título: {titulo} - Autor: {info['autor']} - Quantidade: {info['quantidade']}\n")
        print("Pressione Enter para continuar...")
        input()
        break
  

#------------(Função para remover um livro)------------#

def remover_livro(): 

    os.system("cls" if os.name == "nt" else "clear")
    while True:
        titulo = input("Título: ").strip().upper()
        if not titulo: 
            mostrar_erro("Erro: O título não pode estar vazio.")
            continue
        if titulo not in livros:
            mostrar_erro("Erro: Este livro não existe.")
            continue
        del livros[titulo]
        print(f"Livro '{titulo}' removido com sucesso.")
        print("Pressione Enter para continuar...")
        input()
        break
#------------(Função para atualizar a quantidade de um livro)------------#

def atualizar_quantidade(): 

    os.system("cls" if os.name == "nt" else "clear")
    while True:

        titulo = input("Título: ").strip().upper()
        if not titulo:
            mostrar_erro("Erro: O título não pode estar vazio.")
            continue
        if titulo not in livros:
            mostrar_erro("Erro: Livro não encontrado.")
            continue
        break
    while True:
        try:
            quantidade = int(input("Quantidade: "))
            
            if not quantidade:
                mostrar_erro("Erro: A quantidade não pode ser zero.")
                continue        
            if quantidade <= 0:
                mostrar_erro("Erro: A quantidade deve ser maior que zero.")
                continue
        except ValueError:
            mostrar_erro("Erro: A quantidade deve ser um número inteiro.")  
            continue
        break
    livros[titulo]["quantidade"] = quantidade
    print(f"Quantidade do livro '{titulo}' atualizada com sucesso.")
    print("Pressione Enter para continuar...")
    input()

#------------(Função para registrar um empréstimo de um livro)------------#

def registrar_emprestimo(): 

    os.system("cls" if os.name == "nt" else "clear")
    while True:

        titulo = input("Título: ").strip().upper() 
        if not titulo: 
            mostrar_erro("Erro: O título não pode estar vazio.")
            continue
        if titulo not in livros:
            mostrar_erro("Erro: Livro não encontrado.")
            continue
        break

    while True:

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade > livros[titulo]["quantidade"]:
                mostrar_erro("Erro: Quantidade indisponível.")
                continue
        except ValueError:
                mostrar_erro("Erro: A quantidade deve ser um número inteiro.")  
                continue

        if quantidade <= 0:
            mostrar_erro("Erro: A quantidade deve ser maior que zero.")
            continue
        break
    
    os.system("cls" if os.name == "nt" else "clear")
    emprestimos.append({"titulo": titulo, "autor": livros[titulo]["autor"], "quantidade": quantidade})
    livros[titulo]["quantidade"] -= quantidade
    print(f"Emprestimo do livro '{titulo}' realizado com sucesso.\n")
    print("\nPressione Enter para continuar...")
    input()
    os.system("cls" if os.name == "nt" else "clear")

#------------(Função para exibir o log de todos os empréstimos registrados)------------#

def log_emprestimos(): 

    os.system("cls" if os.name == "nt" else "clear")
    while True:
        if not emprestimos:
            print("Nenhum livro emprestado.")
            print("Pressione Enter para continuar...")
            input()
            break
        for titulo, autor, quantidade in ([(e["titulo"], e["autor"], e["quantidade"]) for e in emprestimos]):
            print(f"Título: {titulo} - Autor: {autor} - Quantidade: {quantidade}\n")
        print("Pressione Enter para continuar...")
        input()
        break

#------------(Função para sair do sistema)------------#

def sair():

    print("Saindo do sistema...")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    exit()

#------------(Função principal do sistema)------------#

def main(): 

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try: 
            opcao = int(input(exibir_menu())) 
            if opcao < 1 or opcao > 7:
                mostrar_erro("Erro: opção inválida.")
                continue

        except ValueError:
            mostrar_erro("Erro: opção inválida.")
            continue

        
#------------(Controle da opcao 1 (Adicionar livros))------------#      
        if opcao == 1:
            adicionar_livro()
            
            
#------------(Controle da opcao 2 (Listar livros))------------#

        if opcao == 2:
            listar_livros()
            
    
#------------(Controle da opcao 3 (Remover livros))------------#

        if opcao == 3:
            remover_livro()
               
#------------(Controle da opcao 4 (Atualizar livros))------------#

        if opcao == 4:
            atualizar_quantidade()
            
#------------(Controle da opcao 5 (Registrar emprestimo))------------#

        if opcao == 5:
            registrar_emprestimo()

#------------(Controle da opcao 6 (Exibir log de emprestimos))------------#

        if opcao == 6:
            log_emprestimos()
            
#------------(Controle da opcao 7 (Sair do sistema))------------#

        if opcao == 7:
            sair()
    
if __name__ == "__main__":
    main()
