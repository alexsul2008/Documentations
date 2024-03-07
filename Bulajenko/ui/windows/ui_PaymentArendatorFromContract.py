# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PaymentArendatorFromContractXBXagz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_paymentArendatorFromContract(object):
    def setupUi(self, paymentArendatorFromContract):
        if not paymentArendatorFromContract.objectName():
            paymentArendatorFromContract.setObjectName(u"paymentArendatorFromContract")
        paymentArendatorFromContract.setWindowModality(Qt.NonModal)
        paymentArendatorFromContract.resize(600, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(paymentArendatorFromContract.sizePolicy().hasHeightForWidth())
        paymentArendatorFromContract.setSizePolicy(sizePolicy)
        paymentArendatorFromContract.setMinimumSize(QSize(600, 0))
        paymentArendatorFromContract.setMaximumSize(QSize(600, 350))
        self.centralwidget = QWidget(paymentArendatorFromContract)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 36))
        self.label.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.lbl_fio_arendator = QLineEdit(self.centralwidget)
        self.lbl_fio_arendator.setObjectName(u"lbl_fio_arendator")
        self.lbl_fio_arendator.setEnabled(False)
        self.lbl_fio_arendator.setMinimumSize(QSize(0, 36))
        self.lbl_fio_arendator.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout.addWidget(self.lbl_fio_arendator)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(90, 30))
        self.label_7.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.label_7)

        self.date_payment = QDateTimeEdit(self.centralwidget)
        self.date_payment.setObjectName(u"date_payment")
        self.date_payment.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.date_payment.sizePolicy().hasHeightForWidth())
        self.date_payment.setSizePolicy(sizePolicy2)
        self.date_payment.setMinimumSize(QSize(120, 30))
        self.date_payment.setMaximumSize(QSize(120, 16777215))
        self.date_payment.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_payment.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.date_payment)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(45, 30))
        self.label_2.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 30))
        self.label_4.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.le_payment_tarif = QLineEdit(self.centralwidget)
        self.le_payment_tarif.setObjectName(u"le_payment_tarif")
        self.le_payment_tarif.setEnabled(False)
        self.le_payment_tarif.setMinimumSize(QSize(0, 30))
        self.le_payment_tarif.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.le_payment_tarif)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(90, 30))
        self.label_5.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.discount = QLineEdit(self.centralwidget)
        self.discount.setObjectName(u"discount")
        self.discount.setMinimumSize(QSize(120, 30))
        self.discount.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.discount)

        self.discount_comment = QLineEdit(self.centralwidget)
        self.discount_comment.setObjectName(u"discount_comment")
        self.discount_comment.setMinimumSize(QSize(0, 30))
        self.discount_comment.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.discount_comment)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(90, 30))
        self.label_6.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.shtraf = QLineEdit(self.centralwidget)
        self.shtraf.setObjectName(u"shtraf")
        self.shtraf.setMinimumSize(QSize(120, 30))
        self.shtraf.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_6.addWidget(self.shtraf)

        self.shtraf_comment = QLineEdit(self.centralwidget)
        self.shtraf_comment.setObjectName(u"shtraf_comment")
        self.shtraf_comment.setMinimumSize(QSize(0, 30))
        self.shtraf_comment.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.shtraf_comment)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(90, 30))
        self.label_3.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.size_payment = QLineEdit(self.centralwidget)
        self.size_payment.setObjectName(u"size_payment")
        self.size_payment.setMinimumSize(QSize(120, 30))
        self.size_payment.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.size_payment)

        self.cb_payments = QComboBox(self.centralwidget)
        self.cb_payments.addItem("")
        self.cb_payments.addItem("")
        self.cb_payments.addItem("")
        self.cb_payments.setObjectName(u"cb_payments")
        self.cb_payments.setMinimumSize(QSize(120, 30))
        self.cb_payments.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.cb_payments)

        self.comment_pay = QLineEdit(self.centralwidget)
        self.comment_pay.setObjectName(u"comment_pay")
        self.comment_pay.setMinimumSize(QSize(0, 30))
        self.comment_pay.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.comment_pay)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 0))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_id_contract = QLabel(self.horizontalFrame)
        self.lbl_id_contract.setObjectName(u"lbl_id_contract")
        self.lbl_id_contract.setMinimumSize(QSize(0, 0))
        self.lbl_id_contract.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.lbl_id_contract)

        self.lbl_id_arendator = QLabel(self.horizontalFrame)
        self.lbl_id_arendator.setObjectName(u"lbl_id_arendator")
        self.lbl_id_arendator.setEnabled(False)
        self.lbl_id_arendator.setMinimumSize(QSize(0, 0))
        self.lbl_id_arendator.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.lbl_id_arendator)


        self.verticalLayout.addWidget(self.horizontalFrame, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 400, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 40))
        self.btn_save.setMaximumSize(QSize(16777215, 40))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))
        self.btn_cancel.setMaximumSize(QSize(16777215, 40))
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        paymentArendatorFromContract.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(paymentArendatorFromContract)
        self.statusBar.setObjectName(u"statusBar")
        paymentArendatorFromContract.setStatusBar(self.statusBar)

        self.retranslateUi(paymentArendatorFromContract)

        QMetaObject.connectSlotsByName(paymentArendatorFromContract)
    # setupUi

    def retranslateUi(self, paymentArendatorFromContract):
        paymentArendatorFromContract.setWindowTitle(QCoreApplication.translate("paymentArendatorFromContract", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u0424\u0418\u041e", None))
        self.label_7.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u0414\u0430\u0442\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.date_payment.setDisplayFormat(QCoreApplication.translate("paymentArendatorFromContract", u"dd.MM.yyyy", None))
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u0422\u0430\u0440\u0438\u0444", None))
        self.label_5.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))
        self.discount_comment.setPlaceholderText(QCoreApplication.translate("paymentArendatorFromContract", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.label_6.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u0428\u0442\u0440\u0430\u0444", None))
        self.shtraf_comment.setPlaceholderText(QCoreApplication.translate("paymentArendatorFromContract", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.label_3.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u041f\u043b\u0430\u0442\u0435\u0436", None))
        self.cb_payments.setItemText(0, QCoreApplication.translate("paymentArendatorFromContract", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0435\u0442", None))
        self.cb_payments.setItemText(1, QCoreApplication.translate("paymentArendatorFromContract", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434", None))
        self.cb_payments.setItemText(2, QCoreApplication.translate("paymentArendatorFromContract", u"\u042d\u043a\u0432\u0430\u0439\u0440\u0438\u043d\u0433", None))

        self.comment_pay.setPlaceholderText(QCoreApplication.translate("paymentArendatorFromContract", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.lbl_id_contract.setText("")
        self.lbl_id_arendator.setText("")
        self.btn_save.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043f\u043b\u0430\u0442\u0435\u0436", None))
        self.btn_cancel.setText(QCoreApplication.translate("paymentArendatorFromContract", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

