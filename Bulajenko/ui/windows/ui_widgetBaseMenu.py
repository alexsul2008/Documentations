# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetBaseMenuWxCEMz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_baseMenu(object):
    def setupUi(self, baseMenu):
        if not baseMenu.objectName():
            baseMenu.setObjectName(u"baseMenu")
        baseMenu.resize(270, 542)
        baseMenu.setMaximumSize(QSize(280, 16777215))
        self.verticalLayout_2 = QVBoxLayout(baseMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalFrame = QFrame(baseMenu)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_list_arendators = QPushButton(self.verticalFrame)
        self.btn_list_arendators.setObjectName(u"btn_list_arendators")
        self.btn_list_arendators.setMinimumSize(QSize(0, 36))
        self.btn_list_arendators.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_list_arendators)

        self.btn_list_ts = QPushButton(self.verticalFrame)
        self.btn_list_ts.setObjectName(u"btn_list_ts")
        self.btn_list_ts.setMinimumSize(QSize(0, 36))
        self.btn_list_ts.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_list_ts)

        self.btn_add_arendator = QPushButton(self.verticalFrame)
        self.btn_add_arendator.setObjectName(u"btn_add_arendator")
        self.btn_add_arendator.setMinimumSize(QSize(0, 36))
        self.btn_add_arendator.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_add_arendator)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_add_ts = QPushButton(self.verticalFrame)
        self.btn_add_ts.setObjectName(u"btn_add_ts")
        self.btn_add_ts.setMinimumSize(QSize(0, 36))
        self.btn_add_ts.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_add_ts)

        self.btn_user = QPushButton(self.verticalFrame)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setMinimumSize(QSize(0, 36))
        self.btn_user.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_user)


        self.verticalLayout_2.addWidget(self.verticalFrame)


        self.retranslateUi(baseMenu)

        QMetaObject.connectSlotsByName(baseMenu)
    # setupUi

    def retranslateUi(self, baseMenu):
        baseMenu.setWindowTitle(QCoreApplication.translate("baseMenu", u"Form", None))
        self.btn_list_arendators.setText(QCoreApplication.translate("baseMenu", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        self.btn_list_ts.setText(QCoreApplication.translate("baseMenu", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0422\u0421", None))
        self.btn_add_arendator.setText(QCoreApplication.translate("baseMenu", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430/ \u0437\u0430\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.btn_add_ts.setText(QCoreApplication.translate("baseMenu", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0422\u0421", None))
        self.btn_user.setText(QCoreApplication.translate("baseMenu", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

