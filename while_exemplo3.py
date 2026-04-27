#### Faca um algoritimo que receba n numeros
#### e some-os até que o usuário digite 0

soma=0
num=int(input("Digite um número: "))
while num!=0:
    soma += num
    num=int(input("Digite um número: "))

print("Total:",soma)