from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time

class ImageHandleSplitViewLeft(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 图像扫描特效
        width, height, rgba = self.image.shape
        imgNew = np.empty(shape=[width, height, rgba], dtype=int)
        for h in range(height)[::-1]:
            for w in range(width):
                imgNew[w, h] = self.image[w, h]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)