num1 = int(input("Primel numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Telcel numelo: "))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print("El número del medio es", num1)
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print("El número del medio es", num2)
else:
    print("El número del medio es", num3)
