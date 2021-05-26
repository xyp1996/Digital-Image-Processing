from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time

class ImageHandleMove(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 图像平移特效
        width, height, rgba = self.image.shape
        imgNew = np.empty(shape=[width, height, rgba], dtype=int)
        for i in range(height):
            imgTemp = self.image[height - i: height]
            widthTemp, heightTemp, rgbaTemp = imgTemp.shape
            for w in range(widthTemp):
                for h in range(heightTemp):
                    imgNew[w, h] = imgTemp[w, h]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)