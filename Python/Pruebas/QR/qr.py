import qrcode

qr = qrcode.make("TSwxMDUwLDEsMjItMDEtMjAyMCwwMToyMjo1My4=")
nombre = 'QR.png'
qr.save(nombre)
print (nombre)