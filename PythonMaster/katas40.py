# ============================
# EJERCICIO 40
# Precio final con descuento
# ============================

try:
    precio = float(input("Precio original: "))
    tiene_cupon = input("¿Tienes cupón? (si/no): ").lower()

    if tiene_cupon == "si":
        descuento = float(input("Valor del cupón: "))
        if descuento > 0:
            precio -= descuento
            if precio < 0:
                precio = 0

    print("Precio final:", precio)

except ValueError:
    print("Error en los datos introducidos")
