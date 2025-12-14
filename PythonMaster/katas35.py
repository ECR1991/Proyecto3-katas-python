# ============================
# EJERCICIO 35
# Clase UsuarioBanco
# ============================

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise Exception("Cantidad no válida")
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise Exception("Cantidad no válida")
        if cantidad > self.saldo:
            raise Exception("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise Exception("Cantidad no válida")
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)


# Caso de uso
try:
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    bob.agregar_dinero(20)
    bob.transferir_dinero(alicia, 80)
    alicia.retirar_dinero(50)

    print("Saldo Alicia:", alicia.saldo)
    print("Saldo Bob:", bob.saldo)

except Exception as e:
    print(e)
