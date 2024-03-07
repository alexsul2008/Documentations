# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetNewDatePaymentBBpXDj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SetNewDatePayment(object):
    def setupUi(self, SetNewDatePayment):
        if not SetNewDatePayment.objectName():
            SetNewDatePayment.setObjectName(u"SetNewDatePayment")
        SetNewDatePayment.resize(380, 175)
        SetNewDatePayment.setMinimumSize(QSize(380, 175))
        SetNewDatePayment.setMaximumSize(QSize(380, 175))
        self.centralwidget = QWidget(SetNewDatePayment)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 30, 10, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.de_new_date_payment = QDateEdit(self.centralwidget)
        self.de_new_date_payment.setObjectName(u"de_new_date_payment")
        self.de_new_date_payment.setMinimumSize(QSize(150, 30))
        self.de_new_date_payment.setCursor(QCursor(Qt.PointingHandCursor))
        self.de_new_date_payment.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.de_new_date_payment)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 40))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_save)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 40))
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        SetNewDatePayment.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SetNewDatePayment)
        self.statusbar.setObjectName(u"statusbar")
        SetNewDatePayment.setStatusBar(self.statusbar)

        self.retranslateUi(SetNewDatePayment)

        QMetaObject.connectSlotsByName(SetNewDatePayment)
    # setupUi

    def retranslateUi(self, SetNewDatePayment):
        SetNewDatePayment.setWindowTitle(QCoreApplication.translate("SetNewDatePayment", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("SetNewDatePayment", u"\u041d\u043e\u0432\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.btn_save.setText(QCoreApplication.translate("SetNewDatePayment", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText("")
        self.btn_cancel.setText(QCoreApplication.translate("SetNewDatePayment", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

