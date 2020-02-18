#!/usr/bin/python3
import json
import paramiko
from paramiko import client
from paramiko import SSHClient
from scp import SCPClient
import time
import sys

class inServer():
	def __init__(self):
		pass


	def sendFile(self, ip, user, password, pathFrom, pathTo, file):
		try:
			client = paramiko.SSHClient()
			paramiko.util.log_to_file("paramiko.log")
			client.load_system_host_keys()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(hostname=ip, port=22, username=user,password=password)
			sftp = client.open_sftp()
			sftp.put(pathFrom, pathTo)
			command = 'ls ' + str(pathTo)
			stdin, stdout, stderr = client.exec_command(command)
			recibido = stdout.readlines()
			match = [ s for s in recibido if file in s ]
			print(match)
			time.sleep(0.1)
			client.close()
		except:
			print("Error en la conexion SSH")


def main():
	try:
		ip = str(sys.argv[1])
		user = str(sys.argv[2])
		password = str(sys.argv[3])
		pathFrom = str(sys.argv[4])
		pathTo = str(sys.argv[5])
		file = str(sys.argv[6])
		newSendConf = inServer()
		newSendConf.sendFile(ip, user, password, pathFrom, pathTo, file)
	except Exception as error:
		print ("Exception:", error)


if __name__ == "__main__":
	main()