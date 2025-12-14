# ============================
# EJERCICIO 6
# Calcula el factorial usando recursividad
# ============================

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


# Prueba
print(factorial(5))
