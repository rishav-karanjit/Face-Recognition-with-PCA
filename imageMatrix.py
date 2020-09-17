import cv2
import numpy as np


class imagetoMatrixClass:
    def __init__(self, images_paths, img_width, img_height):

        self.images_paths = images_paths
        self.img_width = img_width
        self.img_height = img_height
        self.img_size = (img_width * img_height)



    def get_matrix(self):

        col = len(self.images_paths)
        img_mat = np.zeros((self.img_size, col))

        i = 0
        for path in self.images_paths:
            grey = cv2.imread(path, 0)
            grey_resized = cv2.resize(grey, (self.img_width,self.img_height))
            mat_grey = np.asmatrix(grey_resized)
            vec=mat_grey.ravel()

            img_mat[:, i] = vec
            i += 1
        return img_mat