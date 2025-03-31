def entre(n):
    if int(n) >= 200 and int(n) <= 500:
        return True

def menos(n):
    if int(n) < 200:
        return True

def clasificarCategoria(n,respuesta):
    if menos(n):
        respuesta = "Rapido"
        return respuesta
    else:
        if entre(n) :
            respuesta = "Normal"
            return respuesta
        else :
            respuesta = "Lenta"
            return respuesta
