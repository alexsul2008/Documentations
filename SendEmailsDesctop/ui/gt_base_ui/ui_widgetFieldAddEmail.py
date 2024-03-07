# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetFieldAddEmailhNmBrg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_WidgetAddEmailOperator(object):
    def setupUi(self, WidgetAddEmailOperator):
        if not WidgetAddEmailOperator.objectName():
            WidgetAddEmailOperator.setObjectName(u"WidgetAddEmailOperator")
        WidgetAddEmailOperator.setEnabled(True)
        WidgetAddEmailOperator.resize(882, 74)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetAddEmailOperator.sizePolicy().hasHeightForWidth())
        WidgetAddEmailOperator.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        WidgetAddEmailOperator.setFont(font)
        self.verticalLayout = QVBoxLayout(WidgetAddEmailOperator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.grb_add_email = QGroupBox(WidgetAddEmailOperator)
        self.grb_add_email.setObjectName(u"grb_add_email")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.grb_add_email.sizePolicy().hasHeightForWidth())
        self.grb_add_email.setSizePolicy(sizePolicy1)
        self.grb_add_email.setMinimumSize(QSize(0, 65))
        self.grb_add_email.setMaximumSize(QSize(16777215, 16777215))
        self.grb_add_email.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.grb_add_email)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 5)
        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.lineEditNewEmall = QLineEdit(self.grb_add_email)
        self.lineEditNewEmall.setObjectName(u"lineEditNewEmall")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditNewEmall.sizePolicy().hasHeightForWidth())
        self.lineEditNewEmall.setSizePolicy(sizePolicy2)
        self.lineEditNewEmall.setMinimumSize(QSize(0, 40))
        self.lineEditNewEmall.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.lineEditNewEmall.setFont(font1)

        self.gridLayout.addWidget(self.lineEditNewEmall, 0, 3, 1, 1, Qt.AlignTop)

        self.horizontalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.labelError = QLabel(self.grb_add_email)
        self.labelError.setObjectName(u"labelError")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelError.sizePolicy().hasHeightForWidth())
        self.labelError.setSizePolicy(sizePolicy3)
        self.labelError.setMinimumSize(QSize(0, 0))
        self.labelError.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(8)
        self.labelError.setFont(font2)
        self.labelError.setMargin(5)

        self.gridLayout.addWidget(self.labelError, 2, 3, 1, 1, Qt.AlignTop)

        self.lbl_add_email_operator = QLabel(self.grb_add_email)
        self.lbl_add_email_operator.setObjectName(u"lbl_add_email_operator")
        self.lbl_add_email_operator.setMinimumSize(QSize(40, 40))
        self.lbl_add_email_operator.setBaseSize(QSize(0, 0))
        self.lbl_add_email_operator.setFrameShape(QFrame.NoFrame)
        self.lbl_add_email_operator.setFrameShadow(QFrame.Plain)
        self.lbl_add_email_operator.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_add_email_operator, 0, 0, 1, 1, Qt.AlignTop)

        self.btn_delete_email_operator = QPushButton(self.grb_add_email)
        self.btn_delete_email_operator.setObjectName(u"btn_delete_email_operator")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_delete_email_operator.sizePolicy().hasHeightForWidth())
        self.btn_delete_email_operator.setSizePolicy(sizePolicy4)
        self.btn_delete_email_operator.setMinimumSize(QSize(40, 40))
        self.btn_delete_email_operator.setMaximumSize(QSize(40, 40))
        self.btn_delete_email_operator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_email_operator.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_email_operator.setIcon(icon)
        self.btn_delete_email_operator.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_delete_email_operator, 0, 5, 3, 1, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 3, 1, 1)

        self.lbl_email_id = QLabel(self.grb_add_email)
        self.lbl_email_id.setObjectName(u"lbl_email_id")
        self.lbl_email_id.setMaximumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.lbl_email_id, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.grb_add_email)


        self.retranslateUi(WidgetAddEmailOperator)

        QMetaObject.connectSlotsByName(WidgetAddEmailOperator)
    # setupUi

    def retranslateUi(self, WidgetAddEmailOperator):
        WidgetAddEmailOperator.setWindowTitle(QCoreApplication.translate("WidgetAddEmailOperator", u"Form", None))
        self.labelError.setText("")
        self.lbl_add_email_operator.setText("")
        self.btn_delete_email_operator.setText("")
        self.lbl_email_id.setText("")
    # retranslateUi

