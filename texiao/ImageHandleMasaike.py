from PyQt5.QtCore import QThread, pyqtSignal, QWaitCondition, QMutex
import numpy as np
import time
import random

mutex = QMutex()
class ImageHandleMasaike(QThread):
    resultImage = pyqtSignal(np.ndarray)

    def __init__(self, image: np.ndarray, showSpeed):
        super().__init__()
        self.image = image
        self.showSpeed = showSpeed

        self._isPause = False
        self.cond = QWaitCondition()
        self.wait()

    def pause(self):
        print("线程休眠")
        self._isPause = True

    def resume(self):
        print("线程启动")
        self._isPause = False
        self.cond.wakeAll()

    def run(self):
        mutex.lock()
        # if self._isPause:
        #     self.cond.wait(self.mutex)
        # 马赛克特效
        limit = 36

        width, height, rgba = self.image.shape
        imgNew = np.empty(shape=[width, height, rgba], dtype=int)


        temp1 = list(range(0, width))
        temp2 = list(range(0, height))
        temp3 = [[i, j] for i in temp1 for j in temp2]
        random.shuffle(temp3)

        total = len(temp3)
        num = int(total / limit)
        for i in range(limit):
            start = i * num
            end = (i + 1) * num
            end = total if i+1 == limit and end < total else end
            for zuobiao in temp3[start:end]:
                w, h = zuobiao
                imgNew[w, h] = self.image[w, h]
            self.resultImage.emit(imgNew)
            time.sleep(self.showSpeed)
        mutex.unlock()
