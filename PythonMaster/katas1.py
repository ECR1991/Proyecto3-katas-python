# ============================
# EJERCICIO 1
# Escribe una función que reciba una cadena de texto como parámetro
# y devuelva un diccionario con las frecuencias de cada letra.
# Los espacios no deben ser considerados.
# ============================

def contar_frecuencia_letras(texto):
    # Creamos un diccionario vacío para guardar las letras
    frecuencias = {}

    # Recorremos cada carácter del texto
    for letra in texto:
        # Comprobamos que no sea un espacio
        if letra != " ":
            # Si la letra ya está en el diccionario, sumamos 1
            if letra in frecuencias:
                frecuencias[letra] += 1
            # Si no está, la añadimos con valor 1
            else:
                frecuencias[letra] = 1

    # Devolvemos el diccionario con las frecuencias
    return frecuencias


# Prueba del ejercicio
texto_ejemplo = "hola hola"
resultado = contar_frecuencia_letras(texto_ejemplo)
print(resultado)
