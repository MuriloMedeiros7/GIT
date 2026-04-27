n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
n3=float(input("Digite a nota 3: "))
n4=float(input("Digite a nota 4: "))

media=(n1+n2+n3+n4)/4

if media>=6:
    print(f"Média: {media} ->>> APROVADO")
elif media<6.0 and media>4.0:
    print(f"Média: {media} ->>> EXAME")
else:
    print(f"Média: {media} ->>> REPROVADO")