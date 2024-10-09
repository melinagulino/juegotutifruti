class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.es_jugador_valido = False

    def crear_jugador(self, nombre):
        self.nombre = nombre

        if self.nombre == "Melina" or self.nombre == "Juan":
            self.es_jugador_valido = True
            return True
        return False

    def validar_nombre(self, nombre):
        return self.nombre == nombre