#!/usr/bin/python3
import json

class editInfo():
	def __init__(self):
		pass

	def editar(self):

		with open('config.json', 'r+') as f:
			data = json.load(f)
			data['id'] = 134
			f.seek(0)
			json.dump(data, f, indent=4)
			f.truncate()

def main():
	categoria = ["GENERAL", "CONTROLADORA", "SO", "PATHS", "DISPOSITIVOS", "RED", "TARIFAS", "CAMBIOS"]
	campo = 
	[
		["id", "id_sucursal", "tipo", "modo_operacion", "numero_serie", "version_app", "ubicacio", "politicas", "actualizacion_automatica", "licencia", "stand_alone", "tolerancia" ],
		["version_TC", "version_ard", "version_sotware_ard", "X", "Y" ],
		["Static_hostname", "Icon_name", "Chassis", "Machine_ID", "Boot_ID", "Operating_System", "Kernel", "Architecture" ],
		["media", "app" ],
		["impresora", "escaner", "lector_rfid", "bocinas" ],
		["server_ip_address", "port", "ip_addeess", "gateway" ],
		["tarias"],
		["id", "user", "status", "last_update" ]
	]
	editarArchivo = editInfo()
	print("Menu de opciones")
	for i in range()
	opcion = input("Opcion:")	
	#resultado = editarArchivo.editar()
	#print(resultado)

if __name__ == "__main__":
	main()