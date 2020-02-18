#!/usr/bin/python3
import psycopg2
import json
import os.path

class database():
	def __init__(self):
		pass


	def createJson(self):
		data = '{\
	"GENERAL":[{\
		"id":4,\
		"id_sucursal":3,\
		"tipo":2,\
		"modo_operacion":1,\
		"numero_serie":"a0792629cb3d4b9f868b99dddb2fe807",\
		"version_app":2.1,\
		"ubicacio":"Vips",\
		"politicas":"              La empresa no se hace responsable por objetos personales,\
              fallas mecanicas y/o electricas, siniestros ocasionados por\
              derrumbes, temblores, terremotos o fenomenos naturales, asi \
              como robo de accesorios o vandalismo en su vehiculo o robo \
              con violencia y portador de arma de fuego. \
              Por robo total de acuerdo a los terminos  del seguro contratado.\
              Boleto Perdido.\
              Se entregara el  vehiculo  a quien acredite la  propiedad.\
              Costo del boleto perdido es de $100.00 \
              Al recibir este boleto acepta las condiciones del seguro contra\
              robo total. PARKING TIP S.A. de C.V. / R.F.C PTI120210571\
              Escobillera 13 Col. Paseos de Churubusco CDMX C.P 09030",\
		"actualizacion_automatica":"False",\
		"licencia":"23455dfdg4es",\
		"stand_alone":"False",\
		"tolerancia":10\
	}],\
	\
	"CONTROLADORA":[{\
		"version_TC":"Pulso_V1",\
		"version_ard":"Micro",\
		"version_sotware_ard":1.3,\
		"X":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
		"Y":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]\
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
	"PATHS":[{\
		"media":"/usr/share/eum/media",\
		"app":"/usr/share/eum"\
	}],\
	\
	"DISPOSITIVOS":[{\
		"impresora":"TUP9000",\
		"escaner":"Honeywell",\
		"lector_rfid":"",\
		"bocinas":""\
	}],\
	\
	"RED":[{\
		"server_ip_address":"12.168.1.129",\
		"port":"2324",\
		"ip_addeess":"192.168.1.12",\
		"gateway":"192.168.1.1"\
	}],\
	\
	"TARIFAS":[\
	],\
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
			with open('config.json','w') as f:
				json.dump(z, f, indent=4)
			if(os.path.exists('config.json')):
				return 0
			else:
				return -1
		except:
			return -1


	def connectDB(self, host, port, user, password, db):
		try:
			connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (host, port, user, password, db)
			conn = psycopg2.connect(connstr)
			cur = conn.cursor()
			sqlquery = "SELECT * FROM public.\"TARIFA\" ORDER BY \"idTarifa\" ASC"
			cur.execute(sqlquery)
			columns = [column[0] for column in cur.description]
			results = []
			for row in cur.fetchall():
				results.append(dict(zip(columns, row)))	
			cur.close()
			conn.close()
			return results
		except:
			return -1


	def addTarifas(self, results):
		fields = [
			'idTarifa',
		    'plaza',
		    'fec_ini',
		    'fec_fin',
		    'hor_ini',
		    'hor_fin',
		    'dia_sem',
		    'des_tar',
		    'costo',
		    'int_1',
		    'int_2',
		    'estado',
		    'prioridad',
		    'descuento'
		]

		my_data = []
		try:
			for item in results:
				my_data = [item[field] for field in fields]
				if(os.path.exists('config.json')):
					with open('config.json') as json_file:
						data = json.load(json_file)
				else:
					print("No existe el archivo")

				temp = data['TARIFAS']
				temp.append({
					fields[0]:my_data[0],
					fields[1]:my_data[1],
					fields[2]:my_data[2],
					fields[3]:my_data[3],
					fields[4]:my_data[4],
					fields[5]:my_data[5],
					fields[6]:my_data[6],
					fields[7]:my_data[7],
					fields[8]:my_data[8],
					fields[9]:my_data[9],
					fields[10]:my_data[10],
					fields[11]:my_data[11],
					fields[12]:my_data[12],
					fields[13]:my_data[13]
			  	})

				if(os.path.exists('config.json')):
					with open('config.json','w') as f:
						json.dump(data, f, indent=4)
				else:
					return -1
			return 0
		except:
			return -1


def main():
	try:
		newConfig = database()
		if(not(newConfig.createJson())):
			print("Archivo creado correctamente")
		else:
			print("Error al crear archivo")

		host = "127.0.0.1"
		port = "5432"
		user = "postgres"
		password = "root"
		db   = "CajerOk"

		resultado = newConfig.connectDB(host, port, user, password, db)

		if(not(newConfig.addTarifas(resultado))):
			print("Tarifas agregadas correctamente")
		else:
			print("Error al agregar tarifas")
	except Exception as error:
		print ("Exception:", error)


if __name__ == "__main__":
	main()