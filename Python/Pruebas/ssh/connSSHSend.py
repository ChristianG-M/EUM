#!/usr/bin/python3
import json
import paramiko
from paramiko import client
from paramiko import SSHClient
from scp import SCPClient
import time
import sys
from serverConnSSHSend import serverConnSSHSend
import os.path

class connSSHSend():
	def __init__(self):
		pass


	def getFileConf(self, ip, user, password, pathFrom, pathTo, file):
		try:
			client = paramiko.SSHClient()
			paramiko.util.log_to_file("paramiko.log")
			client.load_system_host_keys()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(hostname=ip, port=22, username=user,password=password)
			local = str(pathFrom)+str(file)
			remoto = str(pathTo)+str(file)
			sftp = client.open_sftp()
			sftp.get(remoto,local)
			time.sleep(0.1)
			client.close()
		except:
			print("Error en la conexion SSH")


	def getDatos(self):
		try:
			if(os.path.exists('configServer.json')):
				with open('configServer.json', 'r') as f:
					data = json.loads(f.read())
				return data
			else:
				print("El archivo no existe")
		except Exception as error:
			print ("Exception:", error)


	def printEquipos(self, data, file):
		try:
			for i in range(0, len(data['EQUIPOS'])):
				print((i+1),"Usuario:",data['EQUIPOS'][i]['usuario'],"- IP:",data['EQUIPOS'][i]['ip_address'])
			opcion = int(input("\nIngrese opcion: "))
			while( opcion > len(data['EQUIPOS']) ):	
				opcion = int(input("\nIngrese una opcion valida: "))
			self.executeCmd(data, opcion, file)
		except Exception as error:
			print ("Exception:", error)


	def executeCmd(self, data, opcion, file):
		try:
			ip = str(data['EQUIPOS'][(opcion-1)]['ip_address'])
			user = str(data['EQUIPOS'][(opcion-1)]['usuario'])
			password = str(data['EQUIPOS'][(opcion-1)]['password'])
			FromPath = '/home/cajero/Documentos/eum/app/prueba.json'
			ToPath = '/home/'+user+'/Documentos/'+file
			client = paramiko.SSHClient()
			paramiko.util.log_to_file("paramiko.log")
			client.load_system_host_keys()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(hostname='192.168.1.95', port=22, username='cajero',password='eum')
			command = 'python3 /home/cajero/Documentos/eum/app/inServer.py ' +  ' ' + ip + ' ' + user + ' ' + password + ' ' + FromPath + ' ' + ToPath + ' ' + file 
			print(command)
			stdin, stdout, stderr = client.exec_command(command)
			print(stdout.readlines())
			print(stderr.readlines())
			time.sleep(0.1)
			client.close()	
		except Exception as error:
			print ("Exception:", error)


def main():
	try:
		ip = '192.168.1.95'
		user = 'cajero'
		password = 'eum'
		pathFrom = '/home/dl17/Documentos/EUM/Python/Pruebas/ssh/'
		pathTo = '/home/cajero/Documentos/eum/app/'
		file = 'prueba.json'
		newSendConf = serverConnSSHSend()
		newSendConf.sendConfig(ip, user, password, pathFrom, pathTo, file)
	except Exception as error:
		print ("Exception:", error)

	time.sleep(1)

	try:
		ip = '192.168.1.95'
		user = 'cajero'
		password = 'eum'
		pathFrom = '/home/dl17/Documentos/EUM/Python/Pruebas/ssh/'
		pathTo = '/home/cajero/Documentos/eum/app/'
		file = 'configServer.json'
		new_file = 'prueba.json'
		newSendConfD = connSSHSend()
		newSendConfD.getFileConf(ip, user, password, pathFrom, pathTo, file)		
		datosD = newSendConfD.getDatos()
		newSendConfD.printEquipos(datosD, new_file)
	except Exception as error:
		print ("Exception:", error)


if __name__ == "__main__":
	main()