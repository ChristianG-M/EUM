#!/usr/bin/python3

import qrcode

def generarQR( infoCoded, folio ):
	qr = qrcode.make(infoCoded)
	qr.save('QR_' + str(folio) + '.png')
	return qr