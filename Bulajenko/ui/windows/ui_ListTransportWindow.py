# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListTransportWindowfNJtVE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ListTransportWindow(object):
    def setupUi(self, ListTransportWindow):
        if not ListTransportWindow.objectName():
            ListTransportWindow.setObjectName(u"ListTransportWindow")
        ListTransportWindow.resize(1250, 940)
        ListTransportWindow.setMinimumSize(QSize(1250, 0))
        ListTransportWindow.setMaximumSize(QSize(1250, 16777215))
        self.centralwidget = QWidget(ListTransportWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 30, 0, 20)
        self.layoutFiltersTransports_2 = QFrame(self.groupBox)
        self.layoutFiltersTransports_2.setObjectName(u"layoutFiltersTransports_2")
        self.layoutFiltersTransports = QHBoxLayout(self.layoutFiltersTransports_2)
        self.layoutFiltersTransports.setSpacing(15)
        self.layoutFiltersTransports.setObjectName(u"layoutFiltersTransports")
        self.layoutFiltersTransports.setContentsMargins(15, 0, 15, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(5)
        self.label = QLabel(self.layoutFiltersTransports_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 30))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.brand = QComboBox(self.layoutFiltersTransports_2)
        self.brand.setObjectName(u"brand")
        sizePolicy.setHeightForWidth(self.brand.sizePolicy().hasHeightForWidth())
        self.brand.setSizePolicy(sizePolicy)
        self.brand.setMinimumSize(QSize(215, 30))
        self.brand.setMaximumSize(QSize(16777215, 30))
        self.brand.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.brand)

        self.label_2 = QLabel(self.layoutFiltersTransports_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 26))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.model = QComboBox(self.layoutFiltersTransports_2)
        self.model.setObjectName(u"model")
        sizePolicy.setHeightForWidth(self.model.sizePolicy().hasHeightForWidth())
        self.model.setSizePolicy(sizePolicy)
        self.model.setMinimumSize(QSize(215, 30))
        self.model.setMaximumSize(QSize(16777215, 30))
        self.model.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.model)

        self.label_3 = QLabel(self.layoutFiltersTransports_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(100, 26))
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.bodywork = QComboBox(self.layoutFiltersTransports_2)
        self.bodywork.setObjectName(u"bodywork")
        sizePolicy.setHeightForWidth(self.bodywork.sizePolicy().hasHeightForWidth())
        self.bodywork.setSizePolicy(sizePolicy)
        self.bodywork.setMinimumSize(QSize(215, 30))
        self.bodywork.setMaximumSize(QSize(16777215, 30))
        self.bodywork.setCursor(QCursor(Qt.PointingHandCursor))
        self.bodywork.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.bodywork)


        self.layoutFiltersTransports.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(5)
        self.label_7 = QLabel(self.layoutFiltersTransports_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(100, 26))
        self.label_7.setMaximumSize(QSize(100, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.type_transport_id = QComboBox(self.layoutFiltersTransports_2)
        self.type_transport_id.setObjectName(u"type_transport_id")
        sizePolicy.setHeightForWidth(self.type_transport_id.sizePolicy().hasHeightForWidth())
        self.type_transport_id.setSizePolicy(sizePolicy)
        self.type_transport_id.setMinimumSize(QSize(215, 30))
        self.type_transport_id.setMaximumSize(QSize(16777215, 30))
        self.type_transport_id.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.type_transport_id)

        self.label_5 = QLabel(self.layoutFiltersTransports_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(100, 26))
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.status_transport_id = QComboBox(self.layoutFiltersTransports_2)
        self.status_transport_id.setObjectName(u"status_transport_id")
        sizePolicy.setHeightForWidth(self.status_transport_id.sizePolicy().hasHeightForWidth())
        self.status_transport_id.setSizePolicy(sizePolicy)
        self.status_transport_id.setMinimumSize(QSize(215, 30))
        self.status_transport_id.setMaximumSize(QSize(16777215, 30))
        self.status_transport_id.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.status_transport_id)

        self.label_11 = QLabel(self.layoutFiltersTransports_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(100, 26))
        self.label_11.setMaximumSize(QSize(100, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.coutry = QComboBox(self.layoutFiltersTransports_2)
        self.coutry.setObjectName(u"coutry")
        sizePolicy.setHeightForWidth(self.coutry.sizePolicy().hasHeightForWidth())
        self.coutry.setSizePolicy(sizePolicy)
        self.coutry.setMinimumSize(QSize(215, 30))
        self.coutry.setMaximumSize(QSize(16777215, 30))
        self.coutry.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.coutry)


        self.layoutFiltersTransports.addLayout(self.formLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.cb_sorting = QComboBox(self.layoutFiltersTransports_2)
        self.cb_sorting.setObjectName(u"cb_sorting")
        self.cb_sorting.setMinimumSize(QSize(215, 30))
        self.cb_sorting.setMaximumSize(QSize(16777215, 16777215))
        self.cb_sorting.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.cb_sorting, 2, 1, 1, 1)

        self.label_4 = QLabel(self.layoutFiltersTransports_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(100, 26))
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.market_price__min = QLineEdit(self.layoutFiltersTransports_2)
        self.market_price__min.setObjectName(u"market_price__min")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.market_price__min.sizePolicy().hasHeightForWidth())
        self.market_price__min.setSizePolicy(sizePolicy1)
        self.market_price__min.setMinimumSize(QSize(120, 30))
        self.market_price__min.setMaximumSize(QSize(92, 16777215))

        self.gridLayout_2.addWidget(self.market_price__min, 1, 1, 1, 1)

        self.label_10 = QLabel(self.layoutFiltersTransports_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 30))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_10, 1, 2, 1, 1)

        self.market_price__max = QLineEdit(self.layoutFiltersTransports_2)
        self.market_price__max.setObjectName(u"market_price__max")
        sizePolicy1.setHeightForWidth(self.market_price__max.sizePolicy().hasHeightForWidth())
        self.market_price__max.setSizePolicy(sizePolicy1)
        self.market_price__max.setMinimumSize(QSize(120, 30))
        self.market_price__max.setMaximumSize(QSize(92, 16777215))

        self.gridLayout_2.addWidget(self.market_price__max, 1, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.layoutFiltersTransports_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_8 = QLabel(self.layoutFiltersTransports_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 26))
        self.label_8.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.color_id = QComboBox(self.layoutFiltersTransports_2)
        self.color_id.setObjectName(u"color_id")
        sizePolicy.setHeightForWidth(self.color_id.sizePolicy().hasHeightForWidth())
        self.color_id.setSizePolicy(sizePolicy)
        self.color_id.setMinimumSize(QSize(215, 30))
        self.color_id.setMaximumSize(QSize(16777215, 16777215))
        self.color_id.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.color_id, 0, 1, 1, 1)


        self.layoutFiltersTransports.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.layoutFiltersTransports_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, 15, 0)
        self.btn_clear_filters = QPushButton(self.groupBox)
        self.btn_clear_filters.setObjectName(u"btn_clear_filters")
        sizePolicy1.setHeightForWidth(self.btn_clear_filters.sizePolicy().hasHeightForWidth())
        self.btn_clear_filters.setSizePolicy(sizePolicy1)
        self.btn_clear_filters.setMinimumSize(QSize(892, 40))
        self.btn_clear_filters.setMaximumSize(QSize(16777215, 16777215))
        self.btn_clear_filters.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_clear_filters)

        self.btn_add_ts = QPushButton(self.groupBox)
        self.btn_add_ts.setObjectName(u"btn_add_ts")
        self.btn_add_ts.setMinimumSize(QSize(290, 40))
        self.btn_add_ts.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_add_ts)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox, 0, Qt.AlignTop)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1230, 640))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.listTransportLayout = QVBoxLayout()
        self.listTransportLayout.setSpacing(5)
        self.listTransportLayout.setObjectName(u"listTransportLayout")

        self.verticalLayout_4.addLayout(self.listTransportLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 800, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        ListTransportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ListTransportWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 21))
        ListTransportWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ListTransportWindow)
        self.statusbar.setObjectName(u"statusbar")
        ListTransportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListTransportWindow)

        QMetaObject.connectSlotsByName(ListTransportWindow)
    # setupUi

    def retranslateUi(self, ListTransportWindow):
        ListTransportWindow.setWindowTitle(QCoreApplication.translate("ListTransportWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("ListTransportWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.label.setText(QCoreApplication.translate("ListTransportWindow", u"\u041c\u0430\u0440\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("ListTransportWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("ListTransportWindow", u"VIN", None))
        self.label_7.setText(QCoreApplication.translate("ListTransportWindow", u"\u0422\u0438\u043f \u0422\u0421", None))
        self.label_5.setText(QCoreApplication.translate("ListTransportWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_11.setText(QCoreApplication.translate("ListTransportWindow", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.label_4.setText(QCoreApplication.translate("ListTransportWindow", u"\u0426\u0432\u0435\u0442", None))
        self.label_10.setText(QCoreApplication.translate("ListTransportWindow", u"\u0434\u043e", None))
        self.label_6.setText(QCoreApplication.translate("ListTransportWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("ListTransportWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0442", None))
        self.btn_clear_filters.setText(QCoreApplication.translate("ListTransportWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.btn_add_ts.setText(QCoreApplication.translate("ListTransportWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0422\u0421", None))
    # retranslateUi

