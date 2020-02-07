#!/usr/bin/python3
import json

class creatInfo():
	def __init__(self):
		pass
	
	def crear(self):				
		data = { 
			"GENERAL":{
				"id":4,
				"id_sucursal":3,
				"tipo":2,
				"modo_operacion":1,
				"numero_serie":"a0792629cb3d4b9f868b99dddb2fe807",
				"version_app":2.1,
				"ubicacio":"Vips",
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
		              Escobillera 13 Col. Paseos de Churubusco CDMX C.P 09030",
				"actualizacion_automatica":False,
				"licencia":"23455dfdg4es",
				"stand_alone":False,
				"tolerancia":10

		  	},

		  	"CONTROLADORA":{
		  		"version_TC":"Pulso_V1",
		  		"version_ard":"Micro",
		  		"version_sotware_ard":1.3,
		  		"X":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				"Y":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		  	},

		  	"SO":{
		  		"Static_hostname":"rodrigo",
				"Icon_name":"computer-desktop",
				"Chassis":"desktop",
				"Machine_ID":"a0792629cb3d4b9f868b99dddb2fe807",
				"Boot_ID":"ebe192747430474bac7143b7c38058df",
				"Operating_System":"Debian GNU/Linux 10 (buster)",
				"Kernel":"Linux 4.19.0-6-amd64",
				"Architecture":"x86-64"
		  	},

		  	"PATHS":{
		  		"media":"/usr/share/eum/media",
				"app":"/usr/share/eum"
		  	},

		  	"DISPOSITIVOS":{
		  		"impresora":"TUP9000",
				"escaner":"Honeywell",
				"lector_rfid":"",
				"bocinas":""
		  	},

		  	"RED":{
		  		"server_ip_address":"12.168.1.129",
				"port":"2324",
				"ip_addeess":"192.168.1.12",
				"gateway":"192.168.1.1"
		  	},

		  	"TARIFAS":{
		  		"tarifas":"1,1,'','','','','','tarifa de 0 a 1 horas',5,0,1,1,1,1\
		2,1,'','','','','','tarifa de 1 a 2 horas',5,1,2,1,1,1\
		3,1,'','','','','','tarifa de 2 a 3 horas',10,2,3,1,1,1\
		4,1,'','','','','','tarifa de 3 a 4 horas',20,3,4,1,1,1\
		5,1,'','','','','','tarifa de 4 a 5 horas',40,4,5,1,1,1\
		6,1,'','','','','','tarifa de 5 a 6 horas',50,5,6,1,1,1\
		7,1,'','','','','','tarifa de 6 a 7 horas',60,6,7,1,1,1\
		8,1,'','','','','','tarifa de 7 a 8 horas',70,7,8,1,1,1\
		9,1,'','','','','','tarifa de 8 a 9 horas',80,8,9,1,1,1\
		10,1,'','','','','','tarifa de 9 a 10 horas',90,9,10,1,1,1\
		11,1,'','','','','','tarifa de 10 a 11 horas',100,10,11,1,1,1\
		12,1,'','','','','','tarifa maxima',110,11,12,1,1,1\
		13,1,'','','','','','descuento 1',10,0,1,1,2,2\
		14,1,'','','','','','descuento 2',20,1,2,1,2,2\
		15,1,'','','','','','descuento 3',30,1,500,1,2,2\
		16,1,'','','','','','descuento 4',40,3,4,1,2,2\
		17,1,'','','','','','descuento 5',50,4,5,1,2,2\
		18,1,'','','','','','descuento 6',60,5,6,1,2,2\
		26,1,'','','','','','emp',70,6,7,1,2,2\
		27,1,'','','','','','descuento sears',80,7,8,1,2,2\
		28,1,'','','','','','tarrifa de 0 a 3 hrs ',120,12,13,1,1,1\
		29,1,'','','','','','tolerancia',0,13,40000,1,1,1\
		30,1,'','','','','','D',90,8,9,1,2,2\
		31,1,'','','','','','sin sello',100,9,10,1,2,2\
		32,1,'','','','','','sin sello ',110,10,11,1,2,2\
		33,1,'','','','','','sin sello',120,11,40000,1,2,2\
		67,1,'','','','','','''',77,77,78,1,1,4\
		,,'','','','','','',,,,,,"
		  	},

		  	"CAMBIOS":{
		  		"id":1,
		  		"user":"Christian",
		  		"status":True,
		  		"last_update":"2020-01-29"
		  	}
		}

		with open('config.json', 'w') as conf:
			json.dump(data, conf, separators=(',', ':'), indent=4, sort_keys=True)
		return data

def main():
	crearArchivo = creatInfo()
	resultado = crearArchivo.crear()
	print(resultado)

if __name__ == "__main__":
	main()