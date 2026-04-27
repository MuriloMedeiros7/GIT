distancia=float(input("Distância: "))
consumocarro=float(input("Consumo do carro: "))
preçocombustivel=float(input("Preço do combustível: "))
litros=distancia/consumocarro
custo=litros*preçocombustivel
print("Litros necessários: %.2f"% litros)
print("Custo total da viagem: %.2f"% custo,"R$")
