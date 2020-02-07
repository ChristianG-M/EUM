#!/usr/bin/python3
import os
import os.path
import subprocess

class confTeclado():
	def __init__(self):
		pass

	def validarConf(self):
		if(os.path.exists("keyboard.conf")):
			f=open("keyboard.conf", "r")
			contents =f.read()
			if('1' in contents):
				configurado = "Ya esta configurado"
				return True
			else:				
				print("Configurando...")
				self.confMetodTeclado()
		else:				
			print("Configurando...")
			self.confMetodTeclado()

	def confMetodTeclado(self):		
		copyBkp = 'cp /etc/default/keyboard /etc/default/keyboard.old'
		p = os.system('sudo -S %s' % (copyBkp))
		check = 'ls /etc/default/'
		q = os.system('sudo -S %s' % (check))
		copyUS = 'cp ./keyboard /etc/default/'
		r = os.system('sudo -S %s' % (copyUS))
		print(1, file=open("keyboard.conf", "a"))
		command = 'reboot'
		s = os.system('sudo -S %s' % (command))
		return True

def main():
	configuracion = confTeclado()
	result = configuracion.validarConf()
	print(result)

if __name__ == "__main__":
	main()