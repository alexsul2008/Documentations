# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetPaymentCategorygxDuNq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_widgetPaymentCategory(object):
    def setupUi(self, widgetPaymentCategory):
        if not widgetPaymentCategory.objectName():
            widgetPaymentCategory.setObjectName(u"widgetPaymentCategory")
        widgetPaymentCategory.resize(368, 32)
        self.verticalLayout = QVBoxLayout(widgetPaymentCategory)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_id_pcat = QLabel(widgetPaymentCategory)
        self.lbl_id_pcat.setObjectName(u"lbl_id_pcat")
        self.lbl_id_pcat.setMinimumSize(QSize(0, 0))
        self.lbl_id_pcat.setMaximumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lbl_id_pcat)

        self.le_paymen_category = QLineEdit(widgetPaymentCategory)
        self.le_paymen_category.setObjectName(u"le_paymen_category")
        self.le_paymen_category.setMinimumSize(QSize(0, 30))
        self.le_paymen_category.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.le_paymen_category)

        self.btn_save_pcat = QPushButton(widgetPaymentCategory)
        self.btn_save_pcat.setObjectName(u"btn_save_pcat")
        self.btn_save_pcat.setMinimumSize(QSize(30, 30))
        self.btn_save_pcat.setMaximumSize(QSize(30, 30))
        self.btn_save_pcat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_pcat.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_pcat.setIcon(icon)
        self.btn_save_pcat.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_save_pcat)

        self.btn_delete_pcat = QPushButton(widgetPaymentCategory)
        self.btn_delete_pcat.setObjectName(u"btn_delete_pcat")
        self.btn_delete_pcat.setMinimumSize(QSize(30, 30))
        self.btn_delete_pcat.setMaximumSize(QSize(30, 30))
        self.btn_delete_pcat.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_pcat.setIcon(icon1)
        self.btn_delete_pcat.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete_pcat)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(widgetPaymentCategory)

        QMetaObject.connectSlotsByName(widgetPaymentCategory)
    # setupUi

    def retranslateUi(self, widgetPaymentCategory):
        widgetPaymentCategory.setWindowTitle(QCoreApplication.translate("widgetPaymentCategory", u"Form", None))
        self.lbl_id_pcat.setText("")
        self.btn_save_pcat.setText("")
        self.btn_delete_pcat.setText("")
    # retranslateUi

