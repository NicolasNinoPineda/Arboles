class Nodo:
	def__init__(self,valor=None,padre=None,is_raiz=False,is_izq=False,is_der=False):
		self.valor=valor
		self.izq=None
		self.der=None
		self.padre=padre
		self.is_raiz=is_raiz
		self.is_izq=is_izq
		self.is_der=is_der

class ArbolBinario():
	def__init__(self):
		self.raiz=None

	def vacio():
		if self.raiz == None:
			return True
		else:
			return False

	def add(self, valor):
		if self.vacio():
			self.raiz=nodo(valor=valor, is_raiz=True)
		else:
			nodo= self.__get_place(valor)
			if  valor<= nodo.valor:
				nodo.izq = Nodo(volor=valor,padre=nodo,is_izq=True)
			else:
				nodo.der = Nodo(volor=valor,padre=nodo,is_der=True)

	def __get_place(self,valor):
		aux=self.raiz
		while aux :
			temp = aux
			if valor <= aux.valor:
				aux=aux.izq
			else:
				aux=aux.der
		return temp


	def buscar(self,nodo,valor):
		if nodo==None:
			return False
		elif nodo.valor==valor:
			return nodo
		elif nodo.valor>=valor:
			return self.buscar(nodo.izq,valor)
		else:
			return self.buscar(nodo.der,valor)



arbol= ArbolBinario()
arbol.add(8)
arbol.add(10)
arbol.add(3)
arbol.add(14)
arbol.add(13)
arbol.add(1)
arbol.add(6)
arbol.add(4)
arbol.add(7)
print (arbol.buscar(arbol.raiz,8).valor)