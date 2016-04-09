from escposprinter import *
from escposprinter.escpos import EscposIO

# Epson = printer.Usb(0x04b8,0x0202)
# Epson.text('Hello World')
# Epson.cut()

for indexPrinter in range(0, 1):
    if (indexPrinter == 0):
        with EscposIO(printer.Network('10.0.0.174', port=9100)) as p:
            if (p.printer.isAlive()):
                p.printer.open()
                p.set(font='a', codepage='cp1251', size='normal', align='center', bold=True)
                p.printer.set(align='left')
                p.printer.image('/Users/simonefardella/PycharmProjects/GTSV5/GTS_WebApp/static/img/rsz_logo_white_compressed_Scontrini.jpg') #image

            else:
                raise Exception ("Host is unreachable, socket communication was not opened")



