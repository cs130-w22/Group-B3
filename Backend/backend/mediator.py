#import model
#import zip
#import preprocess

class Mediator:
    def __init__(self):
        self.preprocessor = None
        self.model = None
        self.pipe = None
        self.images = []

    def preprocess_img(self, img):
        image, ratio_h, ratio_w = self.preprocessor.resize(img, 0, 0)
        self.images.append(image)

    def delete_img(self):
        self.images.clear()

    def predict(self, img):
        prediction = self.model(img)

    def process_img(self):
        self.preprocessor
    
    def process_zip(self):
        self.preprocessor