from escposprinter import *
from escposprinter.escpos import EscposIO

# Epson = printer.Usb(0x04b8,0x0202)
# Epson.text('Hello World')
# Epson.cut()


with EscposIO(printer.Network('192.168.1.177', port=9100)) as p:
    p.set(font='a', codepage='cp1251', size='normal', align='center', bold=True)
    p.printer.set(align='center')
    #p.printer.image('/Users/simonefardella/Downloads/007.jpeg')
    for i in range(0, 5):
        p.printer.set(align='right')
        p.writelines('Big line, font b\n', font='b')
        p.printer.set(align='left')
        p.writelines('Left Line, font a', font='a')
    #p.writelines(u'Привет', color=2)
        p.printer.set(align='center')
        p.writelines(u'BIG TEXT, riga di stampa: {0}...'.format(str(i)), size='2x')
