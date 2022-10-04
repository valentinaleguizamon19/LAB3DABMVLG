'''Archivo principal - Laboratorio 3
Desarrollado por Valentina Leguizamón
'''
from Clases.menu import *
from Clases.Serial import *
from Clases.reportes import *

#INICIAR CONEXIÓN CON EL PUERTO SERIAL
try:
    puerto = serial.Serial('COM7',9600)
    puerto.close()
    puerto.open()
    print ("Port is open")
except:
    print("Problem open the port")
    
def main():
    menu = Menu("Paciente")
    op=menu.ver()

    if op == "1":
        configurarParametros()

    elif op == "2":
        #Captura de datos
        menu2 = MenuCaptura()
        op2 = menu2.ver()

        if op2 == "1":
            #Datos por cantidad
            dato = datosPorCantidad()
            dato.save()

        elif op2 == "2":
            #Por medio de gráfica en tiempo real
            dato = rtm()
            dato.save()

    elif op == "3":
        # Reportes
        menu3= MenuReportes()
        op2 = menu3.ver()
    
        if op2 == "1":
            #Gráfico de los datos capturados
            grafico_estatico()

        elif op2 == "2":
            #Valor máximo y mínimo
            valor_maximo()
            valor_minimo()

        elif op2 == "3":
            #Promedio de la temperatura
            valor_promedio()
    main()

if __name__=='__main__':
    main()
