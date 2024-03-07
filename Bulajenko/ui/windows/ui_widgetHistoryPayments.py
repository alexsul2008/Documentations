# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetHistoryPaymentspbjFmC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_historyPayments_widget(object):
    def setupUi(self, historyPayments_widget):
        if not historyPayments_widget.objectName():
            historyPayments_widget.setObjectName(u"historyPayments_widget")
        historyPayments_widget.resize(1403, 37)
        self.verticalLayout_2 = QVBoxLayout(historyPayments_widget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_id_contract = QLineEdit(historyPayments_widget)
        self.le_id_contract.setObjectName(u"le_id_contract")
        self.le_id_contract.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_id_contract.sizePolicy().hasHeightForWidth())
        self.le_id_contract.setSizePolicy(sizePolicy)
        self.le_id_contract.setMinimumSize(QSize(50, 30))
        self.le_id_contract.setMaximumSize(QSize(50, 16777215))
        self.le_id_contract.setStyleSheet(u"padding-left: 10px;")

        self.horizontalLayout.addWidget(self.le_id_contract)

        self.le_date_payment = QLineEdit(historyPayments_widget)
        self.le_date_payment.setObjectName(u"le_date_payment")
        self.le_date_payment.setEnabled(False)
        sizePolicy.setHeightForWidth(self.le_date_payment.sizePolicy().hasHeightForWidth())
        self.le_date_payment.setSizePolicy(sizePolicy)
        self.le_date_payment.setMinimumSize(QSize(100, 30))
        self.le_date_payment.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.le_date_payment)

        self.le_total_pay = QLineEdit(historyPayments_widget)
        self.le_total_pay.setObjectName(u"le_total_pay")
        self.le_total_pay.setEnabled(False)
        sizePolicy.setHeightForWidth(self.le_total_pay.sizePolicy().hasHeightForWidth())
        self.le_total_pay.setSizePolicy(sizePolicy)
        self.le_total_pay.setMinimumSize(QSize(120, 30))
        self.le_total_pay.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.le_total_pay)

        self.le_size_payment = QLineEdit(historyPayments_widget)
        self.le_size_payment.setObjectName(u"le_size_payment")
        self.le_size_payment.setEnabled(False)
        sizePolicy.setHeightForWidth(self.le_size_payment.sizePolicy().hasHeightForWidth())
        self.le_size_payment.setSizePolicy(sizePolicy)
        self.le_size_payment.setMinimumSize(QSize(120, 30))
        self.le_size_payment.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.le_size_payment)

        self.le_comment_pay = QLineEdit(historyPayments_widget)
        self.le_comment_pay.setObjectName(u"le_comment_pay")
        self.le_comment_pay.setEnabled(False)
        self.le_comment_pay.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.le_comment_pay)

        self.le_tarif = QLineEdit(historyPayments_widget)
        self.le_tarif.setObjectName(u"le_tarif")
        self.le_tarif.setEnabled(False)
        sizePolicy.setHeightForWidth(self.le_tarif.sizePolicy().hasHeightForWidth())
        self.le_tarif.setSizePolicy(sizePolicy)
        self.le_tarif.setMinimumSize(QSize(100, 30))
        self.le_tarif.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.le_tarif)

        self.le_discount = QLineEdit(historyPayments_widget)
        self.le_discount.setObjectName(u"le_discount")
        self.le_discount.setEnabled(False)
        sizePolicy.setHeightForWidth(self.le_discount.sizePolicy().hasHeightForWidth())
        self.le_discount.setSizePolicy(sizePolicy)
        self.le_discount.setMinimumSize(QSize(100, 30))
        self.le_discount.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.le_discount)

        self.le_discount_comment = QLineEdit(historyPayments_widget)
        self.le_discount_comment.setObjectName(u"le_discount_comment")
        self.le_discount_comment.setEnabled(False)
        self.le_discount_comment.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.le_discount_comment)

        self.le_shtraf = QLineEdit(historyPayments_widget)
        self.le_shtraf.setObjectName(u"le_shtraf")
        self.le_shtraf.setEnabled(False)
        sizePolicy.setHeightForWidth(self.le_shtraf.sizePolicy().hasHeightForWidth())
        self.le_shtraf.setSizePolicy(sizePolicy)
        self.le_shtraf.setMinimumSize(QSize(100, 30))
        self.le_shtraf.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.le_shtraf)

        self.le_shtraf_comment = QLineEdit(historyPayments_widget)
        self.le_shtraf_comment.setObjectName(u"le_shtraf_comment")
        self.le_shtraf_comment.setEnabled(False)
        self.le_shtraf_comment.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.le_shtraf_comment)

        self.le_payments = QLineEdit(historyPayments_widget)
        self.le_payments.setObjectName(u"le_payments")
        self.le_payments.setEnabled(False)
        sizePolicy.setHeightForWidth(self.le_payments.sizePolicy().hasHeightForWidth())
        self.le_payments.setSizePolicy(sizePolicy)
        self.le_payments.setMinimumSize(QSize(150, 30))
        self.le_payments.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.le_payments)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(historyPayments_widget)

        QMetaObject.connectSlotsByName(historyPayments_widget)
    # setupUi

    def retranslateUi(self, historyPayments_widget):
        historyPayments_widget.setWindowTitle(QCoreApplication.translate("historyPayments_widget", u"Form", None))
        self.le_payments.setText("")
    # retranslateUi

