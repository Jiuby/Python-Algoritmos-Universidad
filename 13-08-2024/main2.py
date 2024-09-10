num1, num2, num3 = map(int, input("Inserte los numeros (por espacios): ").split())

if num1 == num2 or num2 == num3 or num3 == num1:
    print("hay numeros repetidos")
else:

    if (num1 > num2 > num3) or (num3 > num2 > num1):
        print("el numero del medio es", num2)
    elif (num2 > num1 > num3) or (num3 > num1 > num2):
        print("el numero del medio es", num1)
    else:
        print("el numero del medio es", num3)
