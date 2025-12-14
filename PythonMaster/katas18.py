# ============================
# EJERCICIO 18
# Filtrar estudiantes con nota >= 90
# ============================

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Eva", "edad": 21, "calificacion": 90}
]

aprobados = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

print(aprobados)
