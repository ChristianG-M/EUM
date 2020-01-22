import base64
for anio in range(10, 11):
	for mes in range(9, 11):
		for dia in range(9, 11):
			for folios in range(1, 2):
				if(mes < 10):
					mes2 = '0' + str(mes)
				else:
					mes2 = str(mes)

				if(dia < 10):
					dia2 = '0' + str(dia)
				else:
					dia2 = str(dia)
				fecha = 'M,' + str(folios) + ',1,' + dia2 + '-' + mes2 + '-20' + str(anio) + ',15:23:29.'
				final = bytes(fecha, 'utf-8')
				print(final, file=open("fechasInicio.txt", "a"))
				print(final)
				encoded = base64.b64encode(final)
				print(encoded, file=open("fechasCodificadas.txt", "a"))
				print(encoded)
				'''token = str(input("Ingrese en token:"))
				print(token)
				limpiaAdmiracion = token.replace( '¡', '+' )
				print(limpiaAdmiracion)
				limpiaComillas = limpiaAdmiracion.replace( "'", '-' )
				print(limpiaComillas)
				limpiaInterrogacion = limpiaComillas.replace( '¿', '=' )
				print(limpiaInterrogacion)
				str_y = base64.b64decode(limpiaInterrogacion)'''
				str_y = base64.b64decode(encoded)
				print(str_y, file=open("fechasDecodificadas.txt", "a"))
				print(str_y)
				if final == str_y:					
					print(str_y, file=open("fechasFin.txt", "a"))
					print('ok')
				else:					
					print("Error!", file=open("Error.txt", "a"))
					print('Error!------------------------------------Error!')