salario=float(input("Digite o seu salário: "))

if salario<500:
    salarioreajustado=salario+(salario*0.15)
    print("O seu salário reajustado é de:", salarioreajustado)
elif salario>=500 and salario <1000:
    salarioreajustado=salario+(salario*0.10)
    print("O seu salário reajustado é de:", salarioreajustado)
else:
    salarioreajustado=salario+(salario*0.05)
    print("O seu salário reajustado é de:", salarioreajustado)  