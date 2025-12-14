# ============================
# EJERCICIO 33
# Suma los elementos correspondientes de dos listas
# ============================

sumar_listas = lambda lista1, lista2: list(map(lambda a, b: a + b, lista1, lista2))


# Prueba del ejercicio
print(sumar_listas([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]
