import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

class Ventanalogin(QDialog):
    def __init__(self):
        super(Ventanalogin,self).__init__()
        loadUi("Ventana_Ingreso.ui", self)





app = QApplication(sys.argv)
widget = Ventanalogin()
widget.show()
sys.exit(app.exec_())