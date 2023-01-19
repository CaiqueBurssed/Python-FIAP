with open("primeiro_arquivo.txt", "w") as arquivo:
    arquivo.write("Hakuna Matata!\nE lindo viver!\nVoce vai aprender!")

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)
