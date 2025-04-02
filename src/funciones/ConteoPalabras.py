def comparar(palabra,lista):       #esta funcion recorre cada lista de mi tupla de descripciones y verifica si se encuentra la palabra pasada por parametro
    for elem in lista :             # me guardo en elem los elementos de la lista,osea cada palabra
        if palabra in elem.lower().split() : #paso a minuscula la palabra, las separo con el .split(), comparo con la palabra exacta
            return True
    else :
        return False

def conteo(descrip):  
    m = 0
    e = 0
    c = 0
    for lista in descrip :      #esta funcion le manda la palabra a buscar a la lista y si retorna true va acumulara en el valor de cada clave 1+
        print('recorrera la lista ', lista)
        if comparar('música',lista) :
            m += 1
            print('sumo m')

        if comparar('entretenimiento',lista) :
            e += 1
            print('sumo e')

        if comparar('charla',lista):
            c += 1
            print('sumo c')
    menciones = {'musica' : m,
                'entretenimiento' : e,
                'charla' : c}
    print('Menciones de musica :' ,menciones['musica'] )
    print('Menciones de entretenimiento :' ,menciones['entretenimiento'])
    print('Menciones de charla : ',menciones['charla'])
        