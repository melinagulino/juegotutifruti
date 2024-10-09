
from tutiffrutti import Jugador


def test_crear_jugador():
    jugador = Jugador("Melina")

    assert jugador.crear_jugador("Melina") == True
    assert jugador.crear_jugador("Juan") == True


def test_crear_varios_jugadores():
    jugador = Jugador("Melina")
    jugador1 = Jugador("Juan")

    assert jugador.crear_jugador("Melina") == True
    assert jugador1.crear_jugador("Juan") == True


def test_validar_jugador():
    jugador = Jugador("Melina")
    assert jugador.crear_jugador("Melina") == True
    assert jugador.es_jugador_valido == True


def test_validar_nombre_del_jugador():
    jugador = Jugador("Melina")

    assert jugador.validar_nombre("Melina") == True
    assert jugador.validar_nombre("Juan") == False