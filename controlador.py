from modelo import *
from vista import *
import sys 
from PyQt5.QtWidgets import QApplication

class coordinandor:
    
    def __init__(self,vista,modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    def validarusuario(self,l,p):
        return self.__mi_modelo.validarusuario(l,p)


def main():
    imagenes = TomografiaModelo()
    imagenes.obtener_imagen()
    app = QApplication(sys.argv)
    mi_vista = Ventanalogin()
    mi_modelo = BaseDatos()
    mi_coordinandor = coordinandor(mi_vista,mi_modelo)
    mi_vista.setControlador(mi_coordinandor)
    mi_modelo.setlogin("1")
    mi_modelo.setpassword("2")
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()   