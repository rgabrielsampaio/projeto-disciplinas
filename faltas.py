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
        return {}

def salvar_frequencia(): # guardar dados no json
    with open(ARQUIVO_FREQUENCIA, "w", encoding="utf-8") as f:
        json.dump(frequencia, f, indent=4, ensure_ascii=False)

frequencia = carregar_frequencia()

def adicionar_frequencia():
    while True:
        limpar_tela()
        disciplinas = list(frequencia.items())

        if not disciplinas:
            input("Nenhuma disciplina cadastrada. Pressione Enter para voltar...")
            return
        
        for i, (disciplina, [quantidade, limite]) in enumerate(disciplinas, start=1):
            print(f"{i}. {disciplina}")
        print("\n0. Voltar\n")

        try:
            opcao = int(input("Escolha uma opção:  "))
            if opcao < 0 or opcao > len(disciplinas):
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

        frequencia[disciplina_selecionada] = [quantidade + nova_falta, limite]
        salvar_frequencia()
        limpar_tela()
        input("Falta(s) adicionada(s) com sucesso. Pressione Enter para continuar...")

def visualizar_frequencia():
    limpar_tela()
    print("Frequência Acadêmica:\n")
    for disciplina, (quantidade, limite) in frequencia.items():
        print(f"{disciplina} — {quantidade}/{limite}")
    input("\nPressione Enter para voltar ao menu...")

def gerenciar_disciplinas():
    while True:
        limpar_tela()
        print("Gerenciar Disciplinas\n")
        print("1. Cadastrar nova disciplina")
        print("2. Remover disciplina")
        print("\n0. Voltar\n")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            input("Entrada inválida. Pressione Enter para tentar novamente...")
            continue

        if opcao == 1:
            cadastrar_disciplina()
        elif opcao == 2:
            remover_disciplina()
        elif opcao == 0:
            return
        else:
            input("Opção inválida. Pressione Enter para tentar novamente...")

def cadastrar_disciplina():
    limpar_tela()
    print("Cadastrar nova disciplina\n")
    nome = input("Nome da disciplina: ").strip()

    if not nome:
        input("Nome inválido. Pressione Enter para continuar...")
        return

    if nome in frequencia:
        input("Essa disciplina já existe. Adicione outra.")
        return
    
    try:
        limite = int(input("Digite o limite de faltas permitido para a disciplina: "))
        if limite <= 0:
            raise ValueError("O limite deve ser maior que zero.")
    except ValueError:
        input("Valor inválido. Pressione enter para continuar...")
        return
    
    frequencia[nome] = [0, limite]
    salvar_frequencia()
    input("Disciplina cadastrada com sucesso! Pressione Enter para continuar...")

def remover_disciplina():
    while True:
        limpar_tela()
        print("Remover disciplina\n")
        disciplinas = list(frequencia.keys())

        if not disciplinas:
            input("Não há disciplinas cadastradas. Pressione Enter para continuar...")
            return
        
        for i, nome in enumerate(disciplinas, start=1):
            print(f"{i}. {nome}")
        print("\n0. Cancelar\n")

        try:
            opcao = int(input("Escolha uma disciplina para remover: "))
            if opcao == 0:
                return
            elif 1 <= opcao <=len(disciplinas):
                nome_disciplina = disciplinas[opcao - 1]
                confirmar = input(f"Tem certeza que deseja remover '{nome_disciplina}'? (s/n): ")
                if confirmar.strip().lower() == "s":
                    del frequencia[nome_disciplina]
                    salvar_frequencia()
                    input("Disciplina removida com sucesso! Pressione Enter para continuar...")
                    limpar_tela()
                    return
                else:
                    input("Remoção cancelada. Pressione Enter para continuar")
                    return
            else:
                input("Opção inválida. Pressione Enter para continuar...")
        except ValueError:
            input("Entrada inválida. Pressione Enter para continuar...")
        

def menu_principal():
    while True:
        limpar_tela()
        print("Menu Principal\n")
        print("1. Adicionar faltas")
        print("2. Verificar faltas")
        print("3. Gerenciar disciplinas")
        print("\n0. Sair\n")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            limpar_tela()
            input("Opção inválida. Pressione Enter para tentar novamente...")

        if opcao == 1:
                adicionar_frequencia()
        elif opcao == 2:
            visualizar_frequencia()
        elif opcao == 3:
            gerenciar_disciplinas()
        elif opcao == 0:
            limpar_tela()
            sys.exit()
        else:
            limpar_tela()
            input("Opção inválida. Pressione Enter para tentar novamente...")

def main():
    limpar_tela()
    input("Pressione Enter para começar...")
    menu_principal()

if __name__ == "__main__":
    main()