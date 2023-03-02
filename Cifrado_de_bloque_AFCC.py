"""
    # Al inicio del prograa lo que haremos sera definir las variables que usaremos 
    # En este caso seran 4 diccionarios que nos ayudaran a obtener las equivalencias respectivas
"""
# abe_num es un diccionario que nos regrese el valor en entero dependiendo de la letra
abe_num = {
    'A':  1, 'B':  2, 'C':  3, 'D':  4,
    'E':  5, 'F':  6, 'G':  7, 'H':  8,
    'I':  9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'Ñ': 15, 'O': 16,
    'P': 17, 'Q': 18, 'R': 19, 'S': 20,
    'T': 21, 'U': 22, 'V': 23, 'W': 24,
    'X': 25, 'Y': 26, 'Z': 27    
}

# abe_bin es un diccionario que nos regrese el arreglo binario de una letra 
num_bin = {
    1:  '00001', 2:  '00010', 3:  '00011', 4:  '00100',
    5:  '00101', 6:  '00110', 7:  '00111', 8:  '01000',
    9:  '01001', 10: '01010', 11: '01011', 12: '01100',
    13: '01101', 14: '01110', 15: '01111', 16: '10000',
    17: '10001', 18: '10010', 19: '10011', 20: '10100',
    21: '10101', 22: '10110', 23: '10111', 24: '11000',
    25: '11001', 26: '11010', 27: '11011'
}

# bin_abe es un diccionario que nos regrese una letra dependiendp de un arreglo binario
bin_abe = {
    '00001': 'A', '00010': 'B', '00011': 'C', '00100': 'D',
    '00101': 'E', '00110': 'F', '00111': 'G', '01000': 'H',
    '01001': 'I', '01010': 'J', '01011': 'K', '01100': 'L',
    '01101': 'M', '01110': 'N', '01111': 'Ñ', '10000': 'O',
    '10001': 'P', '10010': 'Q', '10011': 'R', '10100': 'S',
    '10101': 'T', '10110': 'U', '10111': 'V', '11000': 'W',
    '11001': 'X', '11010': 'Y', '11011': 'Z' 
}

"""
    # Definimos la cadena con la que vamos a trabajar
    # En este caso la dividiremos en un trosos de 8 caracteres lo cual nos dara 3 cadenas 
    # Esas a su vez las dividiremos en 2 y asi tendremos 1 lista con 6 arreglo de 4 caracteres
"""

# Lista 1 con los primeros 8 caracteres 
lista8Caracteres = ["CRIP", "TOGR", "AFIA", "ESUN", "ACIE", "NCIA"]

"""
    # Definimos la  funcion que hara el la operacion de sustitucion
    # Parametro de entrada 
    ## Areglo de 4 caracteres
    # Parametro de salida
    ## Areglo de 4 caracteres
"""

def Sustitucion(arr4Car: str, dicAbeNum: dict, dicNumBin: dict) -> list:
    lisAux = []
    print('*************************************')
    print(arr4Car)
    print('*************************************')
    
    for elemnt in arr4Car:
        valNum = dicAbeNum[elemnt]
        valNumSust = (valNum + 1) % 27
        valBin = dicNumBin[valNumSust]
        lisAux.append(valBin)
    
    print(lisAux)
    print('*************************************')
    return lisAux

def Permutacion(lista: list) -> list:
    listaAux = []
    listaAux.append(lista[2])
    listaAux.append(lista[1])
    listaAux.append(lista[3])
    listaAux.append(lista[0])
    
    print(listaAux)
    print('*************************************')
    return listaAux

          
F = Permutacion(Sustitucion(arr4Car=lista8Caracteres[1], dicAbeNum=abe_num, dicNumBin=num_bin))
        
"""    
aregloSutituido = Sustitucion(ar4Car=lista8Caracteres[1], dic1=abe_num, dic2=num_abe)

arregloPermuted = Permutacion(aregloSutituido)

posLi = 0
posKi = 1
for i in range(2):
    arregloSutituido = Sustitucion(ar4Car=lista8Caracteres[posKi], dic1=abe_num, dic2=num_abe)
"""