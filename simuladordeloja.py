p1=float(input("Produto 1: "))
p2=float(input("Produto 2: "))
p3=float(input("Produto 3: "))
p4=float(input("Produto 4: "))
p5=float(input("Produto 5: "))
total=p1+p2+p3+p4+p5
desconto_avista=total*0.10
final_avista=total-desconto_avista
desconto_cartao=total*0.05
final_cartao=total-desconto_cartao
desconto_parcelado=0
final_parcelado=total

print("Total:", total,"R$")
print("\nÀ vista")
print("\nDesconto  à vista:", desconto_avista,"R$")
print("Valor final à vista:", final_avista,"R$")
print("\nCartão")
print("\nDesconto cartão:", desconto_cartao,"R$")
print("Valor final cartão:", final_cartao,"R$")
print("\nParcelado")
print("\nDesconto parcelado:", desconto_parcelado,"R$")
print("Valor final parcelado:", final_parcelado,"R$")