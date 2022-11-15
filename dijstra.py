import math

class Vertice:

	def __init__(self, i):

		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')

	def agregarVecino(self, v, p):
		
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Grafica:
	
	def __init__(self):
		
		self.vertices = {}

	def agregarVertice(self, id):
		
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, a, b, p):
		
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		
		for v in self.vertices:
			print("El costo del vértice "+str(self.vertices[v].id)+" es "+ str(self.vertices[v].costo)+" llegando desde "+str(self.vertices[v].padre))
			
	
	def camino(self, a, b):
		
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)
			actual = self.vertices[actual].padre
		return [camino, self.vertices[b].costo]

	def minimo(self, l):
		
		if len(l) > 0:
			m = self.vertices[l[0]].costo
			v = l[0]
			for e in l:
				if m > self.vertices[e].costo:
					m = self.vertices[e].costo
					v = e
			return v
		return None

	def dijkstra(self, a):
		
		if a in self.vertices:
			# 1 y 2
			self.vertices[a].costo = 0
			actual = a
			noVisitados = []
			
			for v in self.vertices:
				if v != a:
					self.vertices[v].costo = float('inf')
				self.vertices[v].padre = None
				noVisitados.append(v)

			while len(noVisitados) > 0:
				#3
				for vec in self.vertices[actual].vecinos:
					if self.vertices[vec[0]].visitado == False:
						# 3.a
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
							self.vertices[vec[0]].padre = actual

				# 4
				self.vertices[actual].visitado = True
				noVisitados.remove(actual)

				# 5 y 6
				actual = self.minimo(noVisitados)
		else:
			return False

def main():
	g = Grafica()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarArista(2, 3, 2)
	g.agregarArista(2, 5, 1)
	g.agregarArista(2, 6, 12)
	g.agregarArista(3, 4, 4)
	g.agregarArista(3, 5, 3)
	g.agregarArista(5, 4, 3)
	g.agregarArista(6, 5, 4)
	g.agregarArista(4, 1, 6)
	g.agregarArista(6, 1, 10)
    

	print("\n\nLa ruta más rápida por Dijkstra junto con su costo es:")
	g.dijkstra(2)
	print(g.camino(2, 1))
	print("\nLos valores finales de la gráfica son los siguietes:")
	g.imprimirGrafica()