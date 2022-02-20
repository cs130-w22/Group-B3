import cv2

class Preprocessor:
    def __init__():
        pass

    def preprocess_img(self, img):
        img = self.grayscale(img)
        img = self.threshold(img, 100)
        img = self.blur(img)
        return self.resize(img, 900, 900)
        pass

    def blur(self, img):
        return cv2.GaussianBlur(img, (3,3), 0)

    def grayscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def threshold(self, img, thresh):
        return cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    def resize(self, img, height, width):
        old_w, old_h, channels = img.shape
        w_ratio, h_ratio = old_w/width, old_h/height
        new_dim = (width, height)
        return cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA), w_ratio, h_ratio

