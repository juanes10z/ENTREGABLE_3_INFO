def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.carpeta+"/"+imagen)
        pixel_data = ds.pixel_array
        if (len(pixel_data.shape)) == 3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)

        else: 
            plt.imshow(imagen, cmap= plt.cm.bone)
        plt.axis("off")
        plt.savefig("temp_image.png")



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


    , cmap=plt.cm.bone

, cmap= plt.cm.bone





    def picture_creator(self, imagen):
        ds = pydicom.dcmread(os.path.join(self.carpeta, imagen))

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