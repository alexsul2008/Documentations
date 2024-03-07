# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetAdminRowXaoyYb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_widgetListsAdmins(object):
    def setupUi(self, widgetListsAdmins):
        if not widgetListsAdmins.objectName():
            widgetListsAdmins.setObjectName(u"widgetListsAdmins")
        widgetListsAdmins.resize(343, 30)
        widgetListsAdmins.setStyleSheet(u"QPushButton{	\n"
"	text-align: center;\n"
"}")
        self.horizontalLayout = QHBoxLayout(widgetListsAdmins)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_id_admin = QLabel(widgetListsAdmins)
        self.lbl_id_admin.setObjectName(u"lbl_id_admin")
        self.lbl_id_admin.setMinimumSize(QSize(0, 0))
        self.lbl_id_admin.setMaximumSize(QSize(0, 0))
        self.lbl_id_admin.setLineWidth(0)

        self.horizontalLayout.addWidget(self.lbl_id_admin)

        self.le_name_admin = QLineEdit(widgetListsAdmins)
        self.le_name_admin.setObjectName(u"le_name_admin")
        self.le_name_admin.setMinimumSize(QSize(0, 30))
        self.le_name_admin.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.le_name_admin)

        self.btn_save_admin = QPushButton(widgetListsAdmins)
        self.btn_save_admin.setObjectName(u"btn_save_admin")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_admin.sizePolicy().hasHeightForWidth())
        self.btn_save_admin.setSizePolicy(sizePolicy)
        self.btn_save_admin.setMinimumSize(QSize(30, 30))
        self.btn_save_admin.setMaximumSize(QSize(30, 30))
        self.btn_save_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_admin.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_admin.setIcon(icon)
        self.btn_save_admin.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_save_admin)

        self.btn_delete_admin = QPushButton(widgetListsAdmins)
        self.btn_delete_admin.setObjectName(u"btn_delete_admin")
        self.btn_delete_admin.setMinimumSize(QSize(30, 30))
        self.btn_delete_admin.setMaximumSize(QSize(30, 30))
        self.btn_delete_admin.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_admin.setIcon(icon1)
        self.btn_delete_admin.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_delete_admin)


        self.retranslateUi(widgetListsAdmins)

        QMetaObject.connectSlotsByName(widgetListsAdmins)
    # setupUi

    def retranslateUi(self, widgetListsAdmins):
        widgetListsAdmins.setWindowTitle(QCoreApplication.translate("widgetListsAdmins", u"Form", None))
        self.lbl_id_admin.setText("")
#if QT_CONFIG(tooltip)
        self.btn_save_admin.setToolTip(QCoreApplication.translate("widgetListsAdmins", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_admin.setText("")
#if QT_CONFIG(tooltip)
        self.btn_delete_admin.setToolTip(QCoreApplication.translate("widgetListsAdmins", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.btn_delete_admin.setText("")
    # retranslateUi

