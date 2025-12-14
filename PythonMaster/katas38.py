# ============================
# EJERCICIO 38
# Calificación en texto
# ============================

try:
    nota = int(input("Introduce la nota (0-100): "))

    if nota < 0 or nota > 100:
        print("Nota no válida")
    elif nota <= 69:
        print("insuficiente")
    elif nota <= 79:
        print("bien")
    elif nota <= 89:
        print("muy bien")
    else:
        print("excelente")

except ValueError:
    print("Debes introducir un número")
