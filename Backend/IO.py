
from zipfile import ZipFile
from PIL import Image
import os, io
from ImageStruct import ImageStruct

class IO:
    def __init__(self):
        pass

    #Takes a list of ImageStructs and outputs a Zipfile object of all the cropped images
    def create_zip(self, images):
        path = "./output_images/Crop.zip"
        with ZipFile(path, 'w') as zfile:
            for img in images:
                path_name = img.get_path()
                i = 1
                for crop in img.get_crops():  
                    image_byte = io.BytesIO()
                    crop.save(image_byte, 'png')
                    byte = image_byte.getvalue()
                    
                    zfile.writestr('./{}/{}.png'.format(path_name, i), byte)
                    i += 1

    #Takes binary data of a zipfile and reads all files within the zipfile. 
    def read_zip(self, path):
        images = []
        img_ext = ['.png', '.jpg', '.jpeg']

        with ZipFile(path) as zfile:
            for img_file_path in zfile.namelist():
                if img_file_path[-1] != '/':
                    for ext in img_ext:
                        if ext in img_file_path: 
                            bytes = ZipFile.read(zfile, name=img_file_path)
                            img = Image.open(io.BytesIO(bytes))
                            images.append(ImageStruct(img, img_file_path))
        return images

