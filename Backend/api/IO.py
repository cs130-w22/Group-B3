
from zipfile import ZipFile

class IO:
    def __init__(self):
        self.images = []
        self.send_img = []
        pass

    def create_zip(self):
        pass

    def read_zip(self, filename):
        img_ext = ['.png', 'jpg', '.jpeg']
        with ZipFile(filename) as zfile:
            for img in zfile.namelist():
                for ext in img_ext:
                    if ext in filename:
                        with zfile.open(img) as file:
                            self.images.append(file)

    def get_images(self):
        return self.images

    def delete_images(self):
        self.images.clear()

    def add_img(self, img):
        self.send_img.append(img)
