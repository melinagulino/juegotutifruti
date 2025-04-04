import random
import string
from src.jugador import Jugador


class Tuttifruti:
    def __init__(self, cantidad_jugadores=2):
        self.letras_usadas = set()
        self.letra_actual = self.obtener_letra_aleatoria()
        self.cantidad_jugadores = cantidad_jugadores
        self.puntajes = {f"jugador{i + 1}": 0 for i
                         in range(self.cantidad_jugadores)}
        self.jugadas = {f"jugador{i + 1}": {} for i
                        in range(self.cantidad_jugadores)}
        self.jugadores = {f"jugador{i + 1}": Jugador(f"Jugador {i + 1}") for i
                          in range(self.cantidad_jugadores)}
        self.valor_palabra_correcta = 10
        self.valor_palabra_repetida = 5
        self.valor_palabra_incorrecta = 0
        self.nombres_jugadores = {}

    def obtener_letra_aleatoria(self):
        letras_disponibles = set(string.ascii_uppercase) - self.letras_usadas
        if not letras_disponibles:
            raise ValueError("Todas las letras han sido usadas.")
        letra = random.choice(list(letras_disponibles))
        self.letras_usadas.add(letra)
        return letra

    def validar_palabra(self, palabra):
        return bool(palabra) and palabra[0].lower() == self.letra_actual.lower()

    def _calcular_puntaje_jugador(self, palabra_jugador, palabras_oponente):
        total_puntos = 0
        if self.validar_palabra(palabra_jugador):
            if palabra_jugador.lower() not in palabras_oponente:
                total_puntos += self.valor_palabra_correcta
            else:
                total_puntos += self.valor_palabra_repetida
        else:
            total_puntos += self.valor_palabra_incorrecta
        return total_puntos

    def calcular_puntos(self):
        for i in range(self.cantidad_jugadores):
            jugador = f"jugador{i + 1}"
            respuestas = self.jugadas[jugador]
            palabras_jugador = [p for p in respuestas.values() if p]
            puntaje_total = self.puntajes.get(jugador, 0)

            if jugador not in self.nombres_jugadores and "nombre" in respuestas:
                self.nombres_jugadores[jugador] = respuestas["nombre"]
            palabras_oponente = set()
            for j in range(self.cantidad_jugadores):
                if i != j:
                    palabras_oponente.update(
                        {p.lower() for p in self.jugadas[f"jugador{j + 1}"].values()
                         if p}
                    )
            for palabra_jugador in palabras_jugador:
                puntaje_total += (self._calcular_puntaje_jugador
                                  (palabra_jugador, palabras_oponente))
            self.puntajes[jugador] = puntaje_total

        return self.puntajes

    def calcular_ganador(self):
        max_puntaje = max(self.puntajes.values())
        ganadores = [jugador for jugador, puntaje in self.puntajes.items()
                     if puntaje == max_puntaje]
        if len(ganadores) > 1:
            return None
        else:
            jugador_id = ganadores[0]
            nombre = self.nombres_jugadores.get(jugador_id, jugador_id).capitalize()
            return Jugador(nombre)







