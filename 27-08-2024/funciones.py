def promedioNotas(cantidad: int):
    i = 0
    suma = 0
    while i < cantidad:
        nota = float(input(f"Escriba la nota {i + 1}: "))
        suma += nota
        i += 1
    return suma / cantidad

def cuboYcuarta(cantidad: int):
    i = 0
    suma_cubo = 0
    suma_cuarta = 0

    while i < cantidad:
        numero = float(input(f"Escriba el numero {i + 1}: "))
        cubo = int(numero ** 3)
        cuarta = int(numero ** 4)
        print(cubo, cuarta)
        suma_cubo += cubo
        suma_cuarta += cuarta
        i += 1

    return f"El cubo es: {suma_cubo}, la cuarta es: {suma_cuarta}"

