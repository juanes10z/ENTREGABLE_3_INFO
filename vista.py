import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QLineEdit, QLabel, QSlider, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

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
        else:
            texto = "Usuario o Contraseña incorrectos"
        
        msj = QMessageBox.information(self,"Alerta",texto,QMessageBox.Ok,QMessageBox.Cancel)
       

    def reject_(self):
        self.campo_usuario.setText("")
        self.campo_password.setText("")
    
    def setControlador(self, c):
        self.__mi_controlador = c


