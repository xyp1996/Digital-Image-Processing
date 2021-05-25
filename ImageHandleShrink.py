from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time

class ImageHandleShrink(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 中间收缩特效
        row, col, rgba = self.image.shape
        imgNew = np.empty(shape=[row, col, rgba], dtype=int)

        center = int(col / 2)

        for cc in range(center):
            for h in range(col):
                imgNew[cc, h] = self.image[cc, h]
                imgNew[row - 1 - cc, h] = self.image[row - 1 - cc, h]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)