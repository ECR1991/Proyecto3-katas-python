# ============================
# EJERCICIO 11
# Pedir la edad y comprobar que es correcta
# ============================

try:
    edad = int(input("Introduce tu edad: "))

    if edad < 0 or edad > 120:
        print("Edad fuera de rango.")
    else:
        print("Edad correcta:", edad)

except ValueError:
    print("Error: debes introducir un número.")
