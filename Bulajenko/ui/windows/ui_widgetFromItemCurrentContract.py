# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetFromItemCurrentContractNciwRO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_FormItemCurrentContract(object):
    def setupUi(self, FormItemCurrentContract):
        if not FormItemCurrentContract.objectName():
            FormItemCurrentContract.setObjectName(u"FormItemCurrentContract")
        FormItemCurrentContract.resize(330, 36)
        self.horizontalLayout = QHBoxLayout(FormItemCurrentContract)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_delay = QPushButton(FormItemCurrentContract)
        self.btn_delay.setObjectName(u"btn_delay")
        self.btn_delay.setMinimumSize(QSize(0, 36))
        self.btn_delay.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_delay)

        self.btn_confirm_pay = QPushButton(FormItemCurrentContract)
        self.btn_confirm_pay.setObjectName(u"btn_confirm_pay")
        self.btn_confirm_pay.setMinimumSize(QSize(150, 36))
        self.btn_confirm_pay.setMaximumSize(QSize(150, 16777215))
        self.btn_confirm_pay.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_confirm_pay)

        self.btn_return = QPushButton(FormItemCurrentContract)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setMinimumSize(QSize(0, 36))
        self.btn_return.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_return)


        self.retranslateUi(FormItemCurrentContract)

        QMetaObject.connectSlotsByName(FormItemCurrentContract)
    # setupUi

    def retranslateUi(self, FormItemCurrentContract):
        FormItemCurrentContract.setWindowTitle(QCoreApplication.translate("FormItemCurrentContract", u"Form", None))
        self.btn_delay.setText(QCoreApplication.translate("FormItemCurrentContract", u"\u041e\u0442\u0441\u0440\u043e\u0447\u043a\u0430", None))
        self.btn_confirm_pay.setText(QCoreApplication.translate("FormItemCurrentContract", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043f\u043b\u0430\u0442\u0435\u0436", None))
        self.btn_return.setText(QCoreApplication.translate("FormItemCurrentContract", u"\u0412\u043e\u0437\u0432\u0440\u0430\u0442", None))
    # retranslateUi

