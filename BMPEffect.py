from PyQt5.QtWidgets import QApplication, QMainWindow
from mainui import Ui_MainWindow
import sys

from ImageFile import ImageFile

from ImageHandleSplitViewDown import ImageHandleSplitViewDown
from ImageHandleSplitViewUp import ImageHandleSplitViewUp
from ImageHandleSplitViewRight import ImageHandleSplitViewRight
from ImageHandleSplitViewLeft import ImageHandleSplitViewLeft
from ImageHandleExpand import ImageHandleExpand
from ImageHandleShrink import ImageHandleShrink

from ImageHandleMove import ImageHandleMove
from ImageHandleFly import ImageHandleFly

showSpeed = 0.001  # 特效显示中，图像显示速度控制

class MyUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyUI, self).__init__()
        self.imageFile = ImageFile()
        self.bmpImage = self.imageFile.getBMP('/home/jett/Desktop/test/lena512.bmp')
        self.createThread()

        self.setupUi(self)
        self.initEvent()
        self.initLeftImage()

    def createThread(self):
        # 图像扫描特效
        self.imageHandleSplitViewDown = ImageHandleSplitViewDown(self.bmpImage, showSpeed)
        self.imageHandleSplitViewDown.resultImage.connect(self.flushRightImage)
        self.imageHandleSplitViewUp = ImageHandleSplitViewUp(self.bmpImage, showSpeed)
        self.imageHandleSplitViewUp.resultImage.connect(self.flushRightImage)
        self.imageHandleSplitViewRight = ImageHandleSplitViewRight(self.bmpImage, showSpeed)
        self.imageHandleSplitViewRight.resultImage.connect(self.flushRightImage)
        self.imageHandleSplitViewLeft = ImageHandleSplitViewLeft(self.bmpImage, showSpeed)
        self.imageHandleSplitViewLeft.resultImage.connect(self.flushRightImage)
        # 图像平移特效
        self.imageHandleMove = ImageHandleMove(self.bmpImage, showSpeed)
        self.imageHandleMove.resultImage.connect(self.flushRightImage)
        # 交叉飞入特效
        self.imageHandleFly = ImageHandleFly(self.bmpImage, showSpeed)
        self.imageHandleFly.resultImage.connect(self.flushRightImage)
        # 中间扩展特效
        self.imageHandleExpand = ImageHandleExpand(self.bmpImage, showSpeed)
        self.imageHandleExpand.resultImage.connect(self.flushRightImage)
        # 中间收缩特效
        self.imageHandleShrink = ImageHandleShrink(self.bmpImage, showSpeed)
        self.imageHandleShrink.resultImage.connect(self.flushRightImage)

    def initEvent(self):
        self.action_split_down.triggered.connect(self.splitViewDown)
        self.action_split_up.triggered.connect(self.splitViewUp)
        self.action_split_left.triggered.connect(self.splitViewLeft)
        self.action_split_right.triggered.connect(self.splitViewRight)
        self.action_move.triggered.connect(self.imageMove)
        self.action_fly.triggered.connect(self.imageFly)
        self.action_expand.triggered.connect(self.imageExpand)
        self.action_shrink.triggered.connect(self.imageShrink)

    def splitViewDown(self):
        print(self.imageHandleShrink.isFinished())
        if not self.imageHandleSplitViewDown.isFinished():
            self.imageHandleSplitViewDown.start()

    def splitViewUp(self):
        if not self.imageHandleSplitViewUp.isFinished():
            self.imageHandleSplitViewUp.start()

    def splitViewLeft(self):
        if not self.imageHandleSplitViewLeft.isFinished():
            self.imageHandleSplitViewLeft.start()

    def splitViewRight(self):
        if not self.imageHandleSplitViewRight.isFinished():
            self.imageHandleSplitViewRight.start()

    def imageMove(self):
        if not self.imageHandleMove.isFinished():
            self.imageHandleMove.start()

    def imageFly(self):
        if not self.imageHandleFly.isFinished():
            self.imageHandleFly.start()

    def imageExpand(self):
        if not self.imageHandleExpand.isFinished():
            self.imageHandleExpand.start()

    def imageShrink(self):
        if not self.imageHandleShrink.isFinished():
            self.imageHandleShrink.start()

    def initLeftImage(self):
        img = self.imageFile.ndarry2iamge(self.bmpImage)
        # 使用label进行显示
        self.left_img.setPixmap(img)

    def flushRightImage(self, img):
        img = self.imageFile.ndarry2iamge(img)
        self.right_img.setPixmap(img)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 显示窗口
    win = MyUI()
    win.show()
    sys.exit(app.exec_())
