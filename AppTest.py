from escposprinter import *
from escposprinter.escpos import EscposIO

Epson = printer.Usb(0x04b8,0x0202)
Epson.text('Hello World')
Epson.cut()


with EscposIO(printer.Network('192.168.1.87', port=9100)) as p:
    p.set(font='a', codepage='cp1251', size='normal', align='center', bold=True)
    p.printer.set(align='center')
    p.printer.image('logo.gif')
    p.writelines('Big line\n', font='b')
    p.writelines(u'Привет', color=2)
    p.writelines(u'BIG TEXT', size='2x')
