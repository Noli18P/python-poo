class producto:
	def __init__(self, codigo, nombre, precio):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__precio = precio

	#Getter
	@property
	def codigo(self):
		return self.__codigo


	@property
	def nombre(self):
		return self.__nombre
	

	@property
	def precio(self):
		return self.__precio
	

	#Setter
	@codigo.setter
	def codigo(self, valor):
		self.__codigo = valor


	@nombre.setter
	def nombre(self,valor):
		self.__nombre = valor


	@precio.setter
	def precio(self,valor):
		self.__precio = valor


	#To string
	def __str__(self):
		return 'Codigo: ' + str(self.__codigo) + ' Nombre: ' + str(self.__nombre) + ' Precio: ' + str(self.__precio)  

	#Metodo
	def calcular_total(self, unidades):
		total = self.precio * unidades

		return total

class Pedido:
	def __init__(self,productos,cantidades):
		self.__productos = productos
		self.__cantidades = cantidades

	def total_pedido(self):
		total = 0
			
		for (p,c) in zip(self.__productos,self.__cantidades):
			total += p.calcular_total(c)

		return total


	def mostrar_productos(self):
		for (p,c) in zip(self.__productos,self.__cantidades):
			print('Producto -> ', p.nombre, ' Cantidad -> ' + str(c))


p1 = producto(1, 'Producto 1', 5)
p2 = producto(2, 'Producto 2', 10)
p3 = producto(1, 'Producto 3', 15)

productos = [p1,p2,p3]
cantidades = [5,10,2]

mi_pedido = Pedido(productos, cantidades)


print('Total de productos: ',mi_pedido.total_pedido())
mi_pedido.mostrar_productos()