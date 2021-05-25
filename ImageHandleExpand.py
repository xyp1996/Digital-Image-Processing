from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time

class ImageHandleExpand(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 中间扩展特效
        row, col, rgba = self.image.shape
        imgNew = np.empty(shape=[row, col, rgba], dtype=int)

        center = int(col / 2)

        for cc in range(center):
            for h in range(col):
                imgNew[center - cc, h] = self.image[center - cc, h]
                imgNew[center + cc, h] = self.image[center + cc, h]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)