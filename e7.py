cpf=(input("Digite o CPF (apenas números):"))

if cpf.isdigit(): #Confere se o que foi digitado na cadeia 'cpf' são números
    if len(cpf) == 11:
        print("CPF válido")
    else:
        print("CPF inválido")
else:
    print("O CPF digitado não possui apenas números")