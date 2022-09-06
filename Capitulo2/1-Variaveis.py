nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtdFuncionarios = int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print("\n" + nome + " trabalha na empresa " + empresa + ".")
print(empresa + " possui ", qtdFuncionarios, " funcionários e tem uma média salárial de:", mediaMensalidade)

print("\n---------------------Verifique os tipos de dados abaixo---------------------")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtdFuncionarios] é: ", type(qtdFuncionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))