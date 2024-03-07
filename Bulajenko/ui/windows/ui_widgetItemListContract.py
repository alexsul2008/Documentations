# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetItemListContractNshxaK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_widgetItemNewContract(object):
    def setupUi(self, widgetItemNewContract):
        if not widgetItemNewContract.objectName():
            widgetItemNewContract.setObjectName(u"widgetItemNewContract")
        widgetItemNewContract.resize(846, 262)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetItemNewContract.sizePolicy().hasHeightForWidth())
        widgetItemNewContract.setSizePolicy(sizePolicy)
        widgetItemNewContract.setMaximumSize(QSize(856, 16777215))
        self.verticalLayout = QVBoxLayout(widgetItemNewContract)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.groupBox_base = QGroupBox(widgetItemNewContract)
        self.groupBox_base.setObjectName(u"groupBox_base")
        self.groupBox_base.setMinimumSize(QSize(0, 45))
        self.groupBox_base.setMaximumSize(QSize(16777215, 45))
        self.groupBox_base.setStyleSheet(u"")
        self.groupBox_base.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout = QHBoxLayout(self.groupBox_base)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.label_16 = QLabel(self.groupBox_base)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(80, 0))
        self.label_16.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)

        self.verticalLayout_4.addWidget(self.label_16)

        self.lbl_vikup = QLabel(self.groupBox_base)
        self.lbl_vikup.setObjectName(u"lbl_vikup")
        self.lbl_vikup.setMinimumSize(QSize(80, 0))
        self.lbl_vikup.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(6)
        self.lbl_vikup.setFont(font1)
        self.lbl_vikup.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_vikup)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.le_contract_id = QLineEdit(self.groupBox_base)
        self.le_contract_id.setObjectName(u"le_contract_id")
        self.le_contract_id.setEnabled(False)
        self.le_contract_id.setMinimumSize(QSize(80, 30))
        self.le_contract_id.setMaximumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.le_contract_id, 0, Qt.AlignTop)

        self.label = QLabel(self.groupBox_base)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(20, 30))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.lbl_date_set_arenda = QLabel(self.groupBox_base)
        self.lbl_date_set_arenda.setObjectName(u"lbl_date_set_arenda")
        self.lbl_date_set_arenda.setMinimumSize(QSize(100, 30))
        self.lbl_date_set_arenda.setMaximumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.lbl_date_set_arenda, 0, Qt.AlignTop)

        self.label_19 = QLabel(self.groupBox_base)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(100, 30))
        self.label_19.setMaximumSize(QSize(90, 30))
        self.label_19.setFont(font)

        self.horizontalLayout.addWidget(self.label_19, 0, Qt.AlignTop)

        self.lbl_rental_period = QLabel(self.groupBox_base)
        self.lbl_rental_period.setObjectName(u"lbl_rental_period")
        self.lbl_rental_period.setMinimumSize(QSize(100, 30))
        self.lbl_rental_period.setMaximumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.lbl_rental_period, 0, Qt.AlignTop)

        self.label_2 = QLabel(self.groupBox_base)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 30))
        self.label_2.setMaximumSize(QSize(60, 30))
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignTop)

        self.lbl_status_contact = QLabel(self.groupBox_base)
        self.lbl_status_contact.setObjectName(u"lbl_status_contact")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_status_contact.sizePolicy().hasHeightForWidth())
        self.lbl_status_contact.setSizePolicy(sizePolicy1)
        self.lbl_status_contact.setMinimumSize(QSize(0, 30))
        self.lbl_status_contact.setMaximumSize(QSize(16777215, 30))
        self.lbl_status_contact.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_status_contact, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_delete = QPushButton(self.groupBox_base)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(0, 30))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setLayoutDirection(Qt.RightToLeft)
        self.btn_delete.setStyleSheet(u"padding-left: 10px;\n"
"padding-right: 10px;")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_delete)

        self.lbl_id_ts = QLabel(self.groupBox_base)
        self.lbl_id_ts.setObjectName(u"lbl_id_ts")
        self.lbl_id_ts.setMinimumSize(QSize(0, 30))
        self.lbl_id_ts.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.lbl_id_ts)

        self.btn_collaps = QPushButton(self.groupBox_base)
        self.btn_collaps.setObjectName(u"btn_collaps")
        self.btn_collaps.setMinimumSize(QSize(30, 30))
        self.btn_collaps.setMaximumSize(QSize(30, 30))
        self.btn_collaps.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_collaps.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_collaps)


        self.verticalLayout.addWidget(self.groupBox_base)

        self.groupBox_content = QGroupBox(widgetItemNewContract)
        self.groupBox_content.setObjectName(u"groupBox_content")
        self.groupBox_content.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_content)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.layoutSelectTS = QHBoxLayout()
        self.layoutSelectTS.setSpacing(5)
        self.layoutSelectTS.setObjectName(u"layoutSelectTS")
        self.label_17 = QLabel(self.groupBox_content)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(145, 26))
        self.label_17.setMaximumSize(QSize(145, 16777215))

        self.layoutSelectTS.addWidget(self.label_17)

        self.le_ts = QLineEdit(self.groupBox_content)
        self.le_ts.setObjectName(u"le_ts")
        self.le_ts.setEnabled(False)
        self.le_ts.setMinimumSize(QSize(0, 30))

        self.layoutSelectTS.addWidget(self.le_ts)


        self.verticalLayout_3.addLayout(self.layoutSelectTS)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_21 = QLabel(self.groupBox_content)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(145, 0))
        self.label_21.setMaximumSize(QSize(145, 16777215))
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.le_size_pay = QLineEdit(self.groupBox_content)
        self.le_size_pay.setObjectName(u"le_size_pay")
        self.le_size_pay.setEnabled(False)
        self.le_size_pay.setMinimumSize(QSize(80, 30))
        self.le_size_pay.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_14.addWidget(self.le_size_pay)

        self.label_24 = QLabel(self.groupBox_content)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_14.addWidget(self.label_24)

        self.lbl_method_pay = QLabel(self.groupBox_content)
        self.lbl_method_pay.setObjectName(u"lbl_method_pay")

        self.horizontalLayout_14.addWidget(self.lbl_method_pay)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.equipments_layout = QVBoxLayout()
        self.equipments_layout.setSpacing(0)
        self.equipments_layout.setObjectName(u"equipments_layout")
        self.equipments_layout.setContentsMargins(-1, -1, 0, -1)
        self.checkboxes_layout = QHBoxLayout()
        self.checkboxes_layout.setSpacing(5)
        self.checkboxes_layout.setObjectName(u"checkboxes_layout")
        self.checkboxes_layout.setContentsMargins(-1, -1, 0, -1)
        self.label_15 = QLabel(self.groupBox_content)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(50, 0))
        self.label_15.setMaximumSize(QSize(50, 16777215))

        self.checkboxes_layout.addWidget(self.label_15)

        self.chb_lock = QCheckBox(self.groupBox_content)
        self.chb_lock.setObjectName(u"chb_lock")
        self.chb_lock.setEnabled(False)
        self.chb_lock.setMinimumSize(QSize(70, 30))
        self.chb_lock.setMaximumSize(QSize(68, 16777215))
        self.chb_lock.setCursor(QCursor(Qt.PointingHandCursor))
        self.chb_lock.setLayoutDirection(Qt.LeftToRight)
        self.chb_lock.setTristate(False)

        self.checkboxes_layout.addWidget(self.chb_lock)

        self.chb_shlem = QCheckBox(self.groupBox_content)
        self.chb_shlem.setObjectName(u"chb_shlem")
        self.chb_shlem.setEnabled(False)
        self.chb_shlem.setMinimumSize(QSize(70, 30))
        self.chb_shlem.setMaximumSize(QSize(68, 16777215))
        self.chb_shlem.setCursor(QCursor(Qt.PointingHandCursor))
        self.chb_shlem.setLayoutDirection(Qt.LeftToRight)
        self.chb_shlem.setAutoFillBackground(False)

        self.checkboxes_layout.addWidget(self.chb_shlem)

        self.chb_termocorob = QCheckBox(self.groupBox_content)
        self.chb_termocorob.setObjectName(u"chb_termocorob")
        self.chb_termocorob.setEnabled(False)
        self.chb_termocorob.setMinimumSize(QSize(100, 30))
        self.chb_termocorob.setCursor(QCursor(Qt.PointingHandCursor))

        self.checkboxes_layout.addWidget(self.chb_termocorob)

        self.chb_chehol = QCheckBox(self.groupBox_content)
        self.chb_chehol.setObjectName(u"chb_chehol")
        self.chb_chehol.setEnabled(False)
        self.chb_chehol.setMinimumSize(QSize(150, 30))
        self.chb_chehol.setCursor(QCursor(Qt.PointingHandCursor))

        self.checkboxes_layout.addWidget(self.chb_chehol)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.checkboxes_layout.addItem(self.horizontalSpacer_7)


        self.equipments_layout.addLayout(self.checkboxes_layout)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.groupBox_content)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 20))
        self.label_25.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.label_25)

        self.le_equipment = QLineEdit(self.groupBox_content)
        self.le_equipment.setObjectName(u"le_equipment")
        self.le_equipment.setEnabled(False)
        self.le_equipment.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_17.addWidget(self.le_equipment)


        self.equipments_layout.addLayout(self.horizontalLayout_17)


        self.gridLayout.addLayout(self.equipments_layout, 0, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_content)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(145, 26))

        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.groupBox_actions = QGroupBox(self.groupBox_content)
        self.groupBox_actions.setObjectName(u"groupBox_actions")
        self.groupBox_actions.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_actions)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 5)
        self.cb_dkp = QComboBox(self.groupBox_actions)
        self.cb_dkp.addItem("")
        self.cb_dkp.addItem("")
        self.cb_dkp.addItem("")
        self.cb_dkp.addItem("")
        self.cb_dkp.setObjectName(u"cb_dkp")
        self.cb_dkp.setMinimumSize(QSize(0, 28))
        self.cb_dkp.setMaximumSize(QSize(100, 28))
        self.cb_dkp.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.cb_dkp)

        self.btn_dkp = QPushButton(self.groupBox_actions)
        self.btn_dkp.setObjectName(u"btn_dkp")
        self.btn_dkp.setMinimumSize(QSize(150, 30))
        self.btn_dkp.setMaximumSize(QSize(16777215, 30))
        self.btn_dkp.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_dkp)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.btn_confirm_pay = QPushButton(self.groupBox_actions)
        self.btn_confirm_pay.setObjectName(u"btn_confirm_pay")
        self.btn_confirm_pay.setMinimumSize(QSize(150, 40))
        self.btn_confirm_pay.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_confirm_pay)


        self.verticalLayout_3.addWidget(self.groupBox_actions)


        self.verticalLayout.addWidget(self.groupBox_content)


        self.retranslateUi(widgetItemNewContract)

        QMetaObject.connectSlotsByName(widgetItemNewContract)
    # setupUi

    def retranslateUi(self, widgetItemNewContract):
        widgetItemNewContract.setWindowTitle(QCoreApplication.translate("widgetItemNewContract", u"Form", None))
        self.groupBox_base.setTitle("")
        self.label_16.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u2116 ", None))
        self.lbl_vikup.setText("")
        self.label.setText(QCoreApplication.translate("widgetItemNewContract", u"\u043e\u0442", None))
        self.lbl_date_set_arenda.setText("")
        self.label_19.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0421\u0440\u043e\u043a \u0430\u0440\u0435\u043d\u0434\u044b", None))
        self.lbl_rental_period.setText("")
        self.label_2.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.lbl_status_contact.setText("")
        self.btn_delete.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.lbl_id_ts.setText("")
        self.btn_collaps.setText("")
        self.groupBox_content.setTitle("")
        self.label_17.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e:", None))
        self.label_21.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0430\u0440\u0435\u043d\u0434\u043d\u043e\u0439 \u043f\u043b\u0430\u0442\u044b:", None))
        self.label_24.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0440\u0443\u0431. /", None))
        self.lbl_method_pay.setText("")
        self.label_15.setText("")
        self.chb_lock.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0437\u0430\u043c\u043e\u043a", None))
        self.chb_shlem.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0448\u043b\u0435\u043c", None))
        self.chb_termocorob.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0442\u0435\u0440\u043c\u043e\u043a\u043e\u0440\u043e\u0431", None))
        self.chb_chehol.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0447\u0435\u0445\u043e\u043b \u0434\u043b\u044f \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.label_25.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0434\u0440\u0443\u0433\u043e\u0435", None))
        self.label_22.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0414\u043e\u043f. \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.groupBox_actions.setTitle("")
        self.cb_dkp.setItemText(0, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 1", None))
        self.cb_dkp.setItemText(1, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 2", None))
        self.cb_dkp.setItemText(2, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 3", None))
        self.cb_dkp.setItemText(3, QCoreApplication.translate("widgetItemNewContract", u"\u0414\u041a\u041f 4", None))

        self.btn_dkp.setText(QCoreApplication.translate("widgetItemNewContract", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0414\u041a\u041f", None))
        self.btn_confirm_pay.setText(QCoreApplication.translate("widgetItemNewContract", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043e\u043f\u043b\u0430\u0442\u0443", None))
    # retranslateUi

