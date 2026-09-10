menor = None
maior = None
contador = 0
soma_temp = 0

while True:

  temp = float(input("Digite a temperatura: "))

  if temp == 100:
    break

  if menor is None or temp < menor:
    menor = temp
  if maior is None or temp > maior:
    maior = temp

  contador += 1

if contador > 0:
  media = (menor + maior) / 2

  print("A maior temperatura foi:", maior)
  print("A menor temperatura foi:", menor)
  print("A média das temperaturas foi:", media)

else:
  print("Nenhuma temperatura válida foi registrada.")