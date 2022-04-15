filap1 = []
filap2 = []
opMenu = 0
opPrioridade = 0

def exibirFila():
    print("\n\n\nFILA DE ATENDIMENTO\n\n")
    if filap1 or filap2:
        if filap1:
            for posicao, nome in enumerate(filap1):
                print(f"O paciente {nome} é o numero {posicao+1} da fila")
        
        if filap2:
            for posicao, nome in enumerate(filap2):
                print(f"O paciente {nome} é o numero {posicao+1+len(filap1)} da fila")
    else:
        print("\n\n As filas de atendimento estão vazias.\n\n")

def cadastrarPaciente(nome,p):
    if p == 1:
        filap1.append(nome)
        print(f"\n\n\nPaciente {nome} cadastrado na fila de prioridade ALTA\n\n\n")
    else:
        filap2.append(nome)
        print(f"\n\n\nPaciente {nome} cadastrado na fila de prioridade BAIXA\n\n\n")

def atenderPaciente():
    if filap1:
       return print(f"O paciente {filap1.pop(0)} de prioridade ALTA foi atendido.")
    elif filap2:
       return print(f"O paciente {filap2.pop(0)} de prioridade BAIXA foi atendido.")
    else:
        return print("\n\nFila de Atendimento Vazia !!!\n\n")

def limparFila():
    
    if filap1 or filap2:
        if filap1:
            print(f"{len(filap1)} removido(s) da fila de atendimento de prioridade ALTA")
            filap1.clear()
        
        if filap2:
            print(f"{len(filap2)} removido(s) da fila de atendimento de prioridade BAIXA")
            filap2.clear()
    else:
        print("\n\nFila de Atendimento Vazia !!!\n\n")

def buscarPaciente(nome):
    if nome in filap1:
        p = filap1.index(nome)
        return p+1

    if nome in filap2:
        p = filap2.index(nome)
        return p+1+len(filap1)

    return -1

def Menu():
    print("""
    MENU\n
    1 - Exibir Fila
    2 - Cadastrar Paciente.
    3 - Atender Paciente.
    4 - Buscar Paciente.
    5 - Limpar fila de atendimento.
    6 - Sair
    """
    )

def menuPrioridade():
    print("""
    PRIORIDADE \n
    1 - Alta
    2 - Baixa.
    """
    )

while opMenu != 6:
    Menu()
    opMenu = int(input("Digite a opção desejada:"))

    if opMenu == 1 or opMenu == 2 or opMenu == 3 or opMenu == 4 or opMenu == 5 or opMenu == 6:
        if opMenu == 1:
            exibirFila()

        if opMenu == 2:
            while opPrioridade != 1 or opPrioridade !=2:
                menuPrioridade()
                opPrioridade = int(input("Selecione a prioridade:"))
                if opPrioridade == 1 or opPrioridade ==2:
                    cadastrarPaciente(input("Qual o nome do paciente:"),opPrioridade)
                    break
                else:
                    print("\n\nPrioridade Inválida\n\n")
                    continue

        if opMenu == 3:
            atenderPaciente()

        if opMenu == 4:
            paciente = input("Qual o nome do paciente:")
            posicao = buscarPaciente(paciente)
            
            if posicao != -1:
                print(f"\n\nPaciente {paciente} esta na posicao {posicao} da fila de atendimento \n\n\n")
            else:
                print("\n\n\nPaciente não encontrado\n\n\n")          

        if opMenu == 5:
            limparFila()
                        
        if opMenu == 6: 
            print("\n\nAté a próxima\n\n")            
            break
    else:
       print("\n\nOpção Inválida. Tente Novamente!!! \n\n")