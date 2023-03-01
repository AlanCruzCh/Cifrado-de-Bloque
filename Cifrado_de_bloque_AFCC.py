"""
    # Al inicio del prograa lo que haremos sera definir las variables que usaremos 
    # En este caso seran 3 diccionarios que nos ayudaran a obtener las equialencias
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

# abe_num es un diccionario que nos regresa una lertra dependiendo de un numero entero
num_abe = {
    1:  'A', 2:  'B', 3:  'C', 4:  'D',
    5:  'E', 6:  'F', 7:  'G', 8:  'H',
    9:  'I', 10: 'J', 11: 'K', 12: 'L',
    13: 'M', 14: 'N', 15: 'Ñ', 16: 'O',
    17: 'P', 18: 'Q', 19: 'R', 20: 'S',
    21: 'T', 22: 'U', 23: 'V', 24: 'W',
    25: 'X', 26: 'Y', 27: 'Z'    
}

# abe_bin es un diccionario que nos regrese el arreglo binario de una letra 
abe_bin = {
    'A': '00001', 'B': '00010', 'C': '00011', 'D': '00100',
    'E': '00101', 'F': '00110', 'G': '00111', 'H': '01000',
    'I': '01001', 'J': '01010', 'K': '01011', 'L': '01100',
    'M': '01101', 'N': '01110', 'Ñ': '01111', 'O': '10000',
    'P': '10001', 'Q': '10010', 'R': '10011', 'S': '10100',
    'T': '10101', 'U': '10110', 'V': '10111', 'W': '11000',
    'X': '11001', 'Y': '11010', 'Z': '11011'
}

# bin_abe es un diccionario que nos regrese una letra dependiendp de un arreglo binario
bin_abe = {
    '00001': 'A', '00010': 'B', 3: 'C', 4: 'D',
    '00101': 'E', '00110': 'F', 7: 'G', 8: 'H',
    '01001': 'I', '01010': 'J', 11: 'K', 12: 'L',
    '01101': 'M', '01110': 'N', 15: 'Ñ', 16: 'O',
    '10001': 'P', '10010': 'Q', 19: 'R', 20: 'S',
    '10101': 'T', '10110': 'U', 23: 'V', 24: 'W',
    '11001': 'X', '11010': 'Y', 27: 'Z' 
}