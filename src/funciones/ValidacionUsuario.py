import string
import random

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
    

def validarUsuario15(user,fecha,resto):
    if (len(user) < 16) : # verifico si tengo los 15 caracteres del usuario
        cant = (30 - (len(user) + len(fecha))) # aca me quedo con cuantos caracteres me faltan agregar para que se cree el codigo de descuento
        print('se rellenara el codigo de descuento con :',cant , 'de caracteres aleatorios')
        codigo = ""
        nombre = user.upper()
        for i in range(cant) :                      # aca voy a repetir x veces
            codigo = codigo + random.choice(resto)  # por cada iteracion me traigo un caracter de la variable resto que tiene cargada los nums y letras mayusculas
        codigo = f"{nombre}-{fecha}-{codigo}"
        return codigo
    else :
        codigo = "se superaron los 15 caracteres validos para la generacion del codigo!"
    return codigo