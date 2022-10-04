import pandas as pd
import matplotlib.pyplot as plt
import csv

def grafico_estatico():
    
    df = pd.read_csv("C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/CapturaDatos.csv", sep= ';')
    df.columns = ['Fecha','temp']

    x_horas = df['Fecha']
    y_temp  = df['temp']
    plt.plot(x_horas,y_temp, color = 'red')
    plt.title('Temperatura')
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.show()

def valor_maximo():
    df = pd.read_csv("C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/CapturaDatos.csv", sep= ';')
    df.columns = ['Fecha','temp']

    max_temp = df['temp'].max() 
    maxValueIndex = df['temp'].idxmax()
    fech_max = str(df['Fecha'][maxValueIndex])

    print("Maximo valor de temperatura es : ",max_temp,"y ocurrio en",fech_max)  

def valor_minimo():
    df = pd.read_csv("C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/CapturaDatos.csv", sep= ';')
    df.columns = ['Fecha','temp']
    
    min_temp = df['temp'].min() 
    minValueIndex = df['temp'].idxmin()
    fech_min = str(df['Fecha'][minValueIndex])

    print("Mínimo valor de temperatura es : ",min_temp,"y ocurrio en",fech_min)  

def valor_promedio():
    df = pd.read_csv("C:/Users/valen/Downloads/DABM - VALENTINA LEGUIZAMON/T2/Database/CapturaDatos.csv", sep= ';')
    df.columns = ['Fecha','temp']
    
    mean_temp = df['temp'].mean()
    print("Promedio de temperatura es : ",mean_temp)  
