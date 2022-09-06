tabuada = int(input("Digite um numero para exibir a tabuada: "))

print("\nTabuada do npumero ", tabuada)

for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str(tabuada*valor))