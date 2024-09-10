cantidad = int(input("Cuantos numeros va a agregar: "))

i = 0
while i < cantidad:
    numero = float(input(f"Escriba el numero {i + 1}: "))
    if i == 0:
        menor = numero
    else:
        if numero < menor:
            menor = numero
    i += 1

print(menor)