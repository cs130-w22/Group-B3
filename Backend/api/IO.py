
from zipfile import ZipFile
from PIL import Image
import os, io
import cv2
import numpy as np
from . import ImageInfo

class IO:
    def __init__(self):
        pass

    def create_zip(self, foldername):
        with ZipFile('{}.zip'.format(foldername), 'w') as zfile:
            for dirname, dirpath, filenames in os.walk(foldername):
                zfile.write(dirname)
                for filename in filenames:
                    zfile.write('{}/{}'.format(dirname, filename))
        self.delete_images(foldername)

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

    def delete_images(self, foldername):
        for file in os.listdir('./temp/{}'.format(foldername)):
            os.remove('./temp/{}'.format(file))
        os.remove('./temp/{}'.format(foldername))

