from . import IO, Preprocessor, MLmodel, ImageInfo

class Pipeline:
    def __init__(self, zipbytes):
        self.io = IO()
        self.recv = zipbytes
        self.preprocessor = Preprocessor()
        self.model = MLmodel()
        self.image_info_struct = []
        self.send = None
        pass

    def process_all(self):
        self.image_info_struct = self.unzip_images(self.recv)
        '''for img_info in self.image_info_struct:
            img_prep = self.preprocess(img_info.get_image())
            cropped = self.crop(img_prep)
            for i in range(len(cropped)):
                pass'''
        self.crop()
        self.send = self.zip_crops()
        return self.send

    def unzip_images(self):
        return self.io.read_zip(self.recv)

    '''def preprocess(self, image_data):
        for img in image_data:
            self.preprocessor.process_img(img)'''

    def crop(self):
        for image in self.image_info_struct:
            img = image.get_image()

            crops = get_crops(img)
            img.set_crop(crops)


        

    def zip_crops(self):
        return self.io.create_zip(self.image_info_struct)

    def send_response(self):
        pass

    