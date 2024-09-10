edad_mujeres = 0
edad_hombres = 0

while True:
    edad = int(input("Digite la edad: "))
    genero = input("Digite el genero (M o H): ").lower()

    if genero == "m":
        edad_mujeres += edad
    elif genero == "h":
        edad_hombres += edad
    else:
        print("Genero no valido")
        break

    verificacion = input("¿Desea agregar otra persona? (S/N): ").lower()
    if verificacion == "n":
        break




print(f"La edad promedio de las mujeres es: {edad_mujeres / 2}")
print(f"La edad promedio de los hombres es: {edad_hombres / 2}")