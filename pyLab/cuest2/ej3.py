"""
3.Escribe un programa que muestra la primer,
última u otra letra de una cadena de caracteres,
inclusive una rebanada."""

palabra = input("Introduzca una palabra: ").lower()

print(f"La primera letra es: {palabra[0]}")
print(f"La ultima letra es: {palabra[-1]}")
print(f"La letra del medio es: {palabra[len(palabra)//2]}")
print(f"Una rebanada es {palabra[2:5]}")
print(f"Una rebanada es {palabra[3:]}")