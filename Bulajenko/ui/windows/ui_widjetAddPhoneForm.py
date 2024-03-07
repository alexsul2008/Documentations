# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widjetAddPhoneFormfasFBn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_widjetAddPhoneForm(object):
    def setupUi(self, widjetAddPhoneForm):
        if not widjetAddPhoneForm.objectName():
            widjetAddPhoneForm.setObjectName(u"widjetAddPhoneForm")
        widjetAddPhoneForm.resize(329, 48)
        widjetAddPhoneForm.setMaximumSize(QSize(330, 16777215))
        self.verticalLayout = QVBoxLayout(widjetAddPhoneForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.groupBox = QGroupBox(widjetAddPhoneForm)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.lbl_count = QLabel(self.groupBox)
        self.lbl_count.setObjectName(u"lbl_count")
        self.lbl_count.setMinimumSize(QSize(25, 0))
        self.lbl_count.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout.addWidget(self.lbl_count)

        self.le_phone = QLineEdit(self.groupBox)
        self.le_phone.setObjectName(u"le_phone")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_phone.sizePolicy().hasHeightForWidth())
        self.le_phone.setSizePolicy(sizePolicy1)
        self.le_phone.setMinimumSize(QSize(180, 26))
        self.le_phone.setMaximumSize(QSize(180, 26))

        self.horizontalLayout.addWidget(self.le_phone)

        self.add_phone = QPushButton(self.groupBox)
        self.add_phone.setObjectName(u"add_phone")
        self.add_phone.setMinimumSize(QSize(26, 26))
        self.add_phone.setMaximumSize(QSize(26, 26))
        self.add_phone.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/plus-square_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_phone.setIcon(icon)

        self.horizontalLayout.addWidget(self.add_phone)

        self.delete_phone = QPushButton(self.groupBox)
        self.delete_phone.setObjectName(u"delete_phone")
        self.delete_phone.setMinimumSize(QSize(26, 26))
        self.delete_phone.setMaximumSize(QSize(26, 26))
        self.delete_phone.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_phone.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_phone)

        self.lbl_id_phone = QLabel(self.groupBox)
        self.lbl_id_phone.setObjectName(u"lbl_id_phone")
        self.lbl_id_phone.setMinimumSize(QSize(0, 0))
        self.lbl_id_phone.setMaximumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lbl_id_phone)


        self.verticalLayout.addWidget(self.groupBox)

        self.gbx_msg = QGroupBox(widjetAddPhoneForm)
        self.gbx_msg.setObjectName(u"gbx_msg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gbx_msg.sizePolicy().hasHeightForWidth())
        self.gbx_msg.setSizePolicy(sizePolicy2)
        self.layout_msg = QHBoxLayout(self.gbx_msg)
        self.layout_msg.setSpacing(0)
        self.layout_msg.setObjectName(u"layout_msg")
        self.layout_msg.setContentsMargins(0, 0, 0, 0)
        self.lbl_msg = QLabel(self.gbx_msg)
        self.lbl_msg.setObjectName(u"lbl_msg")
        sizePolicy2.setHeightForWidth(self.lbl_msg.sizePolicy().hasHeightForWidth())
        self.lbl_msg.setSizePolicy(sizePolicy2)

        self.layout_msg.addWidget(self.lbl_msg)


        self.verticalLayout.addWidget(self.gbx_msg)


        self.retranslateUi(widjetAddPhoneForm)

        QMetaObject.connectSlotsByName(widjetAddPhoneForm)
    # setupUi

    def retranslateUi(self, widjetAddPhoneForm):
        widjetAddPhoneForm.setWindowTitle(QCoreApplication.translate("widjetAddPhoneForm", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("widjetAddPhoneForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lbl_count.setText("")
        self.add_phone.setText("")
        self.delete_phone.setText("")
        self.lbl_id_phone.setText("")
        self.lbl_msg.setText("")
    # retranslateUi

