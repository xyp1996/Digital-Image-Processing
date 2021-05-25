# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_img.sizePolicy().hasHeightForWidth())
        self.left_img.setSizePolicy(sizePolicy)
        self.left_img.setMaximumSize(QtCore.QSize(512, 512))
        self.left_img.setText("")
        self.left_img.setAlignment(QtCore.Qt.AlignCenter)
        self.left_img.setObjectName("left_img")
        self.horizontalLayout.addWidget(self.left_img)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.right_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_img.sizePolicy().hasHeightForWidth())
        self.right_img.setSizePolicy(sizePolicy)
        self.right_img.setMaximumSize(QtCore.QSize(512, 512))
        self.right_img.setText("")
        self.right_img.setAlignment(QtCore.Qt.AlignCenter)
        self.right_img.setObjectName("right_img")
        self.horizontalLayout.addWidget(self.right_img)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 28))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.effects = QtWidgets.QMenu(self.menubar)
        self.effects.setObjectName("effects")
        self.menu_4 = QtWidgets.QMenu(self.effects)
        self.menu_4.setObjectName("menu_4")
        self.menu_3 = QtWidgets.QMenu(self.effects)
        self.menu_3.setObjectName("menu_3")
        self.menu = QtWidgets.QMenu(self.effects)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open_file = QtWidgets.QAction(MainWindow)
        self.action_open_file.setObjectName("action_open_file")
        self.action_move = QtWidgets.QAction(MainWindow)
        self.action_move.setObjectName("action_move")
        self.action_fly = QtWidgets.QAction(MainWindow)
        self.action_fly.setObjectName("action_fly")
        self.action_expand = QtWidgets.QAction(MainWindow)
        self.action_expand.setObjectName("action_expand")
        self.action_shrink = QtWidgets.QAction(MainWindow)
        self.action_shrink.setObjectName("action_shrink")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.actionshuiping = QtWidgets.QAction(MainWindow)
        self.actionshuiping.setObjectName("actionshuiping")
        self.actionchuizhi = QtWidgets.QAction(MainWindow)
        self.actionchuizhi.setObjectName("actionchuizhi")
        self.actionshuiping_2 = QtWidgets.QAction(MainWindow)
        self.actionshuiping_2.setObjectName("actionshuiping_2")
        self.actionchuizhi_2 = QtWidgets.QAction(MainWindow)
        self.actionchuizhi_2.setObjectName("actionchuizhi_2")
        self.action_split_down = QtWidgets.QAction(MainWindow)
        self.action_split_down.setObjectName("action_split_down")
        self.action_split_up = QtWidgets.QAction(MainWindow)
        self.action_split_up.setObjectName("action_split_up")
        self.action_split_right = QtWidgets.QAction(MainWindow)
        self.action_split_right.setObjectName("action_split_right")
        self.action_split_left = QtWidgets.QAction(MainWindow)
        self.action_split_left.setObjectName("action_split_left")
        self.file.addAction(self.action_open_file)
        self.menu_4.addAction(self.actionshuiping_2)
        self.menu_4.addAction(self.actionchuizhi_2)
        self.menu_3.addAction(self.actionshuiping)
        self.menu_3.addAction(self.actionchuizhi)
        self.menu.addAction(self.action_split_down)
        self.menu.addAction(self.action_split_up)
        self.menu.addAction(self.action_split_right)
        self.menu.addAction(self.action_split_left)
        self.effects.addAction(self.menu.menuAction())
        self.effects.addAction(self.action_move)
        self.effects.addAction(self.action_fly)
        self.effects.addAction(self.action_expand)
        self.effects.addAction(self.action_shrink)
        self.effects.addAction(self.menu_3.menuAction())
        self.effects.addAction(self.action_8)
        self.effects.addAction(self.menu_4.menuAction())
        self.effects.addAction(self.action_10)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.effects.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.effects.setTitle(_translate("MainWindow", "图像特效"))
        self.menu_4.setTitle(_translate("MainWindow", "百叶窗"))
        self.menu_3.setTitle(_translate("MainWindow", "栅条特效"))
        self.menu.setTitle(_translate("MainWindow", "图像扫描"))
        self.action_open_file.setText(_translate("MainWindow", "打开BMP文件"))
        self.action_move.setText(_translate("MainWindow", "图像移动"))
        self.action_fly.setText(_translate("MainWindow", "交叉飞入"))
        self.action_expand.setText(_translate("MainWindow", "中间扩张"))
        self.action_shrink.setText(_translate("MainWindow", "中间收缩"))
        self.action_8.setText(_translate("MainWindow", "图像渐显"))
        self.action_10.setText(_translate("MainWindow", "马赛克"))
        self.actionshuiping.setText(_translate("MainWindow", "水平栅条"))
        self.actionchuizhi.setText(_translate("MainWindow", "垂直栅条"))
        self.actionshuiping_2.setText(_translate("MainWindow", "水平百叶窗"))
        self.actionchuizhi_2.setText(_translate("MainWindow", "垂直百叶窗"))
        self.action_split_down.setText(_translate("MainWindow", "向下扫描"))
        self.action_split_up.setText(_translate("MainWindow", "向上扫描"))
        self.action_split_right.setText(_translate("MainWindow", "向右扫描"))
        self.action_split_left.setText(_translate("MainWindow", "向左扫描"))