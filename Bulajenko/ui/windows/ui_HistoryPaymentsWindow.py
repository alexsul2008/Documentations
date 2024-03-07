# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HistoryPaymentsWindowIgyuug.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_HistoryPaymentsWindow(object):
    def setupUi(self, HistoryPaymentsWindow):
        if not HistoryPaymentsWindow.objectName():
            HistoryPaymentsWindow.setObjectName(u"HistoryPaymentsWindow")
        HistoryPaymentsWindow.resize(1395, 560)
        self.centralwidget = QWidget(HistoryPaymentsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.label)

        self.lbl_id_arendator = QLabel(self.centralwidget)
        self.lbl_id_arendator.setObjectName(u"lbl_id_arendator")
        self.lbl_id_arendator.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.lbl_id_arendator)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_id_contract = QLabel(self.centralwidget)
        self.lbl_id_contract.setObjectName(u"lbl_id_contract")
        self.lbl_id_contract.setMinimumSize(QSize(50, 30))
        self.lbl_id_contract.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.lbl_id_contract)

        self.lbl_date_payment = QLabel(self.centralwidget)
        self.lbl_date_payment.setObjectName(u"lbl_date_payment")
        self.lbl_date_payment.setMinimumSize(QSize(100, 0))
        self.lbl_date_payment.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lbl_date_payment)

        self.lbl_total_pay = QLabel(self.centralwidget)
        self.lbl_total_pay.setObjectName(u"lbl_total_pay")
        self.lbl_total_pay.setMinimumSize(QSize(120, 0))
        self.lbl_total_pay.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.lbl_total_pay)

        self.lbl_size_payment = QLabel(self.centralwidget)
        self.lbl_size_payment.setObjectName(u"lbl_size_payment")
        self.lbl_size_payment.setMinimumSize(QSize(120, 0))
        self.lbl_size_payment.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.lbl_size_payment)

        self.lbl_comment_pay = QLabel(self.centralwidget)
        self.lbl_comment_pay.setObjectName(u"lbl_comment_pay")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_comment_pay.sizePolicy().hasHeightForWidth())
        self.lbl_comment_pay.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_comment_pay)

        self.lbl_tarif = QLabel(self.centralwidget)
        self.lbl_tarif.setObjectName(u"lbl_tarif")
        self.lbl_tarif.setMinimumSize(QSize(100, 0))
        self.lbl_tarif.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lbl_tarif)

        self.lbl_discount = QLabel(self.centralwidget)
        self.lbl_discount.setObjectName(u"lbl_discount")
        self.lbl_discount.setMinimumSize(QSize(100, 0))
        self.lbl_discount.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lbl_discount)

        self.lbl_discount_comment = QLabel(self.centralwidget)
        self.lbl_discount_comment.setObjectName(u"lbl_discount_comment")
        sizePolicy.setHeightForWidth(self.lbl_discount_comment.sizePolicy().hasHeightForWidth())
        self.lbl_discount_comment.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_discount_comment)

        self.lbl_shtraf = QLabel(self.centralwidget)
        self.lbl_shtraf.setObjectName(u"lbl_shtraf")
        self.lbl_shtraf.setMinimumSize(QSize(100, 0))
        self.lbl_shtraf.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lbl_shtraf)

        self.lbl_shtraf_comment = QLabel(self.centralwidget)
        self.lbl_shtraf_comment.setObjectName(u"lbl_shtraf_comment")
        sizePolicy.setHeightForWidth(self.lbl_shtraf_comment.sizePolicy().hasHeightForWidth())
        self.lbl_shtraf_comment.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_shtraf_comment)

        self.lbl_payments = QLabel(self.centralwidget)
        self.lbl_payments.setObjectName(u"lbl_payments")
        self.lbl_payments.setMinimumSize(QSize(150, 0))
        self.lbl_payments.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.lbl_payments)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1377, 456))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layoutItemsHistoryPaymets = QVBoxLayout()
        self.layoutItemsHistoryPaymets.setSpacing(0)
        self.layoutItemsHistoryPaymets.setObjectName(u"layoutItemsHistoryPaymets")

        self.verticalLayout_2.addLayout(self.layoutItemsHistoryPaymets)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        HistoryPaymentsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(HistoryPaymentsWindow)
        self.statusbar.setObjectName(u"statusbar")
        HistoryPaymentsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HistoryPaymentsWindow)

        QMetaObject.connectSlotsByName(HistoryPaymentsWindow)
    # setupUi

    def retranslateUi(self, HistoryPaymentsWindow):
        HistoryPaymentsWindow.setWindowTitle(QCoreApplication.translate("HistoryPaymentsWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442:", None))
        self.lbl_id_arendator.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"10", None))
        self.lbl_id_contract.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.lbl_date_payment.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.lbl_total_pay.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.lbl_size_payment.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u0430", None))
        self.lbl_comment_pay.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.lbl_tarif.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u0422\u0430\u0440\u0438\u0444 \u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.lbl_discount.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))
        self.lbl_discount_comment.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0441\u043a\u0438\u0434\u043a\u0435", None))
        self.lbl_shtraf.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u0428\u0442\u0440\u0430\u0444", None))
        self.lbl_shtraf_comment.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0448\u0442\u0440\u0430\u0444\u0443", None))
        self.lbl_payments.setText(QCoreApplication.translate("HistoryPaymentsWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
    # retranslateUi

