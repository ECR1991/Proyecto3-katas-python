# ============================
# EJERCICIO 31
# Buscar un nombre en una lista introducida por el usuario
# ============================

def buscar_nombre():
    try:
        # Pedimos una lista de nombres separados por comas
        nombres = input("Introduce una lista de nombres separados por comas: ")
        lista_nombres = nombres.split(",")

        # Quitamos espacios en blanco
        lista_nombres = [nombre.strip() for nombre in lista_nombres]

        # Pedimos el nombre a buscar
        nombre_buscar = input("Introduce el nombre a buscar: ")

        # Comprobamos si está en la lista
        if nombre_buscar in lista_nombres:
            print("Nombre encontrado")
        else:
            # Lanzamos una excepción si no está
            raise Exception("El nombre no se encuentra en la lista")

    except Exception as error:
        print(error)


# Prueba del ejercicio
buscar_nombre()
