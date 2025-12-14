# ============================
# EJERCICIO 3
# Devuelve las palabras que contienen una palabra objetivo
# ============================

def palabras_con_objetivo(lista_palabras, objetivo):
    resultado = []

    for palabra in lista_palabras:
        if objetivo in palabra:
            resultado.append(palabra)

    return resultado


# Prueba
palabras = ["casa", "caseta", "perro", "casual"]
print(palabras_con_objetivo(palabras, "casa"))
