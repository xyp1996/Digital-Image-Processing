from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.mainui import Ui_MainWindow
import sys

from ImageFile import ImageFile

from texiao.ImageHandleSplitViewDown import ImageHandleSplitViewDown
from texiao.ImageHandleSplitViewUp import ImageHandleSplitViewUp
from texiao.ImageHandleSplitViewRight import ImageHandleSplitViewRight
from texiao.ImageHandleSplitViewLeft import ImageHandleSplitViewLeft
from texiao.ImageHandleExpand import ImageHandleExpand
from texiao.ImageHandleShrink import ImageHandleShrink
from texiao.ImageHandleJianxian import ImageHandleJianxian
from texiao.ImageHandleVshade import ImageHandleVshade
from texiao.ImageHandleHshade import ImageHandleHshade
from texiao.ImageHandleMasaike import ImageHandleMasaike
from texiao.ImageHandleMove import ImageHandleMove
from texiao.ImageHandleFly import ImageHandleFly

showSpeed = 0.01  # 特效显示中，图像显示速度控制

class MyUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyUI, self).__init__()
        self.imageFile = ImageFile()
        self.bmpImage = self.imageFile.getBMP('lena512.bmp')
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
        # 图像渐显特效
        self.imageHandleJianxian = ImageHandleJianxian(self.bmpImage, showSpeed)
        self.imageHandleJianxian.resultImage.connect(self.flushRightImage)
        # 百叶窗特效
        self.imageHandleHshade = ImageHandleHshade(self.bmpImage, showSpeed)
        self.imageHandleHshade.resultImage.connect(self.flushRightImage)
        self.imageHandleVshade = ImageHandleVshade(self.bmpImage, showSpeed)
        self.imageHandleVshade.resultImage.connect(self.flushRightImage)
        # 马赛克特效
        self.imageHandleMasaike = ImageHandleMasaike(self.bmpImage, showSpeed)
        self.imageHandleMasaike.resultImage.connect(self.flushRightImage)

    def initEvent(self):
        self.action_split_down.triggered.connect(self.splitViewDown)
        self.action_split_up.triggered.connect(self.splitViewUp)
        self.action_split_left.triggered.connect(self.splitViewLeft)
        self.action_split_right.triggered.connect(self.splitViewRight)
        self.action_move.triggered.connect(self.imageMove)
        self.action_fly.triggered.connect(self.imageFly)
        self.action_expand.triggered.connect(self.imageExpand)
        self.action_shrink.triggered.connect(self.imageShrink)
        self.action_Jianxian.triggered.connect(self.imageJianxian)
        self.action_Masaike.triggered.connect(self.imageMasaike)
        self.action_Hshade.triggered.connect(self.imageHshade)
        self.action_Vshade.triggered.connect(self.imageVshade)

    def splitViewDown(self):
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

    def imageJianxian(self):
        if not self.imageHandleJianxian.isFinished():
            self.imageHandleJianxian.start()

    def imageHshade(self):
        if not self.imageHandleHshade.isFinished():
            self.imageHandleHshade.start()

    def imageVshade(self):
        if not self.imageHandleVshade.isFinished():
            self.imageHandleVshade.start()

    def imageMasaike(self):
        if not self.imageHandleMasaike.isFinished():
            self.imageHandleMasaike.start()

    def initLeftImage(self):
        img = self.imageFile.ndarry2image(self.bmpImage)
        self.left_img.setPixmap(img)

    def flushRightImage(self, img):
        img = self.imageFile.ndarry2image(img)
        self.right_img.setPixmap(img)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 显示窗口
    win = MyUI()
    win.show()
    sys.exit(app.exec_())
