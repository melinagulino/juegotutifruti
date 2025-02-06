import random
import string

class Tuttifruti:
    def __init__(self):
        self.letra_actual = self.obtener_letra_aleatoria()
        self.cantidad_jugadores = 2
        self.totales = []
        self.total_jugador1 = 0
        self.total_jugador2 = 0
        self.jugada_jugador1 = {}
        self.jugada_jugador2 = {}
        self.valor_palabra_correcta = 10
        self.valor_palabra_repetida = 5
        self.valor_palabra_incorrecta = 0

    @staticmethod
    def obtener_letra_aleatoria():
        return random.choice(string.ascii_uppercase)

    def validar_palabra(self, palabra):
        return bool(palabra) and palabra[0].upper() == self.letra_actual

    def calcular_puntos(self):
        palabras_j1 = {p.lower() for p in self.jugada_jugador1.values() if p}
        palabras_j2 = {p.lower() for p in self.jugada_jugador2.values() if p}

        for palabra_j1 in palabras_j1:
            if palabra_j1.upper() and self.validar_palabra(palabra_j1):
                if palabra_j1 not in palabras_j2:
                    self.total_jugador1 += self.valor_palabra_correcta
                else:
                    self.total_jugador1 += self.valor_palabra_repetida
            else:
                self.total_jugador1 += self.valor_palabra_incorrecta

        for palabra_j2 in palabras_j2:
            if palabra_j2.upper() and self.validar_palabra(palabra_j2):
                if palabra_j2 not in palabras_j1:
                    self.total_jugador2 += self.valor_palabra_correcta
                else:
                    self.total_jugador2 += self.valor_palabra_repetida
            else:
                self.total_jugador2 += self.valor_palabra_incorrecta

        return [self.total_jugador1, self.total_jugador2]

    def calcular_ganador(self):
        if self.total_jugador1 > self.total_jugador2:
            return "Jugador 1"
        elif self.total_jugador2 > self.total_jugador1:
            return "Jugador 2"
        else:
            return "Empate"



