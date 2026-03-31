"""Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
Calcula el precio final después del descuento.
Muestra el precio final al usuario.
"""

precio = int(input("Ingrese precio del artículo"))
descuento = int(input("Ingrese porcentaje de descuento"))

print(f"Precio final es: {precio-(precio*(descuento/100))}")