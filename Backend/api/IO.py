
from zipfile import ZipFile
from PIL import Image
import os, io
import cv2
import numpy as np
from . import ImageInfo

class IO:
    def __init__(self):
        pass

    def create_zip(self, images):
        zip_buf = io.BytesIO()
        with ZipFile(zip_buf, 'w') as zfile:
            for img in images:
                path_name = img.get_path()
                
                for crop in img.get_crops():
                    i = 1
                    image_byte = io.BytesIO()
                    crop.save(image_byte, 'png')
                    byte = image_byte.getvalue()
                    
                    zfile.writestr('./{}/{}.png'.format(path_name, i), byte)
                    i += 1

        return zip_buf.getvalue()

    def read_zip(self, zbytes):
        cv_images = []
        img_ext = ['.png', '.jpg', '.jpeg']

        with ZipFile(io.BytesIO(zbytes)) as zfile:
            for img_file_path in zfile.namelist():
                if img_file_path[-1] != '/':
                    for ext in img_ext:
                        if ext in img_file_path: 
                            bytes = ZipFile.read(zfile, name=img_file_path)
                            img = Image.open(io.BytesIO(bytes))
                            cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
                            cv_images.append(ImageInfo(cv_img, img_file_path))

        return cv_images

    def create_image(self, cv_img, name):
        recolor = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        pil = Image.fromarray(recolor)
        pil.filename = name
        return pil

