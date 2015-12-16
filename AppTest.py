from escposprinter import printer
from escposprinter.escpos import EscposIO

with EscposIO(printer.Network('192.168.1.100', port=9100)) as p:
    p.set(font='a', codepage='cp1251', size='normal', align='center', bold=True)
    p.printer.set(align='center')
    p.writelines('Big line\n', font='b')
    p.writelines(u'BIG TEXT', size='2x')