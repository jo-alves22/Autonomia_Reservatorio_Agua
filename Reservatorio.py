print("Digite a altura do reservatorio em centimetros:")
altura = int(input())
print("Digite a largura do reservatorio em centimetros:")
largura = int(input())
print("Digite o comprimento do reservatorio em centimetros:")
comprimento = int(input())
print("Digite o consumo médio diário em litros por dia:")
consumo = int(input())

volume = altura * largura * comprimento
volume = volume / 1000
autonomia = volume / consumo
print(f"A capacidade total do reservatório é de: {volume} litros" )
print(f"A autonomia do reservatório é de: {autonomia} dias")

if(autonomia >= 7):
    print(f"Classificação de consumo: REDUZIDA")
elif(autonomia > 2) and (autonomia < 7):
    print(f"Classificação de consumo: MODERADA")
else:
    print(f"Classificação de consumo: ELEVADA")