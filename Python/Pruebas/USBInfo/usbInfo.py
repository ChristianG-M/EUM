#!/usr/bin/python3
import os
cmd = os.popen('lsusb')

usb = cmd.read()
#print (now)
file_list_usb = usb.split('\n')
num_dispositivos = len(file_list_usb)
print("Numero de slots USB detectados:	", num_dispositivos-1)
print('\nLista:')
for x in range(0, num_dispositivos-1):
	print(file_list_usb[x])
print('\n')
for y in range(0, num_dispositivos-1):
	if( "e851:2100" in file_list_usb[y] ):
		print("Impresora detectada, Modelo: e851:2100 ( Diamante )")


for z in range(0, num_dispositivos-1):
	if( "0c2e:0be1" in file_list_usb[z] ):
		print("Impresora detectada, Modelo: 0c2e:0be1 ( Honeywell )")