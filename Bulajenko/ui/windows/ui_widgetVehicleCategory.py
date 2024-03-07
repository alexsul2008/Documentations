# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetVehicleCategoryuEXAar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_widgetVehicleCategory(object):
    def setupUi(self, widgetVehicleCategory):
        if not widgetVehicleCategory.objectName():
            widgetVehicleCategory.setObjectName(u"widgetVehicleCategory")
        widgetVehicleCategory.resize(368, 32)
        self.verticalLayout = QVBoxLayout(widgetVehicleCategory)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_id_ts_cat = QLabel(widgetVehicleCategory)
        self.lbl_id_ts_cat.setObjectName(u"lbl_id_ts_cat")
        self.lbl_id_ts_cat.setMinimumSize(QSize(0, 0))
        self.lbl_id_ts_cat.setMaximumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lbl_id_ts_cat)

        self.le_vehicle_category = QLineEdit(widgetVehicleCategory)
        self.le_vehicle_category.setObjectName(u"le_vehicle_category")
        self.le_vehicle_category.setMinimumSize(QSize(0, 30))
        self.le_vehicle_category.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.le_vehicle_category)

        self.btn_save_ts_cat = QPushButton(widgetVehicleCategory)
        self.btn_save_ts_cat.setObjectName(u"btn_save_ts_cat")
        self.btn_save_ts_cat.setMinimumSize(QSize(30, 30))
        self.btn_save_ts_cat.setMaximumSize(QSize(30, 30))
        self.btn_save_ts_cat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_ts_cat.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_ts_cat.setIcon(icon)
        self.btn_save_ts_cat.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_save_ts_cat)

        self.btn_delete_ts_cat = QPushButton(widgetVehicleCategory)
        self.btn_delete_ts_cat.setObjectName(u"btn_delete_ts_cat")
        self.btn_delete_ts_cat.setMinimumSize(QSize(30, 30))
        self.btn_delete_ts_cat.setMaximumSize(QSize(30, 30))
        self.btn_delete_ts_cat.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_ts_cat.setIcon(icon1)
        self.btn_delete_ts_cat.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete_ts_cat)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(widgetVehicleCategory)

        QMetaObject.connectSlotsByName(widgetVehicleCategory)
    # setupUi

    def retranslateUi(self, widgetVehicleCategory):
        widgetVehicleCategory.setWindowTitle(QCoreApplication.translate("widgetVehicleCategory", u"Form", None))
        self.lbl_id_ts_cat.setText("")
        self.btn_save_ts_cat.setText("")
        self.btn_delete_ts_cat.setText("")
    # retranslateUi

