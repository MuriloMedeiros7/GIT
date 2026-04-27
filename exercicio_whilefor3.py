totalnotas=int(input("Digite a quantidade de avaliações: "))
soma=0
for i in range(totalnotas):
    nota=float(input("Digite a nota: "))
    soma+=nota
media=soma/totalnotas
print("%.2f"%media)