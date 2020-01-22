#!/usr/bin/python3

import base64

def codeInfoQR( informacion, folio ):
	infoInBytes = bytes( informacion, 'utf-8')
	print(infoInBytes, file=open("InfoInBytes.txt", "a"))
	print(infoInBytes)

	encoded = base64.b64encode(infoInBytes)
	print(encoded, file=open("InfoCoded.txt", "a"))
	print(encoded)
	return encoded