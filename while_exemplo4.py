### Média dos números digitados pelo usuário!!!!
qtde=0
soma=0
n=int(input("Digite um número: "))
while n!= 0:
    soma += n
    qtde += 1
    n=int(input("Digite um número: "))
    print("O valor atual da soma:",soma,"qtde:",qtde)

media=soma/qtde
print(media)