# Sistema de gerenciamento de Pokémons

""" 
Autor: Guilherme
Data: 2026-11-20
Versão: 1.0
Python version: 3.14.7
Não necessário nenhuma instalação
Execute na pasta onde esta o arquivo o seguinte comando: python3 pokedex.py ou pyhton pokedex.py no Windows

"""


#importações
import os
import time
import sys
import unicodedata
from enum import Enum

pokedex = {} #armazena os dados

pokebola = [] #apresenta o historico de captura

class TipoPokemon(str,Enum): #Classes aceitas para cadastro de Pokémons

    NORMAL = "NORMAL"
    FOGO = "FOGO"
    AGUA = "AGUA"
    PLANTA = "PLANTA"
    ELETRICO = "ELETRICO"
    GELO = "GELO"
    LUTADOR = "LUTADOR"
    VENENOSO = "VENENOSO"
    TERRESTRE = "TERRESTRE"
    VOADOR = "VOADOR"
    PSIQUICO = "PSIQUICO"
    INSETO = "INSETO"
    PEDRA = "PEDRA"
    FANTASMA = "FANTASMA"
    DRAGAO = "DRAGAO"
    SOMBRIO = "SOMBRIO"
    ACO = "ACO"
    FADA = "FADA"

def voltar_opcoes():#função para voltar para as opções
    print("\nPressione ENTER para continuar...")
    input()
    limpar_terminal()

def remover_acentos(texto): #Função para remover os acentos e não quebrar o código
    return ''.join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))

def ler_texto(pergunta): #Função que recebe a mensagem do usuário e trata os acentos
    resposta = remover_acentos(input(pergunta))
    return resposta.strip().upper()

def ler_nivel(pergunta):
    while True:
        limpar_terminal()
        try:
            nivel = int(input(pergunta))
            if not (1 <= nivel <= 100):
                erro_pokemon("Erro: O nível deve ser um número de 1 a 100!!!")
                continue
        except ValueError:
            erro_pokemon("Erro: O nível do Pokémon deve ser um número inteiro de 1 a 100!!!")
            continue
        break
    return nivel


def limpar_terminal(): #função para limpar o terminal
    os.system("cls" if os.name == "nt" else "clear")
    
def erro_pokemon(mensagem, segundos=2): #funcao para mostrar os erros depois da validação
    print("\033[1A\033[2K", end="") #apaga a linha que o usuário digitou apos apertar ENTER
    print(mensagem) #mostra o erro
    time.sleep(segundos) #timer de 2s
    print("\033[1A\033[2K", end="") #apaga a mensagem

def adicionar_pokemon():#Função para adicionar Pokémons
    limpar_terminal()

    nome = ler_texto("Digite o NOME do Pokémon: ")
    limpar_terminal()
    if not nome:
        erro_pokemon("Erro: O nome do Pokémon não pode ser vazio!!!")
        return
    elif nome in pokedex:
        erro_pokemon("Erro: Pokémon já catalogado!!")
        return

    for pokemon_tipo in TipoPokemon:
        print(pokemon_tipo.value)

    while True:
        tipo = ler_texto("Digite o TIPO do Pokémon: ")
        if not tipo:
            erro_pokemon("Erro: A tipagem do Pokémon não pode ser vazio!!!")
            continue
        if tipo not in TipoPokemon.__members__:
            erro_pokemon("Erro: Tipo de Pokémon não encontrado!!!")
            continue
        break

    nivel = ler_nivel("Digite o nível do Pokémon: ")
    pokemons_capturados = 0


    limpar_terminal()
    pokedex[nome] = {"tipo": tipo, "nível": nivel, "capturados": pokemons_capturados}
    print(f"O Pokémon '{nome}' foi adicionado com sucesso a sua pokedex.\n")
    voltar_opcoes()
    limpar_terminal()

def mostrar_pokedex():#Função que lista todos os Pokémons cadastrados
    limpar_terminal()
    if not pokedex:
        erro_pokemon("Erro: Nenhum Pokémon catalogado !!!")
    for nome, info in sorted(pokedex.items()):
        print(f"Pokémon: {nome} - Tipo: {info['tipo']} - Nível: {info['nível']}\n")
    voltar_opcoes()
    limpar_terminal()

def remover_pokemon():#função para excluir um Pokémon
    limpar_terminal()
    while True:
        nome = ler_texto("Digite o NOME do Pokémon: ")
        if not nome:
            erro_pokemon("Erro: O NOME do pokemon deve ser informado!!!")
            continue
        elif nome not in pokedex:
            erro_pokemon("Erro: Pokémon não catalogado!!!")
            return
        del pokedex[nome]
        print(f"O Pokémon '{nome}' foi removido da Pokedex!!!")
        voltar_opcoes()
        return

def atualizar_nivel_pokemon():#Função que atualiza o nível de um Pokémon cadastrado
    limpar_terminal()
    while True:
        nome = ler_texto("Digite o NOME do Pokémon: ")
        if not nome:
            erro_pokemon("Erro: O NOME do pokemon deve ser informado!!!")
            continue
        if nome not in pokedex:
            erro_pokemon("Erro: Pokémon não catalogado!!!")
            return
        break
    novo_nivel = ler_nivel(f"Nível atual: {pokedex[nome]['nível']}\nDigite o novo nível do Pokémon: ")
    
    limpar_terminal()
    pokedex[nome]["nível"] = novo_nivel
    print(f"O nível de '{nome}' foi atualizado!!!")
    voltar_opcoes()
    limpar_terminal()

def capturar_pokemon():#Função para capturar um Pokémon e adicionar a contagem quantos já foram capturados
    limpar_terminal()
    while True:
        nome = ler_texto("Digite o NOME do Pokémon: ")
        if not nome:
            erro_pokemon("Erro: O nome não pode estar vazio!!!")
            continue
        if nome not in pokedex:
            erro_pokemon("Erro: Pokémon não catalogado!!!")
            return
        break

    while True:
        try:
            pokemons_capturados = int(input("Quantidade capturada: "))
            if pokemons_capturados <= 0:
                erro_pokemon("Erro: A quantidade deve ser maior que zero (0)!!!")
                continue
        except ValueError:
            erro_pokemon("Erro: A quantidade deve ser um número inteiro")
            continue
        break
                    

    limpar_terminal()
    pokebola.append({"nome": nome, "quantidade": pokemons_capturados})
    pokedex[nome]["capturados"] += pokemons_capturados
    print(f"A quantidade de '{nome}' capturados foi atualizado!!!")
    voltar_opcoes()
    limpar_terminal()  

def historico_captura_pokemon():#Função que exibe o Pokémon capturado e quantos já foram capturados
    limpar_terminal()
    if not pokebola:
        print("Nenhum pokemon capturado.")
    for captura in pokebola:
        print(f"Pokémon: {captura['nome']} - Quantidade capturada: {captura['quantidade']}")
    voltar_opcoes()
    limpar_terminal()

def sair():#Função para sair do sistema

    print("Saindo do sistema...")
    time.sleep(2)
    limpar_terminal()
    sys.exit()

def exibir_menu():#Função que exibe o menu de opções pro usuário
    
    return(
        "1 - Adicionar Pokémon \n"
        "2 - Abrir pokedex\n"
        "3 - Remover Pokémon \n"
        "4 - Atualizar nível Pokémon \n"
        "5 - Capturar Pokemon\n"
        "6 - Histórico de captura \n"
        "7 - Sair \n"
        "Escolha uma opção: "
        )

def main():#Função principal

    while True:
        limpar_terminal()
        try: 
            opcao = int(input(exibir_menu())) 
            if opcao < 1 or opcao > 7:
                erro_pokemon("Erro: opção inválida.")
                continue

        except ValueError:
            erro_pokemon("Erro: opção inválida.")
            continue

        
#------------(Controle da opcao 1 (Adicionar pokemons)------------#      
        if opcao == 1:
            adicionar_pokemon()
            
            
#------------(Controle da opcao 2 (Listar os pokemons))------------#

        elif opcao == 2:
            mostrar_pokedex()
            
    
#------------(Controle da opcao 3 (Remover um pokemon)------------#

        elif opcao == 3:
            remover_pokemon()
               
#------------(Controle da opcao 4 (Atualizar o nivel do pokemon))------------#

        elif opcao == 4:
            atualizar_nivel_pokemon()
            
#------------(Controle da opcao 5 (Capturar pokemon))------------#

        elif opcao == 5:
            capturar_pokemon()

#------------(Controle da opcao 6 (Exibir pokemons capturados))------------#

        elif opcao == 6:
            historico_captura_pokemon()
            
#------------(Controle da opcao 7 (Sair do sistema))------------#

        elif opcao == 7:
            sair()
            
    
if __name__ == "__main__":
    main()
