from Processor import Processor
from IO import IO
from Frcnn_Model import Frcnn_Model
from ImageStruct import ImageStruct

class Pipeline:
    def __init__(self):
        self.io = IO()
        self.path = "./input_images/input.zip"
        self.preprocessor = Processor()
        self.model = Frcnn_Model()
        self.image_struct = []


    def process_all(self):
        self.image_struct = self.unzip_images(self.path)
        self.crop()

        self.zip_crops()

    # unzip images from a zip file with path path into a list of ImageStruct
    def unzip_images(self, path):
        return self.io.read_zip(path)

    #def preprocess(self, image_data):
    #    for img in image_data:
    #        self.preprocessor.process_img(img)
    

    #Takes the list of ImageStruct and crops out all photos within the images and sets it as a list in ImageStruct
    def crop(self):
        for image in self.image_struct:
            img = image.get_image()
            print(img)
            crops = self.model.get_bouding_boxes(img)
            print(crops) # crops = [((x,y,x,y), c), ...]
            coordCrop = self.preprocessor.processOverlap(crops) #coordCrop = [(x,y, x,y), ...]
            cropped_img = self.model.get_crops(img, coordCrop)
            image.set_crops(cropped_img)   

    #Creates zip file from list of ImageStructs
    def zip_crops(self):
        return self.io.create_zip(self.image_struct)



    