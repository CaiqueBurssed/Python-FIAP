with open("iris.data", "r") as arquivo:
    basedados = []
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(basedados)

print(basedados[0][0] + " , " + basedados[0][1])
print(float(basedados[0][0]) + float(basedados[0][1]))
