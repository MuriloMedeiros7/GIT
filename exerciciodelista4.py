lista= [0,1,2,3,4,5,6,7,8,9,10]
print(lista[1:10])
print(lista[8:11])

print(lista[0],lista[2],lista[4],lista[6],lista[8],lista[10])
print(lista[1],lista[3],lista[5],lista[7],lista[9])

lista.sort(reverse=True)
print(lista)
print(sum(lista))
print(len(lista))