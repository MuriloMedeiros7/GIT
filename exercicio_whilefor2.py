nomes=[]
print("Digite 10 nomes abaixo:")
for i in range(1,11):
    nome=input("Digite o nome: ")
    nomes.append(nome)
    print("\n--- Lista de Nomes Recebidos ---")
for nome in nomes:
    print("Nomes:",nomes)