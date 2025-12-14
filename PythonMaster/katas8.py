# ============================
# EJERCICIO 8
# División con control de errores
# ============================

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = num1 / num2
    print("La división es:", resultado)

except ValueError:
    print("Error: debes introducir números.")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
