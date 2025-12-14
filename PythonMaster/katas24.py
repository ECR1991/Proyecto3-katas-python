# ============================
# EJERCICIO 24
# Calcula la diferencia total en los valores de una lista. Usa la función reduce().
# ============================

from functools import reduce

def diferencia_total(lista):
    # Se hace: primer - segundo - tercero - ...
    return reduce(lambda a, b: a - b, lista)

# Prueba del ejercicio
print(diferencia_total([20, 5, 3]))  # 12
