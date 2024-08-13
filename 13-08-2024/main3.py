verificacion = input("¿Desea agregar producto? ")

final = 0

while verificacion.lower() == "si":
    producto = int(input("Precio del producto: "))
    final += producto
    verificacion = input("¿Desea agregar otro producto? ")

balota= input("Inserte el color de la balota sacada: ").lower()

if balota == "blanco":
    descuento = 0
elif balota == "amarillo":
    descuento = 1.10
elif balota == "verde":
    descuento = 1.20
elif balota == "azul":
    descuento = 1.40
elif balota == "rojo":
    descuento = 1.80

total_con_descuento = final * descuento

iva = total_con_descuento * 0.19

total_final = total_con_descuento + iva



print("El total antes de IVA es:", total_con_descuento)
print("El IVA es:", iva)
print("El total a pagar es:", total_final)



