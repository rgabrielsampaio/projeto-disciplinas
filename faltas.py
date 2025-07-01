import os
import sys
import json

def limpar_tela(): # apagar console
    os.system('cls' if os.name == 'nt' else 'clear')

ARQUIVO_FREQUENCIA = "frequencia.json"

def carregar_frequencia(): # importar json com os dados salvos
    if os.path.exists(ARQUIVO_FREQUENCIA):
        with open(ARQUIVO_FREQUENCIA, "r", encoding="utf-8") as f:
            return json.load(f)

    else:
        return {
            "Computação em Nuvem": (0, 15),
            "Fundamentos de Redes de Computadores": (0, 15),
            "Introdução à Programação de Computadores": (0, 8),
            "Introdução à Segurança da Informação": (0, 19),
            "Pensamento Computacional": (0, 15)
        }

def salvar_frequencia(): # guardar dados no json
    with open(ARQUIVO_FREQUENCIA, "w", encoding="utf-8") as f:
        json.dump(frequencia, f, indent=4, ensure_ascii=True)

frequencia = carregar_frequencia()

def adicionar_frequencia():
    while True:
        limpar_tela()
        print("Adicionar Falta\n")
        for i, (disciplina, (quantidade, limite)) in enumerate(frequencia.items(), start=1):
            print(f"{i}. {disciplina}")
        print("\n0. Voltar\n")

        try:
            opcao = int(input("Escolha uma opção:  "))
            if opcao < 0 or opcao > i:
                limpar_tela()
                input("Opção inválida. Pressione Enter para tentar novamente...")
                continue
            elif opcao == 0:
                return  # volta ao menu principal
        except ValueError:
            limpar_tela()
            input("Opção inválida. Pressione Enter para tentar novamente...")
            continue

        lista_disciplinas = list(frequencia.items())
        disciplina_selecionada, (quantidade, limite) = lista_disciplinas[opcao - 1]

        while True:
            limpar_tela()
            try:
                nova_falta = int(input(f"Quantas faltas deseja adicionar em {disciplina_selecionada}? "))
                if nova_falta < 0:
                    raise ValueError("Número negativo")
                break
            except ValueError:
                input("Entrada inválida. Pressione Enter para tentar novamente...")

        frequencia[disciplina_selecionada] = (quantidade + nova_falta, limite)
        salvar_frequencia()
        limpar_tela()
        input("Falta(s) adicionada(s) com sucesso. Pressione Enter para continuar...")

def visualizar_frequencia():
    limpar_tela()
    print("Frequência Acadêmica:\n")
    for disciplina, (quantidade, limite) in frequencia.items():
        print(f"{disciplina} — {quantidade}/{limite}")
    input("\nPressione Enter para voltar ao menu...")

def menu_principal():
    while True:
        limpar_tela()
        print("Menu Principal\n")
        print("1. Adicionar faltas")
        print("2. Verificar faltas")
        print("\n0. Sair\n")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                adicionar_frequencia()
            elif opcao == 2:
                visualizar_frequencia()
            elif opcao == 0:
                limpar_tela()
                sys.exit()
            else:
                limpar_tela()
                input("Opção inválida. Pressione Enter para tentar novamente...")
        except ValueError:
            limpar_tela()
            input("Opção inválida. Pressione Enter para tentar novamente...")

def main():
    limpar_tela()
    input("Pressione Enter para começar...")
    menu_principal()

main()
