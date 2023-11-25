from PyQt5.QtWidgets import QDialog, QMessageBox, QMainWindow, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os
from modelo import *


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
        self.buttonBox.accepted.disconnect(self.accept_)


        resultado = self.__mi_controlador.validarusuario(login, password)
        self.buttonBox.accepted.connect(self.accept_)
        if resultado:
            texto = "!Usted ha ingresado correctamente¡"
            msj = QMessageBox.information(self, "Alerta", texto, QMessageBox.Ok, QMessageBox.Cancel)
            self.__mi_controlador.mostrar_ventana_principal()
            self.close()

        else:
            texto = "Usuario o Contraseña incorrectos"
            msj = QMessageBox.information(self, "Alerta", texto, QMessageBox.Ok, QMessageBox.Cancel)


    def obtener_ruta(self):
        return self.ruta
       
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
        self.slider.setDisabled(True)
        self.slider.valueChanged.connect(self.actualizar_imagen)
        self.setup()

    def setup(self):
        self.current_index = self.slider.value() - 1 
        self.Exit_button.clicked.connect(self.salida_)
        self.Campo2.setPlaceholderText("Ingrese la ruta de la carpeta")
        self.Cargar2.clicked.connect(self.cargar)


    def cargar(self,ruta):
        self.slider.setDisabled(True)
        ruta = self.Campo2.text()
        self.Cargar2.clicked.disconnect(self.cargar)
        resultado = self.__mi_controlador.validar_ruta(ruta)
        self.Cargar2.clicked.connect(self.cargar)

        if resultado: 
            self.ruta = ruta
            texto = "¡La carpeta se ha cargado correctamente!"
            msj = QMessageBox.information(self, "Alerta", texto, QMessageBox.Ok, QMessageBox.Cancel)
            self.slider.setDisabled(False)  
            self.lista_archivos = os.listdir(self.ruta)
                    
        else:    
            texto = "La ruta del archivo no existe,\npor favor verifique si la ha copiado correctamente.\¡Recuerde que debe ser una carpeta, y NO un unico archivo!"
            msj = QMessageBox.information(self, "Alerta", texto, QMessageBox.Ok, QMessageBox.Cancel)

        self.Exit_button.clicked.connect(self.salida_)

    def actualizar_imagen(self, indice):
        self.current_index = indice - 1 
        if 0 <= self.current_index < len(self.lista_archivos):
            imagen = self.lista_archivos[self.current_index]
            self.__mi_controlador.img_conextion(imagen)
            patient_name, study_date, modality, study_instance_uid, patient_id = self.__mi_controlador.img_conextion(imagen)
            self.patient_name_label.setText("Nombre del paciente:\n"+str(patient_name))
            self.study_date_label.setText("Fecha del estudio:\n"+str(study_date))
            self.modality.setText("Modalidad de escaneo:\n"+str(modality))
            self.study_i.setText("Instancias del estudio:\n"+str(study_instance_uid))
            self.id_p.setText("ID de paciente:\n"+str(patient_id))
            pixmap = QPixmap("temp_image.png")
            self.img.setPixmap(pixmap)
            os.remove("temp_image.png")


    def setControlador(self, c):
        self.__mi_controlador = c

    def salida_(self):
        self.__mi_controlador.mostrar_login()
        self.close()
