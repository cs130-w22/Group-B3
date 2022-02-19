
class ImageInfo:
    def __init__(self, img, fpath):
        self.path = fpath
        self.image = img

    def get_image(self):
        return self.image

    def get_name(self):
        return self.path