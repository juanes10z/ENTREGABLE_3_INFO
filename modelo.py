import pydicom
import matplotlib.pyplot as plt
import os

class BaseDatos(object):

    def __init__(self):
        self.__login = ""
        self.__password = ""
        self.carpeta = ""

    def setlogin(self,l):
        self.__login = l

    def setpassword(self,p):
        self.__password = p

    def validarusuario(self,l,p):
        return(self.__login == l) and (self.__password == p)   
    

    def validar_ruta(self, r):
        self.carpeta = r
        return os.path.isdir(r)
    


    def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.carpeta+"/"+imagen)
        pixel_data = ds.pixel_array
        if (len(pixel_data.shape))==3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            plt.imshow(pixel_data, cmap = plt.cm.bone)
        plt.axis('off')
        plt.savefig("temp_image.png")
        patient_name = ds.PatientName
        study_date = ds.StudyDate
        modality = ds.Modality
        study_instance_uid = ds.StudyInstanceUID
        patient_id = ds.PatientID

        return patient_name, study_date, modality, study_instance_uid, patient_id


    

