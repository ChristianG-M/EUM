#!/usr/bin/python3
import configparser
import codecs
from os import system, name
from time import sleep
import sys
import re

class viewData():
	def __init__(self):
		pass

	def getInfo(self):
		global categorias
		global opciones
		global config

		categorias = []
		opciones = []

		config = configparser.ConfigParser()
		config.read('configuracion.ini')

		for section_name in config.sections():
			categorias += [section_name]
			opciones += [config.options(section_name)]


	def menuCategorias(self):
		global categorias

		sleep(0.3)
		system('clear')
		print("\t\tEditar archivo")
		print("\t    Seleccione la categoria")
		for i in range(0, len(categorias)):
			print("{} - {}".format((i+1), categorias[i]))
		print("0 - Salir")

		opcion = int(input("\nIngrese opcion: "))
		while( opcion > len(categorias) ):
			opcion = int(input("\nIngrese una opcion valida: "))

		if( opcion == 0 ):
			sys.exit(0)
		else:
			self.menuElemento(opcion)		


	def menuElemento(self, opcion):
		global categorias
		global opciones

		sleep(0.3)
		system('clear')
		print("\t\tEditar archivo")
		print("\t    Seleccione el elemento")
		print("\t",categorias[(opcion-1)])
		for x in range(0, len(opciones[(opcion-1)])):
			print("{} - {}".format((x+1), opciones[(opcion-1)][x]))
		print("0 - Regresar")

		opcion2 = int(input("\nIngrese opcion: "))
		while( opcion2 > len(opciones[(opcion-1)]) ):
			opcion2 = int(input("\nIngrese una opcion valida: "))

		if( opcion2 == 0 ):
			self.menuCategorias()
		else:
			self.printElemento(opcion, opcion2)


	def printElemento(self, opcion, opcion2):
		global categorias
		global opciones
		global config

		sleep(0.3)
		system('clear')
		print("\t\tEditar archivo")
		print("\t",categorias[(opcion-1)])
		campo = opciones[(opcion-1)][(opcion2-1)]
		print('{} = {}'.format(opciones[(opcion-1)][(opcion2-1)], config.get(str(categorias[(opcion-1)]), str(campo))))
		print("\n1 - Editar")
		print("0 - Regresar")

		opcion3 = int(input("\nIngrese opcion: "))
		while( opcion3 > 1 ):
			opcion3 = int(input("\nIngrese una opcion valida: "))

		if( opcion3 == 1 ):
			self.editarElemento(campo, opcion, opcion2)
		elif( opcion3 == 0 ):
			self.menuElemento(opcion)



	def editarElemento(self, campo, opcion, opcion2):
		global config
		print("\nIngrese nuevo valor para ", campo, ": ")
		update = str(input())
		config[(categorias[(opcion-1)])][opciones[(opcion-1)][(opcion2-1)]] = update
		with open('configuracion.ini', 'w') as configFile:
			config.write(configFile)
		self.printElemento(opcion, opcion2)


	def getValue(self, categoria, opcion):
		print(config.get(str(categoria), str(opcion)))


	def editValue(self, categoria, opcion):
		global config
		print("\nIngrese nuevo valor para ", opcion, ": ")
		update = str(input())
		config[str(categoria)][str(opcion)] = update
		with open('configuracion.ini', 'w') as configFile:
			config.write(configFile)


def main():
	vizualizar = viewData()
	vizualizar.getInfo()
	#vizualizar.getValue('CONTROLADORA2','version_tc')
	#vizualizar.editValue('RED','gateway')
	vizualizar.menuCategorias()


if __name__ == "__main__":
    main()