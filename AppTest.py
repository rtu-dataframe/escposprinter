import datetime

from escposprinter import *
from escposprinter.escpos import EscposIO, Escpos

printerAddress = '192.168.17.187'
printerPort = 9100

string = str("String: " + str(datetime.datetime.now().microsecond))
for iteration in range(1):
    with EscposIO(printer.Network(printerAddress, printerPort)) as p:
        p.set(font='a', codepage='cp1251', size='normal', align='center', bold=True)
        p.writelines('LOGO')
        p.printer.nvRamImage()
        #p.printer.image('IMAGE PATH')
        p.writelines('')
        p.writelines('')
        p.writelines('')
        p.writelines('')


#OTHERWISE

p = EscposIO(printer.Network(printerAddress, port=printerPort))
p.autoCutMode = 'PAPER_PART_CUT'
p.autoclose = False
p.writelines('LOGO')
p.printer.nvRamImage()
p.writelines('')
p.printer.cut()





