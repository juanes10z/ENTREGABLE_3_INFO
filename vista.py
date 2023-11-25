import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QLineEdit, QLabel, QSlider, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import os
from controlador import *

class Ventanalogin(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Ventana_ingreso.ui", self)
        self.setup()

    def setup(self):
        self.buttonBox.accepted.connect(self.accept_)
        self.buttonBox.rejected.connect(self.reject_)
        self.campo_password.setEchoMode(QLineEdit.Password)
    
    def accept_(self):
        login = self.campo_usuario.text()
        password = self.campo_password.text()
        resultado = self.__mi_controlador.validarusuario(login,password)
        if resultado:
            texto = "!Usted ha ingresado correctamente¡"
            msj = QMessageBox.information(self, "Alerta", texto, QMessageBox.Ok, QMessageBox.Cancel)
            self.__mi_controlador.mostrar_ventana_principal()
            self.close()

        else:
            texto = "Usuario o Contraseña incorrectos"
            msj = QMessageBox.information(self, "Alerta", texto, QMessageBox.Ok, QMessageBox.Cancel)
       

    def reject_(self):
        self.campo_usuario.setText("")
        self.campo_password.setText("")
    
    def setControlador(self, c):
        self.__mi_controlador = c
        self.setup()

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("MainWindow.ui", self)
        self.setup()

    def setup(self):
        self.carpeta = "Circle of Willis"
        self.lista_archivos = os.listdir(self.carpeta)
        self.slider.valueChanged.connect(self.cargar)
        self.current_index = self.slider.value() - 1 




    def cargar(self):
        indice = self.slider.value()
        if 0 <= indice < len(self.lista_archivos):
            imagen = self.lista_archivos[indice]
            self.__mi_controlador.img_conextion(imagen)
            pixmap = QPixmap("temp_image.png")
            
            self.img.setPixmap(pixmap)
            os.remove("temp_image.png")

    def setControlador(self, c):
        self.__mi_controlador = c


