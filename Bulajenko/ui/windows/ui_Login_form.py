# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_formEPlFKd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(377, 652)
        LoginWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.central = QFrame(self.centralwidget)
        self.central.setObjectName(u"central")
        self.central.setFrameShape(QFrame.StyledPanel)
        self.central.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.frame_top = QFrame(self.central)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 0))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_top)

        self.btnClose = QPushButton(self.central)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(36, 36))
        self.btnClose.setMaximumSize(QSize(36, 36))
        self.btnClose.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon)
        self.btnClose.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.btnClose)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo = QLabel(self.central)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(150, 150))
        self.logo.setMaximumSize(QSize(150, 150))
        self.logo.setPixmap(QPixmap(u":/Icons/icons/aperture_.svg"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logo)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.le_username = QLineEdit(self.central)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setMinimumSize(QSize(0, 50))
        self.le_username.setMaximumSize(QSize(16777215, 50))
        self.le_username.setTabletTracking(True)
        self.le_username.setStyleSheet(u"")
        self.le_username.setInputMethodHints(Qt.ImhNone)
        self.le_username.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.le_username)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.le_password = QLineEdit(self.central)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMinimumSize(QSize(0, 50))
        self.le_password.setMaximumSize(QSize(16777215, 50))
        self.le_password.setTabletTracking(True)
        self.le_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.le_password)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.btnSignIn = QPushButton(self.central)
        self.btnSignIn.setObjectName(u"btnSignIn")
        self.btnSignIn.setMinimumSize(QSize(0, 60))
        self.btnSignIn.setMaximumSize(QSize(16777215, 60))
        self.btnSignIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSignIn.setTabletTracking(True)

        self.verticalLayout.addWidget(self.btnSignIn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Login_response = QLabel(self.central)
        self.Login_response.setObjectName(u"Login_response")
        self.Login_response.setMinimumSize(QSize(0, 50))
        self.Login_response.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Login_response)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.central, 0, 0, 1, 1)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"LoginWindow", None))
        self.btnClose.setText("")
        self.logo.setText("")
        self.btnSignIn.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.Login_response.setText("")
    # retranslateUi

