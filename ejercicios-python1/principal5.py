"""
    @reroes
    Manejo de estructuras
"""

diccionario  = {"nombre": "René", "apellidos": "Elizalde"}
diccionario2 = {"nombre": "Daniel", "apellidos": "Tinizaray"}   # Estos 2 diccionarios

lista = [diccionario, diccionario2]                             # se guardan en una lista

print("Imprimir diccionario")
for l in lista:
    # print(diccionario[l])
    miDiccionario = l

    print("Mi nombre es: %s y mi apellido es: %s" % ( miDiccionario["nombre"], miDiccionario["apellidos"] ) )

