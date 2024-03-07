# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BaseItemArendatorWidgetMnoGmF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_BaseItemArendatorWidget(object):
    def setupUi(self, BaseItemArendatorWidget):
        if not BaseItemArendatorWidget.objectName():
            BaseItemArendatorWidget.setObjectName(u"BaseItemArendatorWidget")
        BaseItemArendatorWidget.resize(1197, 46)
        BaseItemArendatorWidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(BaseItemArendatorWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 3, 5, 3)
        self.horizontalFrame = QFrame(BaseItemArendatorWidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_id_arendator = QLabel(self.horizontalFrame)
        self.lbl_id_arendator.setObjectName(u"lbl_id_arendator")
        self.lbl_id_arendator.setMinimumSize(QSize(60, 0))
        self.lbl_id_arendator.setMaximumSize(QSize(60, 16777215))
        self.lbl_id_arendator.setStyleSheet(u"padding-left: 10px;")

        self.horizontalLayout.addWidget(self.lbl_id_arendator)

        self.lbl_fio_arendator = QLabel(self.horizontalFrame)
        self.lbl_fio_arendator.setObjectName(u"lbl_fio_arendator")

        self.horizontalLayout.addWidget(self.lbl_fio_arendator)

        self.btn_history_payments = QPushButton(self.horizontalFrame)
        self.btn_history_payments.setObjectName(u"btn_history_payments")
        self.btn_history_payments.setMinimumSize(QSize(180, 40))
        self.btn_history_payments.setMaximumSize(QSize(180, 16777215))
        self.btn_history_payments.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_history_payments)

        self.le_date_registration = QLineEdit(self.horizontalFrame)
        self.le_date_registration.setObjectName(u"le_date_registration")
        self.le_date_registration.setEnabled(False)
        self.le_date_registration.setMinimumSize(QSize(150, 40))
        self.le_date_registration.setMaximumSize(QSize(150, 16777215))
        self.le_date_registration.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_date_registration)

        self.le_count_contract = QLineEdit(self.horizontalFrame)
        self.le_count_contract.setObjectName(u"le_count_contract")
        self.le_count_contract.setEnabled(False)
        self.le_count_contract.setMinimumSize(QSize(80, 40))
        self.le_count_contract.setMaximumSize(QSize(80, 16777215))
        self.le_count_contract.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_count_contract)

        self.btn_hidened_arendator = QPushButton(self.horizontalFrame)
        self.btn_hidened_arendator.setObjectName(u"btn_hidened_arendator")
        self.btn_hidened_arendator.setMinimumSize(QSize(40, 40))
        self.btn_hidened_arendator.setMaximumSize(QSize(40, 40))
        self.btn_hidened_arendator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hidened_arendator.setFocusPolicy(Qt.StrongFocus)
        self.btn_hidened_arendator.setStyleSheet(u"")
        self.btn_hidened_arendator.setIconSize(QSize(30, 30))
        self.btn_hidened_arendator.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_hidened_arendator)

        self.btn_delete = QPushButton(self.horizontalFrame)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(40, 40))
        self.btn_delete.setMaximumSize(QSize(40, 40))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon)
        self.btn_delete.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_delete)


        self.horizontalLayout_2.addWidget(self.horizontalFrame)


        self.retranslateUi(BaseItemArendatorWidget)

        QMetaObject.connectSlotsByName(BaseItemArendatorWidget)
    # setupUi

    def retranslateUi(self, BaseItemArendatorWidget):
        BaseItemArendatorWidget.setWindowTitle(QCoreApplication.translate("BaseItemArendatorWidget", u"Form", None))
        self.lbl_id_arendator.setText("")
        self.lbl_fio_arendator.setText(QCoreApplication.translate("BaseItemArendatorWidget", u"\u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u044c\u0441\u043a\u0438\u0439 \u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u0435\u0446 \u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u044c\u0435\u0432\u0438\u0447", None))
        self.btn_history_payments.setText(QCoreApplication.translate("BaseItemArendatorWidget", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439", None))
#if QT_CONFIG(tooltip)
        self.btn_hidened_arendator.setToolTip(QCoreApplication.translate("BaseItemArendatorWidget", u"\u0421\u043a\u0440\u044b\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_hidened_arendator.setText("")
        self.btn_delete.setText("")
    # retranslateUi

