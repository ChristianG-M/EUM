#!/usr/bin/python3
import os
import os.path
import subprocess
import filecmp
import time

class confTeclado():
	def __init__(self):
		pass

	def validarIdioma(self):
		res = filecmp.cmp('/etc/default/keyboard', './keyboard')
		if(res):			
			return True
		else:
			return False

	def configurarIdioma(self):
		print("¡Creando Backup!")
		time.sleep(5)
		copyBkp = 'cp /etc/default/keyboard /etc/default/keyboard.old'
		os.system('sudo -S %s' % (copyBkp))

		print("¡Eliminando configuracion anterior!")
		time.sleep(5)
		copyBkp = 'rm /etc/default/keyboard'
		os.system('sudo -S %s' % (copyBkp))

		print("¡Revisando Archivos!")
		check = 'ls /etc/default/ | grep "keyboard"'
		os.system('sudo -S %s' % (check))
		time.sleep(5)

		print("¡Copiando nueva configuracion!")
		copyUS = 'cp ./keyboard /etc/default/'
		os.system('sudo -S %s' % (copyUS))
		time.sleep(5)

		print("¡Revisando Archivos!")
		check = 'ls /etc/default/ | grep "keyboard"'
		os.system('sudo -S %s' % (check))
		time.sleep(5)

		print("¡Reiniciando el sistema...!")
		time.sleep(5)
		
		command = 'reboot'
		os.system('sudo -S %s' % (command))

def main():
	configuracion = confTeclado()
	result = configuracion.validarIdioma()
	if(result):
		print("¡Teclado configurado!")
	else:
		configuracion.configurarIdioma()
	print(result)

if __name__ == "__main__":
	main()