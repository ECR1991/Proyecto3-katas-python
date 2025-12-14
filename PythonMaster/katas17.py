# ============================
# EJERCICIO 17
# Lista de dígitos a número
# ============================

from functools import reduce

def lista_a_numero(lista):
    return reduce(lambda a, b: a * 10 + b, lista)


# Prueba
print(lista_a_numero([5, 7, 2]))
