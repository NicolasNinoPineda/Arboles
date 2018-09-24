class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))

def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None   

def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad,arbol.hijos)) 

def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)

def printElement(element):
    print element
    ##ejecutarProfundidadPrimero(arbol, printElement)



arbol = Arbol(0)
agregarElemento(arbol, 1, 0)
agregarElemento(arbol, 2, 0)
agregarElemento(arbol, 2.1, 2)
agregarElemento(arbol, 3, 0)
agregarElemento(arbol, 3.1, 3)
agregarElemento(arbol, 3.2, 3)
agregarElemento(arbol, 3.3, 3)
ejecutarProfundidadPrimero(arbol, printElement)