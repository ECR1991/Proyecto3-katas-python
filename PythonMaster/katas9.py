# ============================
# EJERCICIO 9
# Filtra mascotas prohibidas usando filter()
# ============================

def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))


# Prueba
mascotas = ["Perro", "Gato", "Oso", "Mapache"]
print(filtrar_mascotas(mascotas))
