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


class VentanaPrincipal(QMainWindow):
    def __init__(self, coordinador):
        super().__init__()
        self.coordinador = coordinador
        self.setWindowTitle("Visualizador de Imágenes")
        
        # Crear widgets
        self.label_imagen = QLabel(self)
        self.slider_imagen = QSlider(Qt.Horizontal, self)

        # Configurar diseño de la ventana
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.label_imagen)
        layout.addWidget(self.slider_imagen)

        # Configurar la ventana principal
        self.setCentralWidget(central_widget)
        self.slider_imagen.valueChanged.connect(self.actualizar_imagen)

        # Configurar datos iniciales
        self.repositorio = self.coordinador.obtener_imagenes()
        self.num_imagenes = len(self.repositorio)
        self.slider_imagen.setMaximum(self.num_imagenes - 1)

        # Mostrar la primera imagen al inicio
        self.actualizar_imagen(0)

    def actualizar_imagen(self, indice):
        if 0 <= indice < self.num_imagenes:
            imagen = self.repositorio[indice]
            pixmap = QPixmap.fromImage(imagen)
            self.label_imagen.setPixmap(pixmap)


    def mostrar_ventana_principal(self):
        self.show()