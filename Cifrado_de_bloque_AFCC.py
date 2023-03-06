"""
    # Al inicio del prograa lo que haremos sera definir las variables que usaremos 
    # En este caso seran 4 diccionarios que nos ayudaran a obtener las equivalencias respectivas
"""
# abe_num es un diccionario que nos regrese el valor en entero dependiendo de la letra del abecedario 
abe_num = {
    'A':  0, 'B':  1, 'C':  2, 'D':  3,
    'E':  4, 'F':  5, 'G':  6, 'H':  7,
    'I':  8, 'J':  9, 'K': 10, 'L': 11,
    'M': 12, 'N': 13, 'Ñ': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22, 'W': 23,
    'X': 24, 'Y': 25, 'Z': 26    
}

# num_binario es un diccionario que nos regresa la equivalencia en binario de un numero 
num_bin = {
    0:  '00001', 1:  '00010', 2:  '00011', 3:  '00100',
    4:  '00101', 5:  '00110', 6:  '00111', 7:  '01000',
    8:  '01001', 9:  '01010', 10: '01011', 11: '01100',
    12: '01101', 13: '01110', 14: '01111', 15: '10000',
    16: '10001', 17: '10010', 18: '10011', 19: '10100',
    20: '10101', 21: '10110', 22: '10111', 23: '11000',
    24: '11001', 25: '11010', 26: '11011'
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

# Lista con el contenido de nuestra texto a cifrar 
lista8Caracteres = ["CRIP", "TOGR", "AFIA", "ESUN", "ACIE", "NCIA"]

"""
    # Definimos la  funcion que hara el la operacion de sustitucion
    
    # Parametro de entrada 
    ## String de 4 caracteres
    ## Diccionario de letra a numero 
    ## Diccionario de numero a binario
    
    # Parametro de salida
    ## Lista 
"""

def Sustitucion(arr4Car: str, dicAbeNum: dict, dicNumBin: dict) -> list:
    lisAux = []
    
    for elemnt in arr4Car:
        valNum = dicAbeNum[elemnt]
        valNumSust = (valNum + 1) % 27
        valBin = dicNumBin[valNumSust]
        lisAux.append(valBin)
        
    return lisAux

"""
    # Definimos la  funcion que hara el la operacion de Sustitucion
    
    # Parametro de entrada 
    ## Lista
    
    # Parametro de salida
    ## Lista 
"""

def Permutacion(lista: list) -> list:
    listaAux = []
    
    listaAux.append(lista[2])
    listaAux.append(lista[1])
    listaAux.append(lista[3])
    listaAux.append(lista[0])
    
    return listaAux

"""
    # Definimos la funcion que nos permitira saber la equivalencia de una Caracter a un arreglo binario
    
    # Parametro de entrada 
    ## String de 4 caracteres
    ## Diccionario de Abecedario a Numero
    ## Diccionario de Numero a Binario
    
    # Parametro de salida
    ## Lista 
"""
def ConvertirAbeBin(arreglo: str, dicAbeNum: dict, dicNumBin: dict)-> list:
    listAux = []
    
    for caracter in arreglo:
        valNum = dicAbeNum[caracter]
        valBin = dicNumBin[valNum]
        listAux.append(valBin)
    
    return listAux

"""
    # Definimos la funcion que nos valida que un string de numero binarios no pase de 27
    
    # Parametro de entrada 
    ## Lista
    ## Diccionario de numero a binario
    
    # Parametro de salida
    ## Lista 
"""
def AplicarMod27(strBin: str, dicNumBin: dict) -> str:
    numero_decimal = 0
    
    for posicion, digito_sting in enumerate(strBin[::-1]):
        numero_decimal += int(digito_sting) * 2 ** posicion
        
    valor = numero_decimal % 27
    
    return dicNumBin[valor]

"""
    # Definimos la funcion que usamos para convertir una lsita de arreglo binario a un string
    
    # Parametro de entrada 
    ## Lista
    ## Diccionario de Binario a Letra
    
    # Parametro de salida
    ## Lista 
"""
def ConvertirBinAbe(listArr: list, dicBinAbe: dict) -> str:
    strAbe = ""
    
    for elemento in listArr:
        strAbe = strAbe + dicBinAbe[elemento]
    
    return strAbe

"""
    # Definimos la funcion que realiza la operacion de la XOR 
    
    # Parametro de entrada 
    ## Lista 1 
    ## Lista 2
    
    # Parametro de salida
    ## String
"""
def OperacionOrExclusiva(listaLi: list, listaFRi: list) -> str:
    listAux = []
    
    for posicion in range(len(listaLi)):
        
        arreBinLi = listaLi[posicion]
        arrgBinFRi = listaFRi[posicion]
        lisBinLi = []
        listBinFRi = []
        arregloAux = ""
        
        for elemnto in arreBinLi:
            lisBinLi.append(elemnto)
            
        for elemento in arrgBinFRi:
            listBinFRi.append(elemento)
            
        for iterador in range(len(lisBinLi)):
            valOpeOrExc = int(lisBinLi[iterador]) ^ int(listBinFRi[iterador]) 
            arregloAux += str(valOpeOrExc)
            
        listAux.append(AplicarMod27(strBin=arregloAux, dicNumBin=num_bin))
        
    return ConvertirBinAbe(listArr=listAux, dicBinAbe=bin_abe)
 
 
"""
    * Iniciamos el segmento del programa
"""
print("\n***********************************************************")
print("Texto plano")
print(lista8Caracteres)
print("***********************************************************\n")           

for i in range(2):
    
    FRi = Permutacion(Sustitucion(arr4Car=lista8Caracteres[1], dicAbeNum=abe_num, dicNumBin=num_bin))
    Li = ConvertirAbeBin(arreglo=lista8Caracteres[0], dicAbeNum=abe_num, dicNumBin=num_bin)
    LixFri = OperacionOrExclusiva(listaLi=Li, listaFRi=FRi)
    lista8Caracteres[0] = lista8Caracteres[1]
    lista8Caracteres[1] = LixFri
    
    FRi = Permutacion(Sustitucion(arr4Car=lista8Caracteres[3], dicAbeNum=abe_num, dicNumBin=num_bin))
    Li = ConvertirAbeBin(arreglo=lista8Caracteres[2], dicAbeNum=abe_num, dicNumBin=num_bin)
    LixFri = OperacionOrExclusiva(listaLi=Li, listaFRi=FRi)
    lista8Caracteres[2] = lista8Caracteres[3]
    lista8Caracteres[3] = LixFri
    
    FRi = Permutacion(Sustitucion(arr4Car=lista8Caracteres[5], dicAbeNum=abe_num, dicNumBin=num_bin))
    Li = ConvertirAbeBin(arreglo=lista8Caracteres[4], dicAbeNum=abe_num, dicNumBin=num_bin)
    LixFri = OperacionOrExclusiva(listaLi=Li, listaFRi=FRi)
    lista8Caracteres[4] = lista8Caracteres[5]
    lista8Caracteres[5] = LixFri
    
    print("\n***********************************************************")
    print(lista8Caracteres)
    print("***********************************************************\n")   
    
print("\n***********************************************************")
print("Texto cifrado")
print(lista8Caracteres)
print("***********************************************************\n")          