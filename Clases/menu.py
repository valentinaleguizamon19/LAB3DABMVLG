class Menu:    
    def __init__(self,paciente):
        
        self.paciente = paciente

    def ver(self):
        print("BIENVENIDO AL SISTEMA DE MONITOREO DE TEMPERATURA ".center(20,"*"))
        print("1. Configuración de parámetros")
        print("2. Captura de datos")
        print("3. Reportes")

        op=input(">>>")

        return op

class MenuCaptura():
    def ver(self):
        print("CAPTURA DE DATOS".center(20,"*"))
        print("1. Por cantidad de datos ")
        print("2. Por medio de gráfica en tiempo real")
        print("3. S A L I R")

        op=input(">>>")
        return op
class MenuParametros():
    def ver(self):
        print("CONFIGURACIÓN DE PARÁMETROS")
        
class MenuReportes():
    def ver(self):
        print("MENU REPORTES".center(20,"*"))
        print("1. Gráfica de los datos capturados")
        print("2. Valores máximo y mínimo")
        print("3. Promedio de la temperatura")
        print("4. S A L I R")

        op=input(">>>")
        return op


if __name__=='__main__':
    m = Menu("Paciente")
    m.ver()