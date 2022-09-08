def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       input("Numero Serial: "),
                       input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()
#

def exibirInventario(lista):
    for elemento in lista:
        print("\nNome:", elemento[0])
        print("Valor:", elemento[1])
        print("Serial:", elemento[2])
        print("Departamento:", elemento[3])
#

def exibirPorNome(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor: ", elemento[1])
            print("Serial: ", elemento[2])
#

def depreciarPorNome(lista):
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo:", elemento[1])
            elemento[1] = elemento[1] * 0.9
            print("Valor novo:", elemento[1])
#

def excluirPorSerial(lista):
    serial = input("Digite o valor serial do equipamento que será excluído: ")
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
#

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O valor total de equipamentos é de: ", sum(valores))
#
