# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ColorTransportWindowPXublu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ColorTransportWindow(object):
    def setupUi(self, ColorTransportWindow):
        if not ColorTransportWindow.objectName():
            ColorTransportWindow.setObjectName(u"ColorTransportWindow")
        ColorTransportWindow.resize(312, 92)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorTransportWindow.sizePolicy().hasHeightForWidth())
        ColorTransportWindow.setSizePolicy(sizePolicy)
        ColorTransportWindow.setMinimumSize(QSize(0, 30))
        self.centralwidget = QWidget(ColorTransportWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.list_color_layout = QVBoxLayout()
        self.list_color_layout.setObjectName(u"list_color_layout")

        self.verticalLayout.addLayout(self.list_color_layout)

        ColorTransportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ColorTransportWindow)

        QMetaObject.connectSlotsByName(ColorTransportWindow)
    # setupUi

    def retranslateUi(self, ColorTransportWindow):
        ColorTransportWindow.setWindowTitle(QCoreApplication.translate("ColorTransportWindow", u"MainWindow", None))
    # retranslateUi

