from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import time

class ImageHandleFly(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed
        self.wait()

    def run(self):
        # 交叉飞入特效
        row, col, rgba = self.image.shape
        imgNew = np.empty(shape=[row, col, rgba], dtype=int)

        center = int(col / 2)
        top = self.image[:center]
        buttom = self.image[center:]

        rowTop, colTop, rgbaTop = top.shape
        rowButtom, colButtom, rgbaButtom = buttom.shape
        for left, right in zip(range(row), range(row)[::-1]):
            for i in range(left):
                imgTemp = top[: rowTop, colTop - left:colTop]
                rowTemp, colTemp, rgbaTemp = imgTemp.shape
                for h in range(colTemp):
                    for w in range(rowTemp):
                        imgNew[w, h] = imgTemp[w, h]
            for i in range(right):
                imgTemp = buttom[: rowButtom, : colButtom - i]
                rowTemp, colTemp, rgbaTemp = imgTemp.shape
                for h in range(colTemp):
                    for w in range(rowTemp):
                        imgNew[w + center, i] = imgTemp[w, i]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)