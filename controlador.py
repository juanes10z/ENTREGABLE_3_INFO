from modelo import *
from vista import *
import sys 
from PyQt5.QtWidgets import QApplication

class coordinador:
    def __init__(self, ventana_login, modelo):
        self.__mi_modelo = modelo
        self.__mi_ventana_principal = VentanaPrincipal()
        self.__mi_ventana_principal.setControlador(self)
        self.__ventana_login = Ventanalogin()

    def validarusuario(self, l, p):
        return self.__mi_modelo.validarusuario(l, p)

    
    def img_conextion(self, imagen):
        return self.__mi_modelo.picture_creator(imagen)

    def mostrar_ventana_principal(self):
        if not self.__mi_ventana_principal:
            self.__mi_ventana_principal = VentanaPrincipal()
        self.__mi_ventana_principal.setControlador(self)
        self.__mi_ventana_principal.show()

    
    def mostrar_login(self):
        if not self.__ventana_login:
            self.__ventana_login = Ventanalogin()
        self.__ventana_login.setControlador(self)
        self.__ventana_login.show()


    def validar_ruta(self, ruta):
        return self.__mi_modelo.validar_ruta(ruta)
    

def main():

    app = QApplication(sys.argv)
    mi_vista_login = Ventanalogin()
    mi_modelo = BaseDatos()
    mi_coordinador = coordinador(mi_vista_login, mi_modelo)
    mi_vista_login.setControlador(mi_coordinador)
    mi_modelo.setlogin("medicoAnalitico")
    mi_modelo.setpassword("bio12345")
    mi_vista_login.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
