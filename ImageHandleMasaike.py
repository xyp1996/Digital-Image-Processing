from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time
import random

class ImageHandleMasaike(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 马赛克特效
        limit = 36

        temp1 = list(range(0, 256))
        temp2 = list(range(0, 256))
        temp3 = [[i, j] for i in temp1 for j in temp2]
        random.shuffle(temp3)

        width, height, rgba = self.image.shape
        imgNew = np.empty(shape=[width, height, rgba], dtype=int)

        num = int(len(temp3) / limit)
        for i in range(limit):
            for zuobiao in temp3[i * num:(i + 1) * num]:
                w, h = zuobiao
                imgNew[w, h] = self.image[w, h]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)
