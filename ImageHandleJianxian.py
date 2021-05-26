from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time

class ImageHandleJianxian(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 图像渐显特效
        width, height, rgba = self.image.shape
        imgNew = np.empty(shape=[width, height, rgba], dtype=int)
        for i in range(0, 256, 10):
            for w in range(width):
                for h in range(height):
                    temp = np.array([i, i, i, 255])
                    if all(temp >= self.image[w, h]):
                        imgNew[w, h] = self.image[w, h]
                    else:
                        imgNew[w, h] = temp
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)