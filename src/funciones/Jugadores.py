def MayorPuntaje(jugadores):
    puntosMax = 0
    claveMVP = ""
    for clave,valor in jugadores.items() :
        if jugadores[clave]["puntuacion"] > puntosMax :
            claveMVP = clave
            puntosMax = valor["puntuacion"]
    return claveMVP

def cargarInformacionJugadores(clave,valor,jugadores): #en este 
    PuntoKill = 3
    #acumulo en mi nuevo diccionario los datos que hizo en la ronda x los puntos
    jugadores[clave]["kills"] += valor["kills"] 
    jugadores[clave]["asistencia"] += valor["assists"] 
    #acumula todos los puntos recaudados por ronda en puntuacion
    if valor["deaths"] is True:
        jugadores[clave]["muertes"] += 1 
    else :
        jugadores[clave]["muertes"] += 0
    jugadores[clave]["puntuacion"] = (( jugadores[clave]["kills"]* PuntoKill) + jugadores[clave]["asistencia"] - (jugadores[clave]["muertes"]))
    return jugadores
