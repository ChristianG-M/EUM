#!/usr/bin/python3
import paramiko
from paramiko import client
from paramiko import SSHClient
from scp import SCPClient
import time

try:
	client = paramiko.SSHClient()
	paramiko.util.log_to_file("paramiko.log")
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname='192.168.1.95', port=22, username='cajero',password='eum')
	sftp = client.open_sftp()
	sftp.get('/home/cajero/Documentos/eum/app/configServer.json','/home/dl17/Documentos/EUM/Python/Pruebas/ssh/configServer.json')
	time.sleep(0.1)
	client.close()
except:
	print("Error en la conexion SSH")