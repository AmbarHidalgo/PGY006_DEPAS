from colorama import Style
import numpy
import os
import msvcrt
depas=numpy.empty([2,10,4],object)

def dibujarEdificio():
    print("    A   B   C   D")
    for x in range(10): #Filas
        if 10-x<10:
            print(f"0{10-x}",end="|")
        else:
            print(f"{10-x}",end="|")
        
        for y in range(4): #Columnas
            if depas[0,x,y]==None:
                print(f"🟩", end="|") 
            else:
                print(f"🟥", end="|")
        print(" ")

def limpiarpantalla():
    pass

def printr(texto):
    pass

def comprarDepa(piso,columna):
    pass

def pagar(costo,pago):
    pass

def buscarDueno(rut):
    pass



