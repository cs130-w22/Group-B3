#image and crops are in PIL Image object form
class ImageStruct:
    def __init__(self, img, fpath):
        self.path = fpath
        self.image = img
        self.crops = []

    def get_image(self):
        return self.image

    def get_name(self):
        return self.path

    def get_crops(self):
        return self.crops

    def set_crop(self, all_crops):
        self.crops = all_crops
