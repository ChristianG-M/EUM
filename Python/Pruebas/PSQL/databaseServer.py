#!/usr/bin/python3
import psycopg2
import json
import os.path

class databaseServer():
	def __init__(self):
		pass


	def createJsonServer(self):		
		data = '{\
			"SERVER":[{\
				"numero_serie":"354351435151ae5413",\
				"nombre":"Server Principal",\
				"id_sucursal":"3",\
				"version_app":"2.1",\
				"ubicacion":"Vips",\
				"actualizacion_automatica":"False"\
			}],\
			\
			"RED":[{\
				"server_ip_address":"192.168.1.64",\
				"port":"2324",\
				"gateway":"192.168.1.1"\
			}],\
			\
			"EQUIPOS":[{\
				"id":"0",\
				"numero_serie":"54651",\
				"ip_address":"0.0.0.0",\
				"usuario":"x",\
				"password":"x"\
			},\
			{\
				"id":"1",\
				"numero_serie":"63543654a35e4354ae",\
				"ip_address":"192.168.1.95",\
				"usuario":"cajero",\
				"password":"eum"\
			},\
			{\
				"id":"2",\
				"numero_serie":"63543sdfe4354ae",\
				"ip_address":"192.168.1.90",\
				"usuario":"eum",\
				"password":"eum"\
			}],\
			\
			"SO":[{\
				"Static_hostname":"rodrigo",\
				"Icon_name":"computer-desktop",\
				"Chassis":"desktop",\
				"Machine_ID":"a0792629cb3d4b9f868b99dddb2fe807",\
				"Boot_ID":"ebe192747430474bac7143b7c38058df",\
				"Operating_System":"Debian GNU/Linux 10 (buster)",\
				"Kernel":"Linux 4.19.0-6-amd64",\
				"Architecture":"x86-64"\
			}],\
			\
			"CAMBIOS":[{\
				"id":1,\
				"user":"Christian",\
				"status":"True",\
				"last_update":"2020-01-29"\
			}]\
		}'
		try:
			z = json.loads(data)
			with open('configServer.json','w') as f:
				json.dump(z, f, indent=4)
			if(os.path.exists('configServer.json')):
				return 0
			else:
				return -1
		except:
			return -1


def main():
	try:
		newConfigServer = databaseServer()
		print(newConfigServer.createJsonServer())
	except Exception as error:
		print ("Exception:", error)


if __name__ == "__main__":
	main()