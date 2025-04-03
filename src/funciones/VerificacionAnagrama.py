def anagrama(primerP,segundaP):
    if len(primerP) != len(segundaP) : # 1ro - si tienen la misma cantidad de caracteres sera lo primero que chekeo
        return False 
    if sorted(primerP) == sorted(segundaP):
        return True
    else:
        return False