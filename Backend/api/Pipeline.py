from . import IO, Preprocessor, MLmodel, ImageInfo

class Pipeline:
    def __init__(self, zipbytes):
        self.io = IO()
        self.preprocessor = Preprocessor()
        self.model = MLmodel()
        self.image_info_struct = []
        self.image_send = []
        pass

    def process_all(self, zbytes):
        self.image_info_struct = self.unzip_images(zbytes)
        for img_info in self.image_info_struct:
            img_prep = self.preprocess(img_info.get_image())
            cropped = self.crop(img_prep)
            for i in range(len(cropped)):
                pass
        return self.zip_crops()

    def unzip_images(self, zfilename):
        return self.io.read_zip(zfilename)

    def preprocess(self, image_data):
        for img in image_data:
            self.preprocessor.process_img(img)

    def crop(self):
        pass

    def zip_crops(self, foldername):
        self.zip_name = self.io.create_zip(foldername)

    def send_response(self):
        pass

    