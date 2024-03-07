# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetAddColorTransportKyiyfE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_widgetAddColorTransport(object):
    def setupUi(self, widgetAddColorTransport):
        if not widgetAddColorTransport.objectName():
            widgetAddColorTransport.setObjectName(u"widgetAddColorTransport")
        widgetAddColorTransport.resize(344, 32)
        self.verticalLayout = QVBoxLayout(widgetAddColorTransport)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.lbl_id = QLabel(widgetAddColorTransport)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setMinimumSize(QSize(0, 0))
        self.lbl_id.setMaximumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lbl_id)

        self.le_name_color = QLineEdit(widgetAddColorTransport)
        self.le_name_color.setObjectName(u"le_name_color")
        self.le_name_color.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.le_name_color)

        self.le_hex_color = QLineEdit(widgetAddColorTransport)
        self.le_hex_color.setObjectName(u"le_hex_color")
        self.le_hex_color.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.le_hex_color)

        self.btn_save = QPushButton(widgetAddColorTransport)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(30, 30))
        self.btn_save.setMaximumSize(QSize(30, 30))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_delete = QPushButton(widgetAddColorTransport)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(30, 30))
        self.btn_delete.setMaximumSize(QSize(30, 30))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(widgetAddColorTransport)

        QMetaObject.connectSlotsByName(widgetAddColorTransport)
    # setupUi

    def retranslateUi(self, widgetAddColorTransport):
        widgetAddColorTransport.setWindowTitle(QCoreApplication.translate("widgetAddColorTransport", u"Form", None))
        self.lbl_id.setText("")
        self.btn_save.setText("")
        self.btn_delete.setText("")
    # retranslateUi

