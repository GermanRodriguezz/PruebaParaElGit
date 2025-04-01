def anagrama(primerP,segundaP):
    if len(primerP) == len(segundaP) : # 1ro - si tienen la misma cantidad de caracteres sera lo primero que chekeo
        print('la palabra es ',primerP)
        for i in range(len(segundaP)) :     # 2do - tengo que ver si las letras de la 2da palabra se encuentran en la primer palabra,para eso recorro
            letra = segundaP[i]
            print(letra)
            if not letra in primerP : # 3ro - si no se encuentra una letra de la 2da palabra dentro de la primera, corto
                return False
                break
        return True
    else :
        return False                         # si termino el for es porque encontro todas las letras de la 2da palabra en la primer palabra