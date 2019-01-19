class Numeros(object):
	def __init__(self,lista):
		self.lista = lista

	def agregar_lista(self,lista):
		self.lista = lista

	def obtener_lista(self):
		return self.lista
#Mediante la siguiente clase convertimos los datos de la lista recibida a listan
class Convertir_lista(object):
	def __init__(self,lista):
		self.lista = lista

	def lista_nueva(self):
		listan = []

		for d in self.lista:
			for p in d:
				n = int(p)
				listan.append(n)
		listan.sort(key=int)

		return listan
# Mediante la siguiente clase se utiliza el algoritmo de busqueda binaria
class busqueda():


	def __init__(self, lista):
		self.lista = lista
		print(self.lista)

	def busqueda_posicion(self, elemento):
		self.elemento = elemento
		self.inferior = 0
		self.superior = len(self.lista)
		self.medio = int((self.inferior + self.superior) / 2)
		self.ubicacion = -1

		while (self.inferior <= self.superior) and (self.ubicacion == -1):
			if self.elemento == self.lista[self.medio]:
				self.ubicacion = self.medio
			elif (self.elemento < self.lista[self.medio]):
				self.superior = self.medio-1
			else:
				self.inferior = self.medio+1
			self.medio= int((self.inferior + self.superior + 1) / 2)

		return self.ubicacion



