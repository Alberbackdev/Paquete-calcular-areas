'''
Realiza un POO  que calcule el area y perimetro de un rectangulo
donde:
altura(h)=7cm
base(b)= 10 cm
Formula de Area(A):
A=b.h
Perimetro= 2.h + 2.b
1.1- Crear archivo para implementar modulo: "import areaR" o "from areaR import*"
1.2- crear el archivo de la raiz
2-Parte
2.1-Crear carpeta  con el nombre Miprimerpaquete con los archivos:
__init__.py --> archivo inicial
Sumar.py --> funcion sumar
Restar.py --> Funcion restar
2.1.1 - Crear subpaquete con el nombre Áreas con los archivos:
__init__.py --> archivo de inicio
areaR.py archivo ya creado
AreaT.py archivo por crear
3- Parte
Crear los paquetes Distribuibles
3.1 hacer config de l setup.py
3.2 instalarlo en el ordenador

Nota Todo Grabado desde el comienzo
'''
class Area():
	"""docstring for Rectangulo"""
	def __init__(self):
		self.altura = 7
		self.base = 10

	def area_rectangulo(self):
		a=self.base * self.altura
		return "El Area del Rectangulo es:", a,"cm"

	def perimetro_rectangulo(self):
		p=(2*self.base) + (2*self.altura)
		return "El Perimetro del Rectangulo es de: ", p, "cm"


