import datetime
from escposprinter import *
from escposprinter.escpos import EscposIO, Escpos


printerAddress = '192.168.1.72'
printerPort = 9100

def checkPrinterAlive():
    if (printer.Network.isAlive(printerAddress, printerPort)):
        return True
    else:
        raise Exception ("Host is unreachable, socket communication was not opened")

if (checkPrinterAlive()):
    string = str("String: " + str(datetime.datetime.now().microsecond))
    with EscposIO(printer.Network(printerAddress, printerPort)) as p:
        p.set(font='a', codepage='cp1251', size='normal', align='center', bold=True)
        p.writelines('')
        p.writelines('')
        p.writelines('')
        p.writelines("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam facilisis congue sodales. Nullam pharetra diam vel tempus facilisis.")
        p.writelines('')
        p.writelines('')
        p.writelines('')




