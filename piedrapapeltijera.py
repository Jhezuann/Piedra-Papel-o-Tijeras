import random

def jugar():
    usuario=input("Escoge una opcion: 'pi' para piedra, 'pa' para papel y 'ti' para tijera.\n").lower()

    computadora=random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!'

    if ganoElJugador(usuario, computadora):
        return 'Ganaste!'
    
    return 'Perdiste!'

def ganoElJugador(jugador, oponente):
    #Retornar True(verdadero) si gana el jugador
    #Piedra gana a tijera (pi>ti)
    #Tijera gana a papel (ti>pa)
    #papel gana a piedra (pa>pi)
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False

print(jugar())