#!/usr/bin/python3
import configparser

archivoConf = configparser.ConfigParser()

archivoConf['CAMBIOS'] = {}

fieldCambios = archivoConf['CAMBIOS']
fieldCambios['id'] = "1"
fieldCambios['last_update'] = "2020-01-30"
fieldCambios['status'] = "True"
fieldCambios['user'] = "Christian"


archivoConf['CONTROLADORA'] = {}

fieldControladora = archivoConf['CONTROLADORA']
fieldControladora['X'] = "[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]"
fieldControladora['Y'] = "[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]"
fieldControladora['version_TC'] = "Pulso_V1"
fieldControladora['version_ard'] = "Micro"
fieldControladora['version_sotware_ard'] = "1.3"


archivoConf['DISPOSITIVOS'] = {}

fieldDispositivos = archivoConf['DISPOSITIVOS']
fieldDispositivos['bocinas'] = ""
fieldDispositivos['escaner'] = "Honeywell"
fieldDispositivos['impresora'] = "TUP9000"
fieldDispositivos['lector_rfid'] = ""


archivoConf['GENERAL'] = {}

fieldGeneral = archivoConf['GENERAL']
fieldGeneral['actualizacion_automatica'] = "False"
fieldGeneral['id'] = "4"
fieldGeneral['id_sucursal'] = "3"
fieldGeneral['licencia'] = "23455dfdg4es"
fieldGeneral['modo_operacion'] = "1"
fieldGeneral['numero_serie'] = "a0792629cb3d4b9f868b99dddb2fe807"
fieldGeneral['politicas'] = "              La empresa no se hace responsable por objetos personales,\t\t              fallas mecanicas y/o electricas, siniestros ocasionados por\t\t              derrumbes, temblores, terremotos o fenomenos naturales, asi \t\t              como robo de accesorios o vandalismo en su vehiculo o robo \t\t              con violencia y portador de arma de fuego. \t\t              Por robo total de acuerdo a los terminos  del seguro contratado.\t\t              Boleto Perdido.\t\t              Se entregara el  vehiculo  a quien acredite la  propiedad.\t\t              Costo del boleto perdido es de $100.00 \t\t              Al recibir este boleto acepta las condiciones del seguro contra\t\t              robo total. PARKING TIP S.A. de C.V. / R.F.C PTI120210571\t\t              Escobillera 13 Col. Paseos de Churubusco CDMX C.P 09030"
fieldGeneral['stand_alone'] = "False"
fieldGeneral['tipo'] = "2"
fieldGeneral['tolerancia'] = "10"
fieldGeneral['ubicacio'] = "Vips"
fieldGeneral['version_app'] = "2.1"



archivoConf['PATHS'] = {}
fieldPaths = archivoConf['PATHS']
fieldPaths['app'] = "/usr/share/eum"
fieldPaths['media'] = "/usr/share/eum/media"



archivoConf['RED'] = {}
fieldRed = archivoConf['RED']
fieldRed['gateway'] = "192.168.1.1"
fieldRed['ip_addeess'] = "192.168.1.12"
fieldRed['port'] = "2324"
fieldRed['server_ip_address'] = "12.168.1.129"


archivoConf['SO'] = {}
fieldSO = archivoConf['SO']
fieldSO['Architecture'] = "x86-64"
fieldSO['Boot_ID'] = "ebe192747430474bac7143b7c38058df"
fieldSO['Chassis'] = "desktop"
fieldSO['Icon_name'] = "computer-desktop"
fieldSO['Kernel'] = "Linux 4.19.0-6-amd64"
fieldSO['Machine_ID'] = "a0792629cb3d4b9f868b99dddb2fe807"
fieldSO['Operating_System'] = "Debian GNU/Linux 10 (buster)"
fieldSO['Static_hostname'] = "rodrigo"


archivoConf['TARIFAS'] = {}
fieldTarifas = archivoConf['TARIFAS']
fieldTarifas['tarifas'] = "(1, 1, None, None, None, None, None, 'tarifa de 0 a 1 horas', 5, 0, 1, 1, 1, 1)\
(2, 1, None, None, None, None, None, 'tarifa de 1 a 2 horas', 5, 1, 2, 1, 1, 1)\
(3, 1, None, None, None, None, None, 'tarifa de 2 a 3 horas', 10, 2, 3, 1, 1, 1)\
(4, 1, None, None, None, None, None, 'tarifa de 3 a 4 horas', 20, 3, 4, 1, 1, 1)\
(5, 1, None, None, None, None, None, 'tarifa de 4 a 5 horas', 40, 4, 5, 1, 1, 1)\
(6, 1, None, None, None, None, None, 'tarifa de 5 a 6 horas', 50, 5, 6, 1, 1, 1)\
(7, 1, None, None, None, None, None, 'tarifa de 6 a 7 horas', 60, 6, 7, 1, 1, 1)\
(8, 1, None, None, None, None, None, 'tarifa de 7 a 8 horas', 70, 7, 8, 1, 1, 1)\
(9, 1, None, None, None, None, None, 'tarifa de 8 a 9 horas', 80, 8, 9, 1, 1, 1)\
(10, 1, None, None, None, None, None, 'tarifa de 9 a 10 horas', 90, 9, 10, 1, 1, 1)\
(11, 1, None, None, None, None, None, 'tarifa de 10 a 11 horas', 100, 10, 11, 1, 1, 1)\
(12, 1, None, None, None, None, None, 'tarifa maxima', 110, 11, 12, 1, 1, 1)\
(13, 1, None, None, None, None, None, 'descuento wallmart', 10, 0, 1, 1, 2, 2)\
(14, 1, None, None, None, None, None, 'descuento cinemex', 20, 1, 2, 1, 2, 2)\
(15, 1, None, None, None, None, None, 'descuento cinemex', 30, 1, 500, 1, 2, 2)\
(16, 1, None, None, None, None, None, 'descuento cinemex', 40, 3, 4, 1, 2, 2)\
(17, 1, None, None, None, None, None, 'descuento vips', 50, 4, 5, 1, 2, 2)\
(18, 1, None, None, None, None, None, 'descuento suburbia', 60, 5, 6, 1, 2, 2)\
(26, 1, None, None, None, None, None, 'emp', 70, 6, 7, 1, 2, 2)\
(27, 1, None, None, None, None, None, 'descuento sears', 80, 7, 8, 1, 2, 2)\
(28, 1, None, None, None, None, None, 'tarrifa de 0 a 3 hrs ', 120, 12, 13, 1, 1, 1)\
(29, 1, None, None, None, None, None, 'tolerancia', 0, 13, 40000, 1, 1, 1)\
(30, 1, None, None, None, None, None, 'D', 90, 8, 9, 1, 2, 2)\
(31, 1, None, None, None, None, None, 'sin sello', 100, 9, 10, 1, 2, 2)\
(32, 1, None, None, None, None, None, 'sin sello ', 110, 10, 11, 1, 2, 2)\
(33, 1, None, None, None, None, None, 'sin sello', 120, 11, 40000, 1, 2, 2)\
(67, 1, None, None, None, None, None, '', 77, 77, 78, 1, 1, 4)"




with open('configuracion.ini', 'w') as configfile:
	archivoConf.write(configfile)