# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetColorTransportOAYrnj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_widgetColorTransport(object):
    def setupUi(self, widgetColorTransport):
        if not widgetColorTransport.objectName():
            widgetColorTransport.setObjectName(u"widgetColorTransport")
        widgetColorTransport.resize(347, 34)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetColorTransport.sizePolicy().hasHeightForWidth())
        widgetColorTransport.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(widgetColorTransport)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.lbl_id = QLabel(widgetColorTransport)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setMinimumSize(QSize(0, 0))
        self.lbl_id.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lbl_id)

        self.lbl_color = QLabel(widgetColorTransport)
        self.lbl_color.setObjectName(u"lbl_color")
        self.lbl_color.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lbl_color)

        self.btn_name = QPushButton(widgetColorTransport)
        self.btn_name.setObjectName(u"btn_name")
        self.btn_name.setMinimumSize(QSize(0, 30))
        self.btn_name.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_name.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(widgetColorTransport)

        QMetaObject.connectSlotsByName(widgetColorTransport)
    # setupUi

    def retranslateUi(self, widgetColorTransport):
        widgetColorTransport.setWindowTitle(QCoreApplication.translate("widgetColorTransport", u"Form", None))
        self.lbl_id.setText("")
        self.lbl_color.setText("")
        self.btn_name.setText("")
    # retranslateUi

