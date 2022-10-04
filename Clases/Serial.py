import serial
import time
import sys
from tabulate import tabulate
from datetime import datetime
from datetime import timedelta
from turtle import clear
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd


#INICIAR CONEXIÓN CON EL PUERTO SERIAL
try:
    puerto = serial.Serial('COM7',9600)
    puerto.close()
    puerto.open()
    print ("Port is open")
except:
    print("Problem open the port")

# CLASE SERIAL DATOS - Aquí se puede realizar el guardado de los datos al archivo

class serial_datos:
    def __init__(self,temperatura,fecha):
        self.temperatura = temperatura
        self.fecha = fecha

    def verDatos(self):
        header = ["TEMPERATURA","FECHA"]
        datos = [[self.temperatura,self.fecha]]
        print(tabulate(datos,header,tablefmt="grid"))
        return datos
    
    #FUNCIÓN PARA GUARDAR LOS DATOS

    def save(self):
        file = open('C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/CapturaDatos.csv','w')

        for i in range (0, len(self.temperatura)):
            t = str(self.temperatura[i])
            f = str(self.fecha[i])
            file = open('C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/CapturaDatos.csv','a')
            linea = ";".join([t,f])
            file.write(linea+"\n")
            file.close()

#- - - - - - - - - - - - - - - - - - - - - - - - -CAPTURA DE LOS DATOS - - - - - - - - - - - - - - - - - - - - - - - - - -

def CapturaDatos(temperatura, fecha):
    d = int(puerto.readline().decode().strip())
    temperatura.append(d)
 
    f = datetime.now().strftime("%c")
    fecha.append(f)
    time.sleep(1.5)

    # VISUALIZACIÓN DE LEDS EN TIEMPO REAL 
    visualizacionLEDS(d)
    
    return temperatura, fecha

#CAPTURA DE DATOS POR CANTIDAD
def datosPorCantidad():
    temperatura = []
    fecha = []
    cant = int(input ("Ingrese la cantidad de datos que desea ver"))
    for i in range (0, cant):
        temperatura, fecha= CapturaDatos(temperatura, fecha)
        i = i+1

    dato = serial_datos(fecha,temperatura)
    return dato
#CAPTURA DE DATOS POR GRÁFICA

def onclick(event):
    global pausa
    print ("pausa")
    pausa = True
pausa = False
def rtm():

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event',onclick)

    ydata=[]
    fecha = []

    def update_data(frames):
        if not pausa:
            punto = puerto.readline().decode().strip()
            visualizacionLEDS(int(punto))
            print(punto)
            ydata.append(punto)
            f = datetime.now().strftime("%c")
            fecha.append(f)
            ax.clear()
            ax.plot(ydata) 
        return(ydata, fecha)

    ani = animation.FuncAnimation(fig,update_data)
    plt.show()

    dato = serial_datos(fecha,ydata)
    
    return dato




# - - - - - - - - - - - - - - - - - - - - - - - - -CONFIGURACIÓN DE LOS PARAMETROS - - - - - - - - - - - - - - - - - - - - - - - - - -
def configurarParametros():
    file = open('C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/Parametros.csv','w')
    print("Hipotermia")

    min_H = int(input("Valor mínimo para hipotermia: "))
    max_H = int(input("Valor máximo para hipotermia: "))

    hipo = ";".join([str(min_H),str(max_H),"H"])
    file.write(hipo+"\n")

    print("Normal")
    min_N = int(input("Valor mínimo para temperatura normal: "))
    max_N = int(input("Valor máximo para temperatura normal: "))

    normal = ";".join([str(min_N), str(max_N),"N"])
    file.write(normal+"\n")

    print("Fiebre")
    min_F = int(input("Valor mínimo para fiebre: "))
    max_F = int(input("Valor máximo para fiebre: "))

    fiebre = ";".join([str(min_F),str(max_F),"F"])
    file.write(fiebre+"\n")

    file.close()

# - - - - - - - - - - - - - - - - - - - - - - - - -VISUALIZACIÓN EN TIEMPO REAL EN LOS LEDS - - - - - - - - - - - - - - - - - - - - - - - - - -
def visualizacionLEDS(d):
    hipo,nor,fie = leerParametros()
    print("Temp=",d)

    if d >= hipo[0] and d <= hipo[1]:
        temp = "H"

    elif d >= nor[0] and d <= nor[1]:
        temp = "N"

    elif d >= fie[0] and d <= fie[1]:
        temp = "F"
    else:
        temp = "Nan"
        print("El rango no ha sido definido")
            
    print ("Categoria:",temp)
    puerto.write(temp.encode())

# Obtener parametros del archivo
def getParametros():
    p = open('C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/Parametros.csv','r')
    paramet = p.readlines()
    return paramet

def leerParametros():
    hipo = []
    nor = []
    fie =[]
    listaParametros = getParametros()

    for i in range (0,3):
        par = listaParametros[i]
        par = par.split(';')

        if i == 0:
            hipo.append(int(par[0]))
            hipo.append(int(par[1]))

        elif i == 1:
            nor.append(int(par[0]))
            nor.append(int(par[1]))

        elif i == 2:
            fie.append(int(par[0]))
            fie.append(int(par[1]))
        else:
            continue
        
    return hipo,nor,fie
