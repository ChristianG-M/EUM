#!/usr/bin/python3
'''DL17'''
import base64
import qrcode

class codificar():
    def __init__(self):
        pass

    def codeInfoQR(self, informacion):        
        infoInBytes = bytes( informacion, 'utf-8')
        print(infoInBytes, file=open("InfoInBytes.txt", "a"))
        encoded = base64.b64encode(infoInBytes)
        print(encoded, file=open("InfoCoded.txt", "a"))
        return encoded

    def generarQR(self, infoCoded, expedidoraID, folio ):
        qr = qrcode.make(infoCoded)
        nombre = 'QR_' + str(expedidoraID)+ '_' + str(folio) + '.png' 
        qr.save( nombre )
        print(nombre, file=open("QRFiles.txt", "a"))
        return nombre

    def cleanCharQR( self, ticketQR ):
        limpiaAdmiracion = ticketQR.replace( '¡', '+' )
        limpiaComillas = limpiaAdmiracion.replace( "'", '-' )
        limpiaInterrogacion = limpiaComillas.replace( '¿', '=' )
        ticketQRFinal = limpiaInterrogacion
        print(ticketQRFinal, file=open("infoRead.txt", "a"))
        return ticketQRFinal

    def decodeInfoQR(self, informacion):
        decoded = base64.b64decode(informacion)
        infoInString = str( decoded, 'utf-8')
        print(infoInString, file=open("infoReadCoded.txt", "a"))
        return infoInString

    def validarExist(self, infoIni, infoFin):
        infoInBytesOne = bytes( infoIni, 'utf-8')        
        if infoInBytesOne == infoFin:
            return True
        else:
            return False
'''
def main():    
    codificador = codificar()
    str_info = "M,1050,1,22-01-2020,01:12:48."
    datos = str_info.split(',')
    print(str_info, file=open("InfoOriginal.txt", "a"))
    codificado = codificador.codeInfoQR(str_info)
    codificador.generarQR(codificado, datos[2], datos[1])
    readTicketQR = str(input("Ingrese ticket QR:"))
    ticketQRLimpio = codificador.cleanCharQR( readTicketQR )
    readDatos = codificador.decodeInfoQR(ticketQRLimpio)
    if(codificador.validarExist(str_info, readDatos)):
        print("Informacion correcta")
    else:
        print("->   ¡ERROR!   <-")


if __name__ == "__main__":
    main()'''
'''DL17'''