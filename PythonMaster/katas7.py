# ============================
# EJERCICIO 7
# Convierte una lista de tuplas en strings usando map()
# ============================

def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))


# Prueba
print(tuplas_a_strings([(1, 2), (3, 4)]))
