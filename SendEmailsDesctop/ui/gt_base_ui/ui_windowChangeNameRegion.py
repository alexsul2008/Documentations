# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowChangeNameRegionfCcflH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_WindowChangeNameRegion(object):
    def setupUi(self, WindowChangeNameRegion):
        if not WindowChangeNameRegion.objectName():
            WindowChangeNameRegion.setObjectName(u"WindowChangeNameRegion")
        WindowChangeNameRegion.resize(519, 488)
        self.centralwidget = QWidget(WindowChangeNameRegion)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.lbl_id_region = QLabel(self.frame_top)
        self.lbl_id_region.setObjectName(u"lbl_id_region")
        self.lbl_id_region.setMaximumSize(QSize(0, 0))
        self.lbl_id_region.setLineWidth(0)

        self.horizontalLayout.addWidget(self.lbl_id_region)

        self.frame_4 = QFrame(self.frame_top)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setLineWidth(0)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_4)

        self.btn_close = QPushButton(self.frame_top)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(36, 36))
        self.btn_close.setMaximumSize(QSize(36, 36))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(235, 0, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame_top)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 0)
        self.le_name_region = QLineEdit(self.main_frame)
        self.le_name_region.setObjectName(u"le_name_region")
        self.le_name_region.setMinimumSize(QSize(0, 45))
        self.le_name_region.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_3.addWidget(self.le_name_region)

        self.scrollArea = QScrollArea(self.main_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 505, 304))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.add_widget_layout__region = QVBoxLayout()
        self.add_widget_layout__region.setSpacing(5)
        self.add_widget_layout__region.setObjectName(u"add_widget_layout__region")

        self.verticalLayout_4.addLayout(self.add_widget_layout__region)

        self.verticalSpacer = QSpacerItem(20, 185, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.footer_frame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.btn_save_region = QPushButton(self.footer_frame)
        self.btn_save_region.setObjectName(u"btn_save_region")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_save_region.sizePolicy().hasHeightForWidth())
        self.btn_save_region.setSizePolicy(sizePolicy2)
        self.btn_save_region.setMinimumSize(QSize(0, 50))
        self.btn_save_region.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_region.setIcon(icon1)
        self.btn_save_region.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_save_region)


        self.verticalLayout.addWidget(self.footer_frame)

        WindowChangeNameRegion.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(WindowChangeNameRegion)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        WindowChangeNameRegion.setStatusBar(self.statusBar)

        self.retranslateUi(WindowChangeNameRegion)

        QMetaObject.connectSlotsByName(WindowChangeNameRegion)
    # setupUi

    def retranslateUi(self, WindowChangeNameRegion):
        WindowChangeNameRegion.setWindowTitle(QCoreApplication.translate("WindowChangeNameRegion", u"MainWindow", None))
        self.lbl_id_region.setText("")
        self.label.setText(QCoreApplication.translate("WindowChangeNameRegion", u"\u0424\u043e\u0440\u043c\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0440\u0435\u0433\u0438\u043e\u043d\u0430 \u042d\u041a\u041f", None))
        self.btn_close.setText("")
        self.btn_save_region.setText(QCoreApplication.translate("WindowChangeNameRegion", u"  \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

