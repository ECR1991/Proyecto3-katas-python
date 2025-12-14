# ============================
# EJERCICIO 22
# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
# ============================

from functools import reduce

def producto_total(lista):
    # Reduce va multiplicando el acumulado por el siguiente número
    return reduce(lambda a, b: a * b, lista)

# Prueba del ejercicio
print(producto_total([1, 2, 3, 4]))  # 24
