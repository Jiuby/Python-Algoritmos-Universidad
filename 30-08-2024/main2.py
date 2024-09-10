
x = int(input("Ingrese un numero del 1 al 1000 (0 y mayor a 1000 para salir): "))

num250_400 = 0
num20_100 = 0
num500_700 = 0
cantidad = 0

while x != 0 and x < 1000:
    num = int(input("Inserte el numero:"))
    print(f"la longitud del numero es: {len(str(num))}")
    if num >= 250 and num <= 400:
        num250_400 += 1
    elif num >= 20 and num <= 100:
        num20_100 += 1
    elif num >= 500 and num <= 700:
        num500_700 += 1
    cantidad += 1
    x = int(input("Ingrese un numero del 1 al 1000 (0 y mayor a 1000 para salir): "))


print(f"La cantidad de numeros entre 250 y 400 es: {num250_400}")
print(f"La cantidad de numeros entre 20 y 100 es: {num20_100}")
print(f"La cantidad de numeros entre 500 y 700 es: {num500_700}")
print(f"La cantidad de numeros ingresados es: {cantidad}")


