# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetItemListArendatorNRWpIE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_WidgetItemListArendator(object):
    def setupUi(self, WidgetItemListArendator):
        if not WidgetItemListArendator.objectName():
            WidgetItemListArendator.setObjectName(u"WidgetItemListArendator")
        WidgetItemListArendator.resize(1256, 57)
        WidgetItemListArendator.setMinimumSize(QSize(1256, 0))
        WidgetItemListArendator.setMaximumSize(QSize(1256, 16777215))
        WidgetItemListArendator.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(WidgetItemListArendator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 3)
        self.frameItemListArendator = QFrame(WidgetItemListArendator)
        self.frameItemListArendator.setObjectName(u"frameItemListArendator")
        self.frameItemListArendator.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.frameItemListArendator)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.lbl_dogovor = QLabel(self.frameItemListArendator)
        self.lbl_dogovor.setObjectName(u"lbl_dogovor")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dogovor.sizePolicy().hasHeightForWidth())
        self.lbl_dogovor.setSizePolicy(sizePolicy)
        self.lbl_dogovor.setMinimumSize(QSize(70, 0))
        self.lbl_dogovor.setMaximumSize(QSize(70, 16777215))
        self.lbl_dogovor.setStyleSheet(u"")
        self.lbl_dogovor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_dogovor)

        self.lbl_vikup = QLabel(self.frameItemListArendator)
        self.lbl_vikup.setObjectName(u"lbl_vikup")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_vikup.sizePolicy().hasHeightForWidth())
        self.lbl_vikup.setSizePolicy(sizePolicy1)
        self.lbl_vikup.setMinimumSize(QSize(70, 10))
        self.lbl_vikup.setMaximumSize(QSize(70, 16777215))
        self.lbl_vikup.setStyleSheet(u"")
        self.lbl_vikup.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_vikup)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.fio_phone_layout = QVBoxLayout()
        self.fio_phone_layout.setSpacing(5)
        self.fio_phone_layout.setObjectName(u"fio_phone_layout")
        self.fio_phone_layout.setContentsMargins(-1, -1, 0, -1)
        self.lbl_fio_arendator = QLabel(self.frameItemListArendator)
        self.lbl_fio_arendator.setObjectName(u"lbl_fio_arendator")
        self.lbl_fio_arendator.setMinimumSize(QSize(250, 0))
        self.lbl_fio_arendator.setMaximumSize(QSize(250, 16777215))

        self.fio_phone_layout.addWidget(self.lbl_fio_arendator)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frameItemListArendator)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 0))
        self.label_2.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lbl_phone = QLabel(self.frameItemListArendator)
        self.lbl_phone.setObjectName(u"lbl_phone")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_phone.sizePolicy().hasHeightForWidth())
        self.lbl_phone.setSizePolicy(sizePolicy2)
        self.lbl_phone.setMinimumSize(QSize(0, 15))
        self.lbl_phone.setMaximumSize(QSize(16777215, 15))
        self.lbl_phone.setStyleSheet(u"")
        self.lbl_phone.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_phone)


        self.fio_phone_layout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.fio_phone_layout)

        self.grb_ts = QFrame(self.frameItemListArendator)
        self.grb_ts.setObjectName(u"grb_ts")
        self.grb_ts.setMinimumSize(QSize(200, 0))
        self.grb_ts.setMaximumSize(QSize(200, 16777215))
        self.grb_ts.setCursor(QCursor(Qt.PointingHandCursor))
        self.grb_ts.setStyleSheet(u"#lbl_transport_model:hover QFrame:hover{color: rgb(235, 0, 0);}")
        self.verticalLayout_3 = QVBoxLayout(self.grb_ts)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_transport_model = QLabel(self.grb_ts)
        self.lbl_transport_model.setObjectName(u"lbl_transport_model")
        self.lbl_transport_model.setMinimumSize(QSize(200, 0))
        self.lbl_transport_model.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_3.addWidget(self.lbl_transport_model)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_color_ts = QLabel(self.grb_ts)
        self.lbl_color_ts.setObjectName(u"lbl_color_ts")
        self.lbl_color_ts.setMinimumSize(QSize(20, 20))
        self.lbl_color_ts.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.lbl_color_ts)

        self.lbl_transport_vin = QLabel(self.grb_ts)
        self.lbl_transport_vin.setObjectName(u"lbl_transport_vin")
        self.lbl_transport_vin.setMinimumSize(QSize(175, 20))
        self.lbl_transport_vin.setMaximumSize(QSize(175, 20))

        self.horizontalLayout_4.addWidget(self.lbl_transport_vin)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.grb_ts)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 7, 0, 7)
        self.lbl_size_pay = QLabel(self.frameItemListArendator)
        self.lbl_size_pay.setObjectName(u"lbl_size_pay")
        self.lbl_size_pay.setMinimumSize(QSize(100, 0))
        self.lbl_size_pay.setMaximumSize(QSize(100, 16777215))
        self.lbl_size_pay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_size_pay)

        self.lbl_metod_pay = QLabel(self.frameItemListArendator)
        self.lbl_metod_pay.setObjectName(u"lbl_metod_pay")
        self.lbl_metod_pay.setMinimumSize(QSize(100, 0))
        self.lbl_metod_pay.setMaximumSize(QSize(100, 16777215))
        self.lbl_metod_pay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_metod_pay)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frameItemListArendator)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.lbl_next_pay = QLabel(self.frameItemListArendator)
        self.lbl_next_pay.setObjectName(u"lbl_next_pay")
        self.lbl_next_pay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_next_pay)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.lbl_date_closed_contract = QLabel(self.frameItemListArendator)
        self.lbl_date_closed_contract.setObjectName(u"lbl_date_closed_contract")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_date_closed_contract.sizePolicy().hasHeightForWidth())
        self.lbl_date_closed_contract.setSizePolicy(sizePolicy3)
        self.lbl_date_closed_contract.setMinimumSize(QSize(100, 0))
        self.lbl_date_closed_contract.setMaximumSize(QSize(100, 16777215))
        self.lbl_date_closed_contract.setStyleSheet(u"")
        self.lbl_date_closed_contract.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_date_closed_contract)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.btn_dogovor = QPushButton(self.frameItemListArendator)
        self.btn_dogovor.setObjectName(u"btn_dogovor")
        self.btn_dogovor.setMinimumSize(QSize(36, 36))
        self.btn_dogovor.setMaximumSize(QSize(36, 36))
        self.btn_dogovor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dogovor.setStyleSheet(u":hover{background-color: orange}")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/clipboard_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dogovor.setIcon(icon)
        self.btn_dogovor.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_dogovor)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.buttonsOption_layout = QHBoxLayout()
        self.buttonsOption_layout.setSpacing(0)
        self.buttonsOption_layout.setObjectName(u"buttonsOption_layout")

        self.horizontalLayout_2.addLayout(self.buttonsOption_layout)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.btn_close_contract = QPushButton(self.frameItemListArendator)
        self.btn_close_contract.setObjectName(u"btn_close_contract")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_close_contract.sizePolicy().hasHeightForWidth())
        self.btn_close_contract.setSizePolicy(sizePolicy4)
        self.btn_close_contract.setMinimumSize(QSize(36, 36))
        self.btn_close_contract.setMaximumSize(QSize(36, 36))
        self.btn_close_contract.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close_contract.setStyleSheet(u":hover{background-color: orange}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/unlock_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_contract.setIcon(icon1)
        self.btn_close_contract.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_close_contract)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.lbl_id_ts = QLabel(self.frameItemListArendator)
        self.lbl_id_ts.setObjectName(u"lbl_id_ts")
        self.lbl_id_ts.setMinimumSize(QSize(15, 20))
        self.lbl_id_ts.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lbl_id_ts)

        self.lbl_date_set_arenda = QLabel(self.frameItemListArendator)
        self.lbl_date_set_arenda.setObjectName(u"lbl_date_set_arenda")
        self.lbl_date_set_arenda.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lbl_date_set_arenda)

        self.lbl_id_arendator = QLabel(self.frameItemListArendator)
        self.lbl_id_arendator.setObjectName(u"lbl_id_arendator")
        self.lbl_id_arendator.setMinimumSize(QSize(0, 0))
        self.lbl_id_arendator.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lbl_id_arendator)

        self.lbl_id_ts.raise_()
        self.lbl_id_arendator.raise_()
        self.grb_ts.raise_()
        self.btn_dogovor.raise_()
        self.lbl_date_set_arenda.raise_()

        self.verticalLayout.addWidget(self.frameItemListArendator)


        self.retranslateUi(WidgetItemListArendator)

        QMetaObject.connectSlotsByName(WidgetItemListArendator)
    # setupUi

    def retranslateUi(self, WidgetItemListArendator):
        WidgetItemListArendator.setWindowTitle(QCoreApplication.translate("WidgetItemListArendator", u"Form", None))
        self.lbl_dogovor.setText("")
        self.lbl_vikup.setText("")
        self.lbl_fio_arendator.setText(QCoreApplication.translate("WidgetItemListArendator", u"\u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u044c\u0441\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("WidgetItemListArendator", u"\u0442\u043b\u0444.", None))
        self.lbl_phone.setText(QCoreApplication.translate("WidgetItemListArendator", u"+7(999)-999-99-99", None))
        self.lbl_transport_model.setText(QCoreApplication.translate("WidgetItemListArendator", u"Yamaha Vino", None))
        self.lbl_color_ts.setText("")
        self.lbl_transport_vin.setText(QCoreApplication.translate("WidgetItemListArendator", u"AAAA100AAAA99999999", None))
        self.lbl_size_pay.setText("")
        self.lbl_metod_pay.setText("")
        self.label_3.setText(QCoreApplication.translate("WidgetItemListArendator", u"\u0414\u0430\u0442\u0430 \u0441\u043b\u0435\u0434.\n"
"\u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.lbl_next_pay.setText("")
        self.lbl_date_closed_contract.setText("")
#if QT_CONFIG(tooltip)
        self.btn_dogovor.setToolTip(QCoreApplication.translate("WidgetItemListArendator", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
#endif // QT_CONFIG(tooltip)
        self.btn_dogovor.setText("")
        self.btn_close_contract.setText("")
        self.lbl_id_ts.setText("")
        self.lbl_date_set_arenda.setText("")
        self.lbl_id_arendator.setText("")
    # retranslateUi

