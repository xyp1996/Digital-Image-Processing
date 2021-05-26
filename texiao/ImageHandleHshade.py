from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time

class ImageHandleHshade(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 百叶窗特效
        limit = 8
        row, col, rgba = self.image.shape
        imgNew = np.empty(shape=[row, col, rgba], dtype=int)
        num = int(col / limit)
        ilist = range(num)
        jlist = range(limit)
        for i in ilist:
            for j in jlist:
                num2 = num * j
                for h in range(col):
                    imgNew[i + num2, h] = self.image[i + num2, h]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)