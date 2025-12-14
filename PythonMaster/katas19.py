# ============================
# EJERCICIO 19
# Filtrar números impares
# ============================

impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))


# Prueba
print(impares([1, 2, 3, 4, 5]))
