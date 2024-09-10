vendedores = int(input("Digite la cantidad de vendedores: "))
sueldo_base = int(input("Digite el sueldo base: "))
comisiones_total = 0
venta_total = 0

for i in range(vendedores):
    comisiones_vendedor = 0
    for j in range(3):
        venta = int(input(f"Digite la venta {j + 1} del vendedor {i + 1}: "))
        venta_total += venta
        comisiones_vendedor += venta * 0.10

    comisiones_total += comisiones_vendedor
    print(f"El vendedor {i + 1} recibirá {comisiones_vendedor} por comisiones y {sueldo_base + comisiones_vendedor} por sueldo base y comisiones")

print(f"La venta total de la empresa es: {venta_total}")
print(f"La comisión total de la empresa es: {comisiones_total}")
