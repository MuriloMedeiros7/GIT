valor=float(input("Digite o valor de aquisição do produto: "))

if valor<50:
    venda=valor+(valor*0.45)
else:
    venda=valor+(valor*0.30)
    print("O valor da compra será de: R$", venda)