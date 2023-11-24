from pydicom import dcmread

class BaseDatos(object):

    def __init__(self):
        self.__login = ""
        self.__password = ""

    def setlogin(self,l):
        self.__login = l

    def setpassword(self,p):
        self.__password = p

    def validarusuario(self,l,p):
        return(self.__login == l) and (self.__password == p)       

class TomografiaModelo:
    def __init__(self):
        self.repositorio = []

    def obtener_imagen(self):
            

        for i in range(1,140):
          if i <= 9:
            m = "0"+str(i)
            im = dcmread(r"Circle of Willis\1-0"+str(m)+".dcm")
            self.repositorio.append(im)
        print("Archivo Dicom cargado correctamente")
        return self.repositorio