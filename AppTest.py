import datetime

from escposprinter import *
from escposprinter.escpos import EscposIO, Escpos

printerAddress = '192.168.0.197'
printerPort = 9100

def checkPrinterAlive():
    return True

if (checkPrinterAlive()):
    string = str("String: " + str(datetime.datetime.now().microsecond))
    for iteration in range(10):
        with EscposIO(printer.Network(printerAddress, printerPort)) as p:
            p.set(font='a', codepage='cp1251', size='normal', align='center', bold=True)
            p.writelines('LOGO')
            p.printer.nvRamImage()
            #p.printer.image('IMAGE PATH')
            p.writelines('')
            p.writelines('')
            p.writelines('')
            p.writelines('')






