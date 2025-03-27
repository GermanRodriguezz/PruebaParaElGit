def verificar_vocal(renglon,lista) : # recibo la linea de palabras del texto      # aca
    palabrasDelRenglon = renglon.split()
    if len(palabrasDelRenglon) > 1 : # si tengo mas de una palabra,evaluo la segunda
        palabra = palabrasDelRenglon[1]
        if  palabra.startswith(lista) :
            return True
    return False # en caso de que no tengo segunda palabra la linea retorna Flases