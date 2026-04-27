ladot1=float(input("Digite o primeiro lado:"))
ladot2=float(input("Digite o segundo lado:"))
ladot3=float(input("Digite o terceiro lado:"))

if ladot1+ladot2>ladot3 and ladot1+ladot3>ladot2 and ladot2+ladot3>ladot1:
    print("É um triângulo!")
    if ladot1==ladot2 and ladot2==ladot3:
        print("É um triângulo Equilátero")
elif ladot1==ladot2 or ladot1==ladot3 or ladot2==ladot3:
    print("É um triângulo Isósceles")
elif ladot1!=ladot2 and ladot2!=ladot3:
    print("É um triângulo Escaleno")
else:
    print("Não é um triângulo")