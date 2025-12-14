# ============================
# EJERCICIO 4
# Calcula la diferencia entre dos listas usando map()
# ============================

def diferencia_listas(lista1, lista2):
    return list(map(lambda a, b: a - b, lista1, lista2))


# Prueba
print(diferencia_listas([10, 20, 30], [1, 2, 3]))
