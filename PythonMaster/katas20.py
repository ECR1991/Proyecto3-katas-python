# ============================
# EJERCICIO 20
# Filtrar solo enteros
# ============================

def solo_enteros(lista):
    return list(filter(lambda x: type(x) == int, lista))


# Prueba
print(solo_enteros([1, "hola", 3, "mundo", 5]))
