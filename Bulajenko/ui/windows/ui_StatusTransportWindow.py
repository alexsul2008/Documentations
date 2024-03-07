# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StatusTransportWindowTyZEGO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_StatusTransportWindow(object):
    def setupUi(self, StatusTransportWindow):
        if not StatusTransportWindow.objectName():
            StatusTransportWindow.setObjectName(u"StatusTransportWindow")
        StatusTransportWindow.resize(312, 92)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatusTransportWindow.sizePolicy().hasHeightForWidth())
        StatusTransportWindow.setSizePolicy(sizePolicy)
        StatusTransportWindow.setMinimumSize(QSize(0, 30))
        self.centralwidget = QWidget(StatusTransportWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.list_status_layout = QVBoxLayout()
        self.list_status_layout.setObjectName(u"list_status_layout")

        self.verticalLayout.addLayout(self.list_status_layout)

        StatusTransportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StatusTransportWindow)

        QMetaObject.connectSlotsByName(StatusTransportWindow)
    # setupUi

    def retranslateUi(self, StatusTransportWindow):
        StatusTransportWindow.setWindowTitle(QCoreApplication.translate("StatusTransportWindow", u"MainWindow", None))
    # retranslateUi

