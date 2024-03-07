# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowttSqSm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1248, 842)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_top = QFrame(self.centralwidget)
        self.frm_top.setObjectName(u"frm_top")
        self.frm_top.setMinimumSize(QSize(0, 50))
        self.frm_top.setMaximumSize(QSize(16777215, 50))
        self.frm_top.setFrameShape(QFrame.StyledPanel)
        self.frm_top.setFrameShadow(QFrame.Raised)
        self.frm_top.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.frm_top)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 0)
        self.btn_hamburger_menu = QPushButton(self.frm_top)
        self.btn_hamburger_menu.setObjectName(u"btn_hamburger_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_hamburger_menu.sizePolicy().hasHeightForWidth())
        self.btn_hamburger_menu.setSizePolicy(sizePolicy1)
        self.btn_hamburger_menu.setMinimumSize(QSize(40, 0))
        self.btn_hamburger_menu.setMaximumSize(QSize(40, 16777215))
        self.btn_hamburger_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/menu_.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/Icons/icons/x_.svg", QSize(), QIcon.Disabled, QIcon.On)
        icon.addFile(u":/Icons/icons/x_.svg", QSize(), QIcon.Active, QIcon.On)
        self.btn_hamburger_menu.setIcon(icon)
        self.btn_hamburger_menu.setIconSize(QSize(30, 30))
        self.btn_hamburger_menu.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_hamburger_menu)

        self.horizontalSpacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 20, 0)
        self.lbl_role_name = QLabel(self.frm_top)
        self.lbl_role_name.setObjectName(u"lbl_role_name")
        self.lbl_role_name.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_5.addWidget(self.lbl_role_name)

        self.lbl_name_user = QLabel(self.frm_top)
        self.lbl_name_user.setObjectName(u"lbl_name_user")
        self.lbl_name_user.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_5.addWidget(self.lbl_name_user)

        self.role = QLabel(self.frm_top)
        self.role.setObjectName(u"role")
        self.role.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.role)


        self.horizontalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.frm_top)

        self.frm_content = QFrame(self.centralwidget)
        self.frm_content.setObjectName(u"frm_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frm_content.sizePolicy().hasHeightForWidth())
        self.frm_content.setSizePolicy(sizePolicy2)
        self.frm_content.setFrameShape(QFrame.NoFrame)
        self.frm_content.setFrameShadow(QFrame.Raised)
        self.layoutContent = QVBoxLayout(self.frm_content)
        self.layoutContent.setSpacing(5)
        self.layoutContent.setObjectName(u"layoutContent")
        self.layoutContent.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frm_content)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_base = QWidget()
        self.tab_base.setObjectName(u"tab_base")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_base)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.charts_layout = QVBoxLayout()
        self.charts_layout.setSpacing(5)
        self.charts_layout.setObjectName(u"charts_layout")

        self.horizontalLayout_4.addLayout(self.charts_layout)

        self.tabWidget.addTab(self.tab_base, "")
        self.tab_arendators_window = QWidget()
        self.tab_arendators_window.setObjectName(u"tab_arendators_window")
        self.tab_arendators_window.setLayoutDirection(Qt.LeftToRight)
        self.layout_arendators_window = QVBoxLayout(self.tab_arendators_window)
        self.layout_arendators_window.setSpacing(0)
        self.layout_arendators_window.setObjectName(u"layout_arendators_window")
        self.layout_arendators_window.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_arendators_window, "")

        self.layoutContent.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frm_content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_hamburger_menu.setText("")
        self.lbl_role_name.setText("")
        self.lbl_name_user.setText("")
        self.role.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_base), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_arendators_window), QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
    # retranslateUi

