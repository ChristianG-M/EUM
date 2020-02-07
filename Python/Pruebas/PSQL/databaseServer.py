#!/usr/bin/python3
import psycopg2
import json

# Postgres
PSQL_HOST = "127.0.0.1"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "root"
PSQL_DB   = "CajerOk"

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
except:
	print("Error al crear archivo inicial")