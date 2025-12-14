# ============================
# EJERCICIO 32
# Buscar el puesto de un empleado por su nombre
# ============================

def buscar_empleado(nombre, empleados):
    # Recorremos la lista de empleados
    for empleado in empleados:
        # Si el nombre coincide, devolvemos el puesto
        if empleado["nombre"] == nombre:
            return empleado["puesto"]

    # Si no se encuentra el nombre
    return "La persona no trabaja aquí"


# Prueba del ejercicio
empleados = [
    {"nombre": "Juan Perez", "puesto": "Programador"},
    {"nombre": "Ana Lopez", "puesto": "Diseñadora"},
    {"nombre": "Luis Gomez", "puesto": "Administrador"}
]

print(buscar_empleado("Ana Lopez", empleados))
print(buscar_empleado("Pedro Ruiz", empleados))
