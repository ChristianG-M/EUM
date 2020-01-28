import qrcode

qr = qrcode.make("=+-")
nombre = 'QRFinal.png'
qr.save(nombre)
print (nombre)