# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetFromItemClosedContractYAwmgw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_FormItemClosedContract(object):
    def setupUi(self, FormItemClosedContract):
        if not FormItemClosedContract.objectName():
            FormItemClosedContract.setObjectName(u"FormItemClosedContract")
        FormItemClosedContract.resize(330, 36)
        self.horizontalLayout = QHBoxLayout(FormItemClosedContract)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_issue_another = QPushButton(FormItemClosedContract)
        self.btn_issue_another.setObjectName(u"btn_issue_another")
        self.btn_issue_another.setMinimumSize(QSize(150, 36))
        self.btn_issue_another.setMaximumSize(QSize(150, 16777215))
        self.btn_issue_another.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_issue_another)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(FormItemClosedContract)

        QMetaObject.connectSlotsByName(FormItemClosedContract)
    # setupUi

    def retranslateUi(self, FormItemClosedContract):
        FormItemClosedContract.setWindowTitle(QCoreApplication.translate("FormItemClosedContract", u"Form", None))
        self.btn_issue_another.setText(QCoreApplication.translate("FormItemClosedContract", u"\u0412\u044b\u0434\u0430\u0442\u044c \u0434\u0440\u0443\u0433\u043e\u0439", None))
    # retranslateUi

