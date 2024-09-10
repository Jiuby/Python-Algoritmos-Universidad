while True:
    salario_hora = int(input("Salario Por Hora: "))
    horas_trabajadas = int(input("Horas trabajadas: "))

    if horas_trabajadas <= 48:
        salario = horas_trabajadas * salario_hora
    elif horas_trabajadas <= 57:
        horas_extras = horas_trabajadas - 48
        salario = (48 * salario_hora) + (horas_extras * salario_hora * 1.25)
    else:
        extras_35 = horas_trabajadas - 57 # Se puede simplemente en salario borrar estas variables y realizar la logica ahi
        extras_25 = 8
        salario = (48 * salario_hora) + (extras_25 * salario_hora * 1.25) + (extras_35 * salario_hora * 1.35)

    print(salario)
    x = input("Desea continuar? ")
    if x.lower() == "no":
        break



