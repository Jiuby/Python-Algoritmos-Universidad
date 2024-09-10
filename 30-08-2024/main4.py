lista = []

while True:
    x = int(input("Digite un número: "))
    lista.append(x)

    if lista[0] > lista[-1]:
        lista[0] = lista[-1]

    continuar = input("¿Desea agregar otro número? (S/N): ").lower()
    if continuar == "n":
        break

print("El numero mas menor es:", lista[0])
