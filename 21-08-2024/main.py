x = input("¿Quiere jugar? ")
puntos = 0
if x.lower() == "si":
    print("5 + 5")
    resultado = int(input("Respuesta: "))
    if resultado == 10:
        puntos += 1
    else:
        puntos += 0

    print("5 - 5")
    resultado = int(input("Respuesta: "))
    if resultado == 0:
        puntos += 1
    else:
        puntos += 0

    print("5 * 5")
    resultado = int(input("Respuesta: "))
    if resultado == 25:
        puntos += 1
    else:
        puntos += 0

    print("5 / 5")
    resultado = int(input("Respuesta: "))
    if resultado == 1:
        puntos += 1
    else:
        puntos += 0

    print("5 % 5")
    resultado = int(input("Respuesta: "))
    if resultado == 0:
        puntos += 1
    else:
        puntos += 0

    if puntos == 5:
        print("Ganaste")
    else:
        print("Perdiste")
