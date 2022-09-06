nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
doencaInfectoContagiosa = input("Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print("\nO paciente " + nome + " POSSUI atendimento prioritário!")
elif doencaInfectoContagiosa == "SIM":
    print("\nO paciente " + nome + " DEVE ser direcionado para sala de espera reservada!")
else:
    print("\nO paciente " + nome + " NÂO POSSUI atendimento prioritário e pode aguardar na sala comum!")
print("FIM")
