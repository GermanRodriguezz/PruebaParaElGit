import string

digitos = string.digits
Mayusculas = string.ascii_uppercase
letras = string.ascii_letters

def esMayus(caracter) :
    return caracter in Mayusculas

def esNum(caracter) :
    return caracter in digitos

def esLetra(caracter):
    return caracter in letras

def validarUsuario(usuario) :
    if len(usuario) > 4 : # correcto
        puede = True
        for i in usuario :
            if esMayus(i) or esNum(i) or esLetra(i):
                puede = True
            else :
                puede = False
                break
        return puede
        