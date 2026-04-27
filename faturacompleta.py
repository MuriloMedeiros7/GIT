nome=str(input("Digite seu nome: "))
p1=float(input("Produto 1: "))
p2=float(input("Produto 2: "))
p3=float(input("Produto 3: "))
total=p1+p2+p3
media=total/3
imposto=total*0.12
valor_imposto=total+imposto
desconto=valor_imposto*0.05
valor_final=valor_imposto-desconto
print("\n---Relatório---")
print("Valor total:", total,"R$")
print("Valor da média: %.2f"% media,"R$")
print("Valor com impostos:", valor_imposto,"R$")
print("Valor final: %.2f"% valor_final,"R$")