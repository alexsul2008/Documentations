# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetItemNewContractwZiMFm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_widgetItemNewContract(object):
    def setupUi(self, widgetItemNewContract):
        if not widgetItemNewContract.objectName():
            widgetItemNewContract.setObjectName(u"widgetItemNewContract")
        widgetItemNewContract.resize(846, 287)
        widgetItemNewContract.setMaximumSize(QSize(856, 16777215))
        self.verticalLayout = QVBoxLayout(widgetItemNewContract)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 15, 0, 15)
        self.groupBox_5 = QGroupBox(widgetItemNewContract)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(55, 26))
        self.label_18.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_13.addWidget(self.label_18)

        self.lbl_date_set_arenda = QLabel(self.groupBox_5)
        self.lbl_date_set_arenda.setObjectName(u"lbl_date_set_arenda")
        sizePolicy.setHeightForWidth(self.lbl_date_set_arenda.sizePolicy().hasHeightForWidth())
        self.lbl_date_set_arenda.setSizePolicy(sizePolicy)
        self.lbl_date_set_arenda.setMinimumSize(QSize(100, 30))
        self.lbl_date_set_arenda.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_13.addWidget(self.lbl_date_set_arenda)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(77, 0))
        self.label_19.setMaximumSize(QSize(77, 16777215))

        self.horizontalLayout_13.addWidget(self.label_19)

        self.le_rental_period = QLineEdit(self.groupBox_5)
        self.le_rental_period.setObjectName(u"le_rental_period")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_rental_period.sizePolicy().hasHeightForWidth())
        self.le_rental_period.setSizePolicy(sizePolicy1)
        self.le_rental_period.setMinimumSize(QSize(72, 30))
        self.le_rental_period.setMaximumSize(QSize(72, 30))
        self.le_rental_period.setMaxLength(10)

        self.horizontalLayout_13.addWidget(self.le_rental_period)

        self.cb_rental_period = QComboBox(self.groupBox_5)
        self.cb_rental_period.addItem("")
        self.cb_rental_period.addItem("")
        self.cb_rental_period.addItem("")
        self.cb_rental_period.setObjectName(u"cb_rental_period")
        sizePolicy1.setHeightForWidth(self.cb_rental_period.sizePolicy().hasHeightForWidth())
        self.cb_rental_period.setSizePolicy(sizePolicy1)
        self.cb_rental_period.setMinimumSize(QSize(100, 30))
        self.cb_rental_period.setMaximumSize(QSize(100, 30))
        self.cb_rental_period.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.cb_rental_period)

        self.lbl_msg_period = QLabel(self.groupBox_5)
        self.lbl_msg_period.setObjectName(u"lbl_msg_period")

        self.horizontalLayout_13.addWidget(self.lbl_msg_period)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lbl_id_dogovor = QLabel(self.groupBox_5)
        self.lbl_id_dogovor.setObjectName(u"lbl_id_dogovor")
        self.lbl_id_dogovor.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.lbl_id_dogovor)


        self.horizontalLayout_13.addLayout(self.horizontalLayout)

        self.btn_cancel_new_contract = QPushButton(self.groupBox_5)
        self.btn_cancel_new_contract.setObjectName(u"btn_cancel_new_contract")
        self.btn_cancel_new_contract.setMinimumSize(QSize(0, 30))
        self.btn_cancel_new_contract.setMaximumSize(QSize(16777215, 30))
        self.btn_cancel_new_contract.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.btn_cancel_new_contract)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.layoutSelectTS = QHBoxLayout()
        self.layoutSelectTS.setSpacing(5)
        self.layoutSelectTS.setObjectName(u"layoutSelectTS")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(155, 30))
        self.label_17.setMaximumSize(QSize(155, 30))

        self.layoutSelectTS.addWidget(self.label_17)

        self.cb_type_ts = QComboBox(self.groupBox_5)
        self.cb_type_ts.setObjectName(u"cb_type_ts")
        sizePolicy1.setHeightForWidth(self.cb_type_ts.sizePolicy().hasHeightForWidth())
        self.cb_type_ts.setSizePolicy(sizePolicy1)
        self.cb_type_ts.setMinimumSize(QSize(157, 30))
        self.cb_type_ts.setMaximumSize(QSize(157, 30))
        self.cb_type_ts.setCursor(QCursor(Qt.PointingHandCursor))

        self.layoutSelectTS.addWidget(self.cb_type_ts)

        self.cb_brand_ts = QComboBox(self.groupBox_5)
        self.cb_brand_ts.setObjectName(u"cb_brand_ts")
        sizePolicy1.setHeightForWidth(self.cb_brand_ts.sizePolicy().hasHeightForWidth())
        self.cb_brand_ts.setSizePolicy(sizePolicy1)
        self.cb_brand_ts.setMinimumSize(QSize(160, 30))
        self.cb_brand_ts.setMaximumSize(QSize(160, 16777215))
        self.cb_brand_ts.setCursor(QCursor(Qt.PointingHandCursor))

        self.layoutSelectTS.addWidget(self.cb_brand_ts)

        self.cb_vin = QComboBox(self.groupBox_5)
        self.cb_vin.setObjectName(u"cb_vin")
        sizePolicy1.setHeightForWidth(self.cb_vin.sizePolicy().hasHeightForWidth())
        self.cb_vin.setSizePolicy(sizePolicy1)
        self.cb_vin.setMinimumSize(QSize(160, 30))
        self.cb_vin.setMaximumSize(QSize(160, 30))
        self.cb_vin.setCursor(QCursor(Qt.PointingHandCursor))

        self.layoutSelectTS.addWidget(self.cb_vin)

        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(35, 0))
        self.label.setMaximumSize(QSize(35, 16777215))

        self.layoutSelectTS.addWidget(self.label)

        self.chb_vikup = QCheckBox(self.groupBox_5)
        self.chb_vikup.setObjectName(u"chb_vikup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chb_vikup.sizePolicy().hasHeightForWidth())
        self.chb_vikup.setSizePolicy(sizePolicy2)
        self.chb_vikup.setMinimumSize(QSize(75, 30))
        self.chb_vikup.setMaximumSize(QSize(16777215, 30))
        self.chb_vikup.setCursor(QCursor(Qt.PointingHandCursor))

        self.layoutSelectTS.addWidget(self.chb_vikup)


        self.verticalLayout_7.addLayout(self.layoutSelectTS)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(155, 30))
        self.label_20.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_14.addWidget(self.label_20)

        self.cb_method_pay = QComboBox(self.groupBox_5)
        self.cb_method_pay.addItem("")
        self.cb_method_pay.addItem("")
        self.cb_method_pay.addItem("")
        self.cb_method_pay.setObjectName(u"cb_method_pay")
        sizePolicy1.setHeightForWidth(self.cb_method_pay.sizePolicy().hasHeightForWidth())
        self.cb_method_pay.setSizePolicy(sizePolicy1)
        self.cb_method_pay.setMinimumSize(QSize(157, 30))
        self.cb_method_pay.setMaximumSize(QSize(157, 30))
        self.cb_method_pay.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.cb_method_pay)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setMinimumSize(QSize(160, 0))
        self.label_21.setMaximumSize(QSize(160, 30))
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.le_size_pay = QLineEdit(self.groupBox_5)
        self.le_size_pay.setObjectName(u"le_size_pay")
        sizePolicy1.setHeightForWidth(self.le_size_pay.sizePolicy().hasHeightForWidth())
        self.le_size_pay.setSizePolicy(sizePolicy1)
        self.le_size_pay.setMinimumSize(QSize(160, 30))
        self.le_size_pay.setMaximumSize(QSize(160, 30))

        self.horizontalLayout_14.addWidget(self.le_size_pay)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(35, 0))
        self.label_24.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_14.addWidget(self.label_24)

        self.lbl_period_pay = QLabel(self.groupBox_5)
        self.lbl_period_pay.setObjectName(u"lbl_period_pay")

        self.horizontalLayout_14.addWidget(self.lbl_period_pay)

        self.lbl_msg_size = QLabel(self.groupBox_5)
        self.lbl_msg_size.setObjectName(u"lbl_msg_size")

        self.horizontalLayout_14.addWidget(self.lbl_msg_size)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.equipments_layout = QVBoxLayout()
        self.equipments_layout.setSpacing(0)
        self.equipments_layout.setObjectName(u"equipments_layout")
        self.equipments_layout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(50, 0))
        self.label_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_16.addWidget(self.label_15)

        self.chb_lock = QCheckBox(self.groupBox_5)
        self.chb_lock.setObjectName(u"chb_lock")
        self.chb_lock.setMinimumSize(QSize(70, 30))
        self.chb_lock.setMaximumSize(QSize(70, 30))
        self.chb_lock.setCursor(QCursor(Qt.PointingHandCursor))
        self.chb_lock.setLayoutDirection(Qt.LeftToRight)
        self.chb_lock.setTristate(False)

        self.horizontalLayout_16.addWidget(self.chb_lock)

        self.chb_shlem = QCheckBox(self.groupBox_5)
        self.chb_shlem.setObjectName(u"chb_shlem")
        self.chb_shlem.setMinimumSize(QSize(70, 30))
        self.chb_shlem.setMaximumSize(QSize(70, 30))
        self.chb_shlem.setCursor(QCursor(Qt.PointingHandCursor))
        self.chb_shlem.setLayoutDirection(Qt.LeftToRight)
        self.chb_shlem.setAutoFillBackground(False)

        self.horizontalLayout_16.addWidget(self.chb_shlem)

        self.chb_termocorob = QCheckBox(self.groupBox_5)
        self.chb_termocorob.setObjectName(u"chb_termocorob")
        self.chb_termocorob.setMinimumSize(QSize(100, 30))
        self.chb_termocorob.setMaximumSize(QSize(100, 30))
        self.chb_termocorob.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.chb_termocorob)

        self.chb_chehol = QCheckBox(self.groupBox_5)
        self.chb_chehol.setObjectName(u"chb_chehol")
        self.chb_chehol.setMinimumSize(QSize(150, 30))
        self.chb_chehol.setMaximumSize(QSize(150, 30))
        self.chb_chehol.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.chb_chehol)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)


        self.equipments_layout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 20))
        self.label_25.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.label_25)

        self.le_equipment = QLineEdit(self.groupBox_5)
        self.le_equipment.setObjectName(u"le_equipment")
        self.le_equipment.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_17.addWidget(self.le_equipment)


        self.equipments_layout.addLayout(self.horizontalLayout_17)


        self.gridLayout.addLayout(self.equipments_layout, 0, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(155, 26))

        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(widgetItemNewContract)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 10, 0, 0)
        self.cb_dkp = QComboBox(self.groupBox_4)
        self.cb_dkp.addItem("")
        self.cb_dkp.addItem("")
        self.cb_dkp.addItem("")
        self.cb_dkp.addItem("")
        self.cb_dkp.setObjectName(u"cb_dkp")
        self.cb_dkp.setMinimumSize(QSize(0, 28))
        self.cb_dkp.setMaximumSize(QSize(100, 28))
        self.cb_dkp.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.cb_dkp)

        self.btn_dkp = QPushButton(self.groupBox_4)
        self.btn_dkp.setObjectName(u"btn_dkp")
        self.btn_dkp.setMinimumSize(QSize(150, 30))
        self.btn_dkp.setMaximumSize(QSize(16777215, 30))
        self.btn_dkp.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_dkp)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.lbl_id_ts = QLabel(self.groupBox_4)
        self.lbl_id_ts.setObjectName(u"lbl_id_ts")

        self.horizontalLayout_11.addWidget(self.lbl_id_ts)

        self.lbl_model_ts = QLabel(self.groupBox_4)
        self.lbl_model_ts.setObjectName(u"lbl_model_ts")
        self.lbl_model_ts.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.lbl_model_ts)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.btn_create_dogovor = QPushButton(self.groupBox_4)
        self.btn_create_dogovor.setObjectName(u"btn_create_dogovor")
        self.btn_create_dogovor.setMinimumSize(QSize(150, 40))
        self.btn_create_dogovor.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_create_dogovor)

        self.btn_confirm_pay = QPushButton(self.groupBox_4)
        self.btn_confirm_pay.setObjectName(u"btn_confirm_pay")
        self.btn_confirm_pay.setMinimumSize(QSize(150, 40))
        self.btn_confirm_pay.setMaximumSize(QSize(16777215, 16777215))
        self.btn_confirm_pay.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_confirm_pay)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.retranslateUi(widgetItemNewContract)

        QMetaObject.connectSlotsByName(widgetItemNewContract)
    # setupUi

    def retranslateUi(self, widgetItemNewContract):
        widgetItemNewContract.setWindowTitle(QCoreApplication.translate("widgetItemNewContract", u"Form", None))
        self.groupBox_5.setTitle("")
        self.label_18.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0414\u0430\u0442\u0430", None))
        self.lbl_date_set_arenda.setText("")
        self.label_19.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0421\u0440\u043e\u043a \u0430\u0440\u0435\u043d\u0434\u044b", None))
        self.cb_rental_period.setItemText(0, QCoreApplication.translate("widgetItemNewContract", u"\u0434\u0435\u043d\u044c", None))
        self.cb_rental_period.setItemText(1, QCoreApplication.translate("widgetItemNewContract", u"\u043c\u0435\u0441\u044f\u0446", None))
        self.cb_rental_period.setItemText(2, QCoreApplication.translate("widgetItemNewContract", u"\u0433\u043e\u0434", None))

        self.lbl_msg_period.setText("")
        self.label_2.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u2116", None))
        self.lbl_id_dogovor.setText("")
        self.btn_cancel_new_contract.setText(QCoreApplication.translate("widgetItemNewContract", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_17.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e", None))
        self.label.setText("")
        self.chb_vikup.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0441 \u0432\u044b\u043a\u0443\u043f\u043e\u043c", None))
        self.label_20.setText(QCoreApplication.translate("widgetItemNewContract", u"\u041f\u0435\u0440\u0438\u043e\u0434\u0438\u0447\u043d\u043e\u0441\u0442\u044c \u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439", None))
        self.cb_method_pay.setItemText(0, QCoreApplication.translate("widgetItemNewContract", u"\u0415\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e", None))
        self.cb_method_pay.setItemText(1, QCoreApplication.translate("widgetItemNewContract", u"\u0415\u0436\u0435\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u043e", None))
        self.cb_method_pay.setItemText(2, QCoreApplication.translate("widgetItemNewContract", u"\u0415\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u043e", None))

        self.label_21.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0430\u0440\u0435\u043d\u0434\u043d\u043e\u0439 \u043f\u043b\u0430\u0442\u044b", None))
        self.label_24.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0440\u0443\u0431./", None))
        self.lbl_period_pay.setText("")
        self.lbl_msg_size.setText("")
        self.label_15.setText("")
        self.chb_lock.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0437\u0430\u043c\u043e\u043a", None))
        self.chb_shlem.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0448\u043b\u0435\u043c       ", None))
        self.chb_termocorob.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0442\u0435\u0440\u043c\u043e\u043a\u043e\u0440\u043e\u0431", None))
        self.chb_chehol.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0447\u0435\u0445\u043e\u043b \u0434\u043b\u044f \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.label_25.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0434\u0440\u0443\u0433\u043e\u0435", None))
        self.label_22.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0414\u043e\u043f. \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.groupBox_4.setTitle("")
        self.cb_dkp.setItemText(0, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 1", None))
        self.cb_dkp.setItemText(1, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 2", None))
        self.cb_dkp.setItemText(2, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 3", None))
        self.cb_dkp.setItemText(3, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 4", None))

        self.btn_dkp.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0414\u041a\u041f", None))
        self.lbl_id_ts.setText("")
        self.lbl_model_ts.setText("")
        self.btn_create_dogovor.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.btn_confirm_pay.setText(QCoreApplication.translate("widgetItemNewContract", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043e\u043f\u043b\u0430\u0442\u0443", None))
    # retranslateUi

