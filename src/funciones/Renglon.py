def RenglonMasLargo(titulos_separados):
    cantidadPalabras = 0
    for lista in titulos_separados:
        if len(lista) > cantidadPalabras :
            cantidadPalabras = len(lista)
            listaMaxima = lista
    print(listaMaxima)