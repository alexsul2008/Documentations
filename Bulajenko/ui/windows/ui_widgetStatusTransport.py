# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetStatusTransportAlzqZw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_widgetStatusTransport(object):
    def setupUi(self, widgetStatusTransport):
        if not widgetStatusTransport.objectName():
            widgetStatusTransport.setObjectName(u"widgetStatusTransport")
        widgetStatusTransport.resize(347, 34)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetStatusTransport.sizePolicy().hasHeightForWidth())
        widgetStatusTransport.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(widgetStatusTransport)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.lbl_id = QLabel(widgetStatusTransport)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setMinimumSize(QSize(0, 0))
        self.lbl_id.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lbl_id)

        self.lbl_color = QLabel(widgetStatusTransport)
        self.lbl_color.setObjectName(u"lbl_color")
        self.lbl_color.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lbl_color)

        self.btn_status = QPushButton(widgetStatusTransport)
        self.btn_status.setObjectName(u"btn_status")
        self.btn_status.setMinimumSize(QSize(0, 30))
        self.btn_status.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_status.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_status)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(widgetStatusTransport)

        QMetaObject.connectSlotsByName(widgetStatusTransport)
    # setupUi

    def retranslateUi(self, widgetStatusTransport):
        widgetStatusTransport.setWindowTitle(QCoreApplication.translate("widgetStatusTransport", u"Form", None))
        self.lbl_id.setText("")
        self.lbl_color.setText("")
        self.btn_status.setText("")
    # retranslateUi

