#!/usr/bin/python3
import paramiko
from paramiko import client
from paramiko import SSHClient
from scp import SCPClient
import time
import sys

class serverConnSSHSend():
	def __init__(self):
		pass


	def sendConfig(self, ip, user, password, pathFrom, pathTo, file):
		try:
			client = paramiko.SSHClient()
			paramiko.util.log_to_file("paramiko.log")
			client.load_system_host_keys()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(hostname=str(ip), port=22, username=str(user),password=str(password))
			sftp = client.open_sftp()
			local = str(pathFrom)+str(file)
			remoto = str(pathTo)+str(file)
			sftp.put(str(local), str(remoto))			
			command = 'ls '+str(pathTo)
			stdin, stdout, stderr = client.exec_command(command)
			recibido = stdout.readlines()
			match = [ s for s in recibido if str(file) in s ]
			print(match)
			time.sleep(0.1)
			client.close()
		except:
			print("Error en la conexion SSH")


def main():
	try:
		ip = '192.168.1.95'
		user = 'cajero'
		password = 'eum'
		pathFrom = '/home/dl17/Documentos/EUM/Python/Pruebas/PSQL/'
		pathTo = '/home/cajero/Documentos/eum/app/'
		file = 'configServer.json'
		newSendConf = serverConnSSHSend()
		newSendConf.sendConfig(ip, user, password, pathFrom, pathTo, file)
	except Exception as error:
		print ("Exception:", error)


if __name__ == "__main__":
	main()