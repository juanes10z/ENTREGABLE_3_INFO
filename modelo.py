from PyQt5.QtCore import QObject
import pydicom
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from pydicom.pixel_data_handlers.util import apply_voi_lut

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
        ds = pydicom.dcmread(os.path.join(self.carpeta, imagen))

        # Aplicar la presentación (Value of Interest - VOI LUT)
        pixel_data = apply_voi_lut(ds.pixel_array, ds)

        fig, ax = plt.subplots()
        if len(pixel_data.shape) == 3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            ax.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            ax.imshow(pixel_data, cmap=plt.cm.bone)
        
        ax.axis("off")

        # Guardar la figura en un archivo temporal
        temp_path = "temp_image.png"
        canvas = FigureCanvas(fig)
        canvas.print_figure(temp_path, bbox_inches="tight")
        plt.close(fig)

        return temp_path


    

