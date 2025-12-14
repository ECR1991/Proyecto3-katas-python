# ============================
# EJERCICIO 37
# Día, tarde o noche
# ============================

try:
    hora = int(input("Introduce la hora (0-23): "))

    if hora < 0 or hora > 23:
        print("Hora no válida")
    elif hora >= 6 and hora <= 12:
        print("Es de día")
    elif hora >= 13 and hora <= 19:
        print("Es de tarde")
    else:
        print("Es de noche")

except ValueError:
    print("Debes introducir un número")
