"""
    @reroes
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellidos": "Elizalde"}

print("Imprimir diccionario")
for l in diccionario.keys():
    # print(diccionario[l])
    print("Mi nombre es: %s y mi apellido es: %s" % ( diccionario.get('nombre'), diccionario.get('apellidos') ) )

