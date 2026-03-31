peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

imc = peso/(altura*altura)
print(f"El IMC es {imc}")
if imc<18.5:
    print(f"Talle S")
elif imc>=18.5 and imc<24.9:
    print(f"Talle M")
elif imc>25 and imc<29.9:
    print(f"Talle L")
elif imc>=30:
    print(f"Talle XL")