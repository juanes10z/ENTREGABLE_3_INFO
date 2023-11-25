from PyQt5.QtCore import QObject
import pydicom
import matplotlib.pyplot as plt

class BaseDatos(object):

    def __init__(self):
        self.__login = ""
        self.__password = ""
        self.carpeta = "Circle of Willis"

    def setlogin(self,l):
        self.__login = l

    def setpassword(self,p):
        self.__password = p

    def validarusuario(self,l,p):
        return(self.__login == l) and (self.__password == p)       
    

    def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.carpeta+"/"+imagen)
        pixel_data = ds.pixel_array

        if len(pixel_data.shape) == 3:
            # Tridimensional: Mostrar la sección central
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            # No tridimensional: Mostrar la imagen directamente
            plt.imshow(pixel_data, cmap=plt.cm.bone)

        plt.axis("off")
        plt.savefig("temp_image.png")


class Modelo(QObject):
    def __init__(self):
        super().__init__()
        self.carpeta = "Circle of Willis"

    

