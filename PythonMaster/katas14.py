# ============================
# EJERCICIO 14
# Filtra palabras que empiezan por una letra
# ============================

def palabras_por_letra(lista, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista))


# Prueba
print(palabras_por_letra(["casa", "perro", "coche"], "c"))
