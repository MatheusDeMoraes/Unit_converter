grandeza = [
  [1, "Volume"],
  [2, "Energia"]
]
volume = [
  [1, "Litro (L)", 1],
  [2, "Metro cúbico (m^3)", 1000],
  [3, "Centímetro cúbico (cm^3)", 0.001],
  [4, "Galão (gal)", 3.78541],
  [5, "Onça fluida (fl oz)", 0.0295735]
]

energy = [
  [1, "Joule (J)", 1],
  [2, "Kilojoule (kJ)", 1000],
  [3, "Kilowatt-hora (kWh)", 3.6e+06],
  [4, "Caloria (cal)", 4.184],
  [5, "Kilocaloria (kcal)", 4184],
  [6, "BTU", 1055.06]
]

print("CONVERSOR DE UNIDADES")
print("Selecione uma grandeza:")
print("1\tVolume")
print("2\tEnergia")
n = int(input())

if (n == 1):
  print("Volume")
  print("\nEscolha a unidade inicial:")
  for i in range(5):
    print(volume[i][0], end='\t')
    print(volume[i][1])

  u1 = int(input())
  print(volume[u1-1][1])

  print("\nEscolha a unidade para a qual converter:")
  for i in range(5):
    print(volume[i][0], end='\t')
    print(volume[i][1])

  u2 = int(input())
  print(volume[u2-1][1])

  print("\nDigite", grandeza[n-1][1], "em", volume[u1-1][1])

  x1 = float(input())
  c1 = volume[u1-1][2]
  c2 = volume[u2-1][2]
  x2 = x1*c1/c2

  print(x1, volume[u1-1][1], "=", x2, volume[u2-1][1])

if (n == 2):
  print("Energia")
  print("\nEscolha a unidade inicial:")
  for i in range(5):
    print(energy[i][0], end='\t')
    print(energy[i][1])
    
  u1 = int(input())
  print(energy[u1-1][1])

  print("\nEscolha a unidade para a qual converter:")
  for i in range(6):
    print(energy[i][0], end='\t')
    print(energy[i][1])
  
  u2 = int(input())
  print(energy[u2-1][1])

  print("\nDigite", grandeza[n-1][1], "em", energy[u1-1][1])

  x1 = float(input())
  c1 = energy[u1-1][2]
  c2 = energy[u2-1][2]
  x2 = x1*c1/c2

  print()
  print(x1, energy[u1-1][1], "=", x2, energy[u2-1][1])
