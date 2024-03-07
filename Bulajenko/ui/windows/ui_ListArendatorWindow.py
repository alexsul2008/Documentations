# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListArendatorWindowvSEBjR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_ListArendatorWindow(object):
    def setupUi(self, ListArendatorWindow):
        if not ListArendatorWindow.objectName():
            ListArendatorWindow.setObjectName(u"ListArendatorWindow")
        ListArendatorWindow.resize(1300, 903)
        ListArendatorWindow.setMinimumSize(QSize(1300, 0))
        ListArendatorWindow.setMaximumSize(QSize(1300, 16777215))
        ListArendatorWindow.setStyleSheet(u"")
        self.action = QAction(ListArendatorWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(ListArendatorWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 15, 0, 5)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 10, -1, 10)
        self.btn_add_client = QPushButton(self.centralwidget)
        self.btn_add_client.setObjectName(u"btn_add_client")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_client.sizePolicy().hasHeightForWidth())
        self.btn_add_client.setSizePolicy(sizePolicy)
        self.btn_add_client.setMinimumSize(QSize(0, 36))
        self.btn_add_client.setMaximumSize(QSize(16777215, 16777215))
        self.btn_add_client.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_client.setLayoutDirection(Qt.LeftToRight)
        self.btn_add_client.setAutoFillBackground(False)
        self.btn_add_client.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/user-plus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_client.setIcon(icon)
        self.btn_add_client.setIconSize(QSize(26, 26))
        self.btn_add_client.setAutoDefault(False)
        self.btn_add_client.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btn_add_client)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.layoutFiltersContracts = QVBoxLayout()
        self.layoutFiltersContracts.setSpacing(5)
        self.layoutFiltersContracts.setObjectName(u"layoutFiltersContracts")
        self.layoutFiltersContracts.setContentsMargins(-1, -1, 28, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, 10, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 30))
        self.label_12.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_12)

        self.id_dogovor = QLineEdit(self.centralwidget)
        self.id_dogovor.setObjectName(u"id_dogovor")
        self.id_dogovor.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.id_dogovor)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 30))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.fio_arendator__text = QLineEdit(self.centralwidget)
        self.fio_arendator__text.setObjectName(u"fio_arendator__text")
        self.fio_arendator__text.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.fio_arendator__text)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 30))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.date_contract = QComboBox(self.centralwidget)
        self.date_contract.setObjectName(u"date_contract")
        self.date_contract.setMinimumSize(QSize(250, 30))
        self.date_contract.setMaximumSize(QSize(250, 16777215))
        self.date_contract.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.date_contract)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 15))
        self.label_16.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.label_16)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 15))
        self.label_15.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.label_15)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(200, 0))
        self.label_14.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_8.addWidget(self.label_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.grb_status = QGroupBox(self.centralwidget)
        self.grb_status.setObjectName(u"grb_status")
        self.grb_status.setMinimumSize(QSize(150, 0))
        self.grb_status.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout = QVBoxLayout(self.grb_status)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.status_contract___all = QRadioButton(self.grb_status)
        self.status_contract___all.setObjectName(u"status_contract___all")
        self.status_contract___all.setMinimumSize(QSize(0, 30))
        self.status_contract___all.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_contract___all.setChecked(True)

        self.verticalLayout.addWidget(self.status_contract___all)

        self.status_contract__open = QRadioButton(self.grb_status)
        self.status_contract__open.setObjectName(u"status_contract__open")
        self.status_contract__open.setMinimumSize(QSize(0, 30))
        self.status_contract__open.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.status_contract__open)

        self.status_contract__close = QRadioButton(self.grb_status)
        self.status_contract__close.setObjectName(u"status_contract__close")
        self.status_contract__close.setMinimumSize(QSize(0, 30))
        self.status_contract__close.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.status_contract__close)


        self.horizontalLayout_7.addWidget(self.grb_status, 0, Qt.AlignTop)

        self.grb_date_pay = QGroupBox(self.centralwidget)
        self.grb_date_pay.setObjectName(u"grb_date_pay")
        self.grb_date_pay.setMinimumSize(QSize(150, 0))
        self.grb_date_pay.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.grb_date_pay)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.estimated_date___all = QRadioButton(self.grb_date_pay)
        self.estimated_date___all.setObjectName(u"estimated_date___all")
        self.estimated_date___all.setMinimumSize(QSize(0, 30))
        self.estimated_date___all.setCursor(QCursor(Qt.PointingHandCursor))
        self.estimated_date___all.setChecked(True)

        self.verticalLayout_3.addWidget(self.estimated_date___all)

        self.estimated_date___today = QRadioButton(self.grb_date_pay)
        self.estimated_date___today.setObjectName(u"estimated_date___today")
        self.estimated_date___today.setMinimumSize(QSize(0, 30))
        self.estimated_date___today.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.estimated_date___today)

        self.estimated_date___tomorrow = QRadioButton(self.grb_date_pay)
        self.estimated_date___tomorrow.setObjectName(u"estimated_date___tomorrow")
        self.estimated_date___tomorrow.setMinimumSize(QSize(0, 30))
        self.estimated_date___tomorrow.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.estimated_date___tomorrow)


        self.horizontalLayout_7.addWidget(self.grb_date_pay, 0, Qt.AlignTop)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 5)
        self.vikup___ts = QCheckBox(self.centralwidget)
        self.vikup___ts.setObjectName(u"vikup___ts")
        self.vikup___ts.setMinimumSize(QSize(100, 26))
        self.vikup___ts.setMaximumSize(QSize(100, 16777215))
        self.vikup___ts.setCursor(QCursor(Qt.PointingHandCursor))
        self.vikup___ts.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.vikup___ts)

        self.driving_license = QCheckBox(self.centralwidget)
        self.driving_license.setObjectName(u"driving_license")
        self.driving_license.setMinimumSize(QSize(0, 26))
        self.driving_license.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.driving_license)

        self.dolg = QCheckBox(self.centralwidget)
        self.dolg.setObjectName(u"dolg")
        self.dolg.setMinimumSize(QSize(0, 26))
        self.dolg.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.dolg)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.layoutFiltersContracts.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.layoutFiltersContracts)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, 28, 10)
        self.btn_clear_filter = QPushButton(self.centralwidget)
        self.btn_clear_filter.setObjectName(u"btn_clear_filter")
        self.btn_clear_filter.setMinimumSize(QSize(400, 40))
        self.btn_clear_filter.setMaximumSize(QSize(16777215, 40))
        self.btn_clear_filter.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_clear_filter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 15, 28, -1)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(70, 36))
        self.label_11.setMaximumSize(QSize(70, 16777215))
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(250, 36))
        self.label_6.setMaximumSize(QSize(250, 16777215))
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(200, 36))
        self.label_7.setMaximumSize(QSize(200, 16777215))
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(100, 36))
        self.label_8.setMaximumSize(QSize(100, 16777215))
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(100, 36))
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setStyleSheet(u"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(36, 0))
        self.label_5.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(330, 36))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(36, 0))
        self.label_9.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1257, 554))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.listArendatorLayout = QVBoxLayout()
        self.listArendatorLayout.setSpacing(5)
        self.listArendatorLayout.setObjectName(u"listArendatorLayout")
        self.listArendatorLayout.setContentsMargins(-1, -1, 0, 0)

        self.verticalLayout_4.addLayout(self.listArendatorLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 3000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        ListArendatorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ListArendatorWindow)
        self.statusbar.setObjectName(u"statusbar")
        ListArendatorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListArendatorWindow)

        self.btn_add_client.setDefault(False)
        self.btn_clear_filter.setDefault(True)


        QMetaObject.connectSlotsByName(ListArendatorWindow)
    # setupUi

    def retranslateUi(self, ListArendatorWindow):
        ListArendatorWindow.setWindowTitle(QCoreApplication.translate("ListArendatorWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.btn_add_client.setText(QCoreApplication.translate("ListArendatorWindow", u"   \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.label_12.setText(QCoreApplication.translate("ListArendatorWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418.\u041e.", None))
        self.label_2.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_16.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label_15.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.label_14.setText("")
        self.grb_status.setTitle("")
        self.status_contract___all.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0412\u0441\u0435", None))
        self.status_contract__open.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435", None))
        self.status_contract__close.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044b\u0435", None))
        self.grb_date_pay.setTitle("")
        self.estimated_date___all.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0412\u0441\u0435", None))
        self.estimated_date___today.setText(QCoreApplication.translate("ListArendatorWindow", u"\u041f\u043b\u0430\u0442\u0435\u0436 \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.estimated_date___tomorrow.setText(QCoreApplication.translate("ListArendatorWindow", u"\u041f\u043b\u0430\u0442\u0435\u0436 \u0437\u0430\u0432\u0442\u0440\u0430", None))
        self.vikup___ts.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0421 \u0432\u044b\u043a\u0443\u043f\u043e\u043c", None))
        self.driving_license.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0435 \u0443\u0434\u043e\u0441\u0442\u043e\u0432\u0435\u0440\u0435\u043d\u0438\u0435", None))
        self.dolg.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0415\u0441\u0442\u044c \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.btn_clear_filter.setText(QCoreApplication.translate("ListArendatorWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.label_11.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.label_6.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e\n"
"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_7.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e", None))
        self.label_3.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0422\u0430\u0440\u0438\u0444", None))
        self.label_8.setText("")
        self.label_10.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("ListArendatorWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.label_9.setText("")
    # retranslateUi

