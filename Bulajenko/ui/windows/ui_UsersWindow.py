# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UsersWindowFyyzMH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_AdminSystem(object):
    def setupUi(self, AdminSystem):
        if not AdminSystem.objectName():
            AdminSystem.setObjectName(u"AdminSystem")
        AdminSystem.resize(1100, 576)
        AdminSystem.setMinimumSize(QSize(1100, 50))
        AdminSystem.setStyleSheet(u"")
        self.centralwidget = QWidget(AdminSystem)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_users = QWidget()
        self.page_users.setObjectName(u"page_users")
        self.verticalLayout_2 = QVBoxLayout(self.page_users)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_add_user = QPushButton(self.page_users)
        self.btn_add_user.setObjectName(u"btn_add_user")
        self.btn_add_user.setMinimumSize(QSize(200, 40))
        self.btn_add_user.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/user-plus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_user.setIcon(icon)
        self.btn_add_user.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_add_user, 0, Qt.AlignRight)

        self.groupBox = QGroupBox(self.page_users)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 32))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(40, 16777215))
        self.label.setStyleSheet(u"padding-left: 5px;")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setMaximumSize(QSize(200, 16777215))
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lbl_date_create = QLabel(self.groupBox)
        self.lbl_date_create.setObjectName(u"lbl_date_create")
        self.lbl_date_create.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_2.addWidget(self.lbl_date_create)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(126, 0))
        self.label_7.setMaximumSize(QSize(126, 16777215))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.scrollArea = QScrollArea(self.page_users)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1151, 408))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_widget_layout = QVBoxLayout()
        self.add_widget_layout.setSpacing(0)
        self.add_widget_layout.setObjectName(u"add_widget_layout")
        self.add_widget_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.add_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addLayout(self.add_widget_layout)

        self.verticalSpacer = QSpacerItem(20, 2000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_users)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_4 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frm_settings = QFrame(self.page_settings)
        self.frm_settings.setObjectName(u"frm_settings")
        self.frm_settings.setMaximumSize(QSize(360, 16777215))
        self.frm_settings.setFrameShape(QFrame.StyledPanel)
        self.frm_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm_settings)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 10, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.label_22 = QLabel(self.frm_settings)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(24, 24))
        self.label_22.setMaximumSize(QSize(24, 24))
        self.label_22.setPixmap(QPixmap(u":/Icons/icons/sun_.svg"))
        self.label_22.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.label_8 = QLabel(self.frm_settings)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.label_8)

        self.btn_add_color_ts = QPushButton(self.frm_settings)
        self.btn_add_color_ts.setObjectName(u"btn_add_color_ts")
        self.btn_add_color_ts.setMinimumSize(QSize(40, 40))
        self.btn_add_color_ts.setMaximumSize(QSize(40, 40))
        self.btn_add_color_ts.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/plus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_color_ts.setIcon(icon1)
        self.btn_add_color_ts.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_add_color_ts)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.label_14 = QLabel(self.frm_settings)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(0, 16777215))

        self.horizontalLayout_6.addWidget(self.label_14)

        self.label_10 = QLabel(self.frm_settings)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.label_11 = QLabel(self.frm_settings)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.frm_settings)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(30, 30))
        self.label_12.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.frm_settings)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(30, 30))
        self.label_13.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.label_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.scrollAreaSettings_2 = QScrollArea(self.frm_settings)
        self.scrollAreaSettings_2.setObjectName(u"scrollAreaSettings_2")
        self.scrollAreaSettings_2.setWidgetResizable(True)
        self.scroll_settings_2 = QWidget()
        self.scroll_settings_2.setObjectName(u"scroll_settings_2")
        self.scroll_settings_2.setGeometry(QRect(0, 0, 333, 394))
        self.verticalLayout_5 = QVBoxLayout(self.scroll_settings_2)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.layout_colored_ts = QVBoxLayout()
        self.layout_colored_ts.setSpacing(5)
        self.layout_colored_ts.setObjectName(u"layout_colored_ts")

        self.verticalLayout_5.addLayout(self.layout_colored_ts)

        self.verticalSpacer_2 = QSpacerItem(20, 398, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.scrollAreaSettings_2.setWidget(self.scroll_settings_2)

        self.verticalLayout_3.addWidget(self.scrollAreaSettings_2)


        self.horizontalLayout_4.addWidget(self.frm_settings)

        self.frm_settings_2 = QFrame(self.page_settings)
        self.frm_settings_2.setObjectName(u"frm_settings_2")
        self.frm_settings_2.setMaximumSize(QSize(360, 16777215))
        self.frm_settings_2.setFrameShape(QFrame.StyledPanel)
        self.frm_settings_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_settings_2)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 10, 5)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.label_23 = QLabel(self.frm_settings_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(24, 24))
        self.label_23.setMaximumSize(QSize(24, 24))
        self.label_23.setPixmap(QPixmap(u":/Icons/icons/award_.svg"))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_23)

        self.label_9 = QLabel(self.frm_settings_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.label_9)

        self.btn_add_payment_category = QPushButton(self.frm_settings_2)
        self.btn_add_payment_category.setObjectName(u"btn_add_payment_category")
        self.btn_add_payment_category.setMinimumSize(QSize(40, 40))
        self.btn_add_payment_category.setMaximumSize(QSize(40, 40))
        self.btn_add_payment_category.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_payment_category.setIcon(icon1)
        self.btn_add_payment_category.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_add_payment_category)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.label_17 = QLabel(self.frm_settings_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.label_16 = QLabel(self.frm_settings_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(30, 30))
        self.label_16.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.label_16)

        self.label_15 = QLabel(self.frm_settings_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(30, 30))
        self.label_15.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.label_15)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.scrollAreaSettings_3 = QScrollArea(self.frm_settings_2)
        self.scrollAreaSettings_3.setObjectName(u"scrollAreaSettings_3")
        self.scrollAreaSettings_3.setWidgetResizable(True)
        self.scroll_settings_3 = QWidget()
        self.scroll_settings_3.setObjectName(u"scroll_settings_3")
        self.scroll_settings_3.setGeometry(QRect(0, 0, 333, 394))
        self.verticalLayout_6 = QVBoxLayout(self.scroll_settings_3)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.layout_payment_category = QVBoxLayout()
        self.layout_payment_category.setSpacing(5)
        self.layout_payment_category.setObjectName(u"layout_payment_category")

        self.verticalLayout_6.addLayout(self.layout_payment_category)

        self.verticalSpacer_3 = QSpacerItem(20, 398, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.scrollAreaSettings_3.setWidget(self.scroll_settings_3)

        self.verticalLayout_4.addWidget(self.scrollAreaSettings_3)


        self.horizontalLayout_4.addWidget(self.frm_settings_2)

        self.frm_settings_3 = QFrame(self.page_settings)
        self.frm_settings_3.setObjectName(u"frm_settings_3")
        self.frm_settings_3.setMaximumSize(QSize(360, 16777215))
        self.frm_settings_3.setFrameShape(QFrame.StyledPanel)
        self.frm_settings_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frm_settings_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.label_24 = QLabel(self.frm_settings_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(24, 24))
        self.label_24.setMaximumSize(QSize(24, 24))
        self.label_24.setPixmap(QPixmap(u":/Icons/icons/truck_.svg"))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_24)

        self.label_21 = QLabel(self.frm_settings_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 30))
        self.label_21.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_9.addWidget(self.label_21)

        self.btn_add_view_ts = QPushButton(self.frm_settings_3)
        self.btn_add_view_ts.setObjectName(u"btn_add_view_ts")
        self.btn_add_view_ts.setMinimumSize(QSize(40, 40))
        self.btn_add_view_ts.setMaximumSize(QSize(40, 40))
        self.btn_add_view_ts.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_view_ts.setIcon(icon1)
        self.btn_add_view_ts.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.btn_add_view_ts)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.label_18 = QLabel(self.frm_settings_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_18)

        self.label_19 = QLabel(self.frm_settings_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(30, 30))
        self.label_19.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.label_19)

        self.label_20 = QLabel(self.frm_settings_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(30, 30))
        self.label_20.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.label_20)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.scrollAreaSettings_4 = QScrollArea(self.frm_settings_3)
        self.scrollAreaSettings_4.setObjectName(u"scrollAreaSettings_4")
        self.scrollAreaSettings_4.setWidgetResizable(True)
        self.scroll_settings_4 = QWidget()
        self.scroll_settings_4.setObjectName(u"scroll_settings_4")
        self.scroll_settings_4.setGeometry(QRect(0, 0, 330, 384))
        self.verticalLayout_7 = QVBoxLayout(self.scroll_settings_4)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.layout_view_ts = QVBoxLayout()
        self.layout_view_ts.setSpacing(5)
        self.layout_view_ts.setObjectName(u"layout_view_ts")

        self.verticalLayout_7.addLayout(self.layout_view_ts)

        self.verticalSpacer_4 = QSpacerItem(20, 398, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.scrollAreaSettings_4.setWidget(self.scroll_settings_4)

        self.verticalLayout_8.addWidget(self.scrollAreaSettings_4)


        self.horizontalLayout_4.addWidget(self.frm_settings_3)

        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout.addWidget(self.stackedWidget)

        AdminSystem.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(AdminSystem)
        self.statusBar.setObjectName(u"statusBar")
        AdminSystem.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(AdminSystem)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 40))
        AdminSystem.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(AdminSystem)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AdminSystem)
    # setupUi

    def retranslateUi(self, AdminSystem):
        AdminSystem.setWindowTitle(QCoreApplication.translate("AdminSystem", u"MainWindow", None))
        self.btn_add_user.setText(QCoreApplication.translate("AdminSystem", u" \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("AdminSystem", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("AdminSystem", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("AdminSystem", u"\u0418\u043c\u044f", None))
        self.label_4.setText(QCoreApplication.translate("AdminSystem", u"E-mail", None))
        self.label_5.setText(QCoreApplication.translate("AdminSystem", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_6.setText(QCoreApplication.translate("AdminSystem", u"\u041f\u0440\u0430\u0432\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.lbl_date_create.setText(QCoreApplication.translate("AdminSystem", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("AdminSystem", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.label_22.setText("")
        self.label_8.setText(QCoreApplication.translate("AdminSystem", u"\u0426\u0432\u0435\u0442\u0430 \u0422\u0421", None))
#if QT_CONFIG(tooltip)
        self.btn_add_color_ts.setToolTip(QCoreApplication.translate("AdminSystem", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0446\u0432\u0435\u0442", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_color_ts.setText("")
        self.label_14.setText("")
        self.label_10.setText(QCoreApplication.translate("AdminSystem", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430", None))
        self.label_11.setText(QCoreApplication.translate("AdminSystem", u"Hex-\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430", None))
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_23.setText("")
        self.label_9.setText(QCoreApplication.translate("AdminSystem", u"\u0426\u0435\u043d\u043e\u0432\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.btn_add_payment_category.setToolTip(QCoreApplication.translate("AdminSystem", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0446\u0432\u0435\u0442", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_payment_category.setText("")
        self.label_17.setText(QCoreApplication.translate("AdminSystem", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_16.setText("")
        self.label_15.setText("")
        self.label_24.setText("")
        self.label_21.setText(QCoreApplication.translate("AdminSystem", u"\u0422\u0438\u043f \u0422\u0421", None))
#if QT_CONFIG(tooltip)
        self.btn_add_view_ts.setToolTip(QCoreApplication.translate("AdminSystem", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0446\u0432\u0435\u0442", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_view_ts.setText("")
        self.label_18.setText(QCoreApplication.translate("AdminSystem", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0422\u0421", None))
        self.label_19.setText("")
        self.label_20.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("AdminSystem", u"toolBar", None))
    # retranslateUi

