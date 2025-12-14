# ============================
# EJERCICIO 10
# Calcula el promedio y lanza excepción si la lista está vacía
# ============================

def promedio_lista(lista):
    if len(lista) == 0:
        raise Exception("La lista está vacía")

    return sum(lista) / len(lista)


# Prueba
try:
    print(promedio_lista([4, 6, 8]))
except Exception as error:
    print(error)
