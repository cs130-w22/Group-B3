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

    def regionOfConvergence(self, box1, box2):
        x1 = max(box1[0], box2[0])
        x2 = min(box1[2], box2[2])
        y1 = max(box1[1], box2[1])
        y2 = min(box1[3], box2[3])

        if x1 >= x2 or y1 >= y2:
            return [0,0]

        conv_area = (x2-x1)*(y2-y1)
        box1_area = (box1[2]-box1[0])*(box1[3]-box1[1])
        box2_area = (box2[2]-box2[0])*(box2[3]-box2[1])

        return [conv_area/box1_area, conv_area/box2_area]


    def processOverlap(self, img_boxes):
        i = 0
        while i < len(img_boxes):
            j = i+1
            while j < len(img_boxes):
                roc = self.regionOfConvergence(img_boxes[i][0], img_boxes[j][0])

                if roc[0] >= 0.9 or roc[1] >= 0.9:
                    if img_boxes[i][1] >= img_boxes[j][1]: #if confidence of box i > box j
                        img_boxes.remove(img_boxes[j])   
                    else:
                        img_boxes.remove(img_boxes[i])
                        j = i+1 
                else:
                    j += 1
            i += 1            

        return img_boxes

    def zip_crops(self):
        return self.io.create_zip(self.image_info_struct)

    def send_response(self):
        pass

    