# ============================
# EJERCICIO 36
# Función procesar_texto
# ============================

def contar_palabras(texto):
    resultado = {}
    for palabra in texto.split():
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1
    return resultado

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra]
    return " ".join(palabras)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"


# Pruebas
print(procesar_texto("hola mundo hola", "contar"))
print(procesar_texto("hola mundo", "reemplazar", "hola", "adios"))
print(procesar_texto("hola mundo hola", "eliminar", "hola"))
