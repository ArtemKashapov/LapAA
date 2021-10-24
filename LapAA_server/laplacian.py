import numpy as np
from PIL import Image
import io

class Laplacian:
    def __init__(self, image_data):
        self.original = Image.open(io.BytesIO(image_data))
        self.gray_im = self.im2gray(self.original)
        self.im_array = self.get_array(self.gray_im)
        # print(self.im_array.shape)

    def im_show(self, imag):
        try:
            imag.show()
        except:
            pass

    def im2gray(self, imag):
        return imag.convert('L')

    def get_array(self, imag):
        return np.array(imag)

    def run(self, kernel_size=3):
        m, n = self.im_array.shape
        proccesed = np.zeros_like(self.im_array)

        # print(self.im_array)
        self.im_array = np.c_[ np.zeros((m, 1)), self.im_array ]
        self.im_array = np.c_[ self.im_array, np.zeros((m, 1)) ]
        self.im_array = np.r_[ np.zeros((1, n + 2)), self.im_array ]
        self.im_array = np.r_[ self.im_array, np.zeros((1, n + 2)) ]
        # print(self.im_array)

        # пробегаемся фильтром 3x3
        kernel = np.array([
            [0, 1, 0],
            [1 ,-4, 1],
            [0, 1, 0]            
        ])

        kernel_mod = np.array([
            [1, 1, 1],
            [1 ,-8, 1],
            [1, 1, 1]            
        ])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                proccesed[i-1][j-1] = np.abs((self.im_array[i-1:i+2, j-1:j+2] @ kernel).sum())

        return proccesed
     



     

import time
if __name__ == '__main__':
    with open('source\input_image-1.jpg', "rb") as image:
        f = image.read()
        b = bytearray(f)
    
    t0 = time.time()
    l = Laplacian(b)
    edges = l.run()
    print('execution time:' + str(time.time() - t0))
    
    l.im_show(Image.fromarray(np.uint8(edges) , 'L'))
    l.im_show(l.original)