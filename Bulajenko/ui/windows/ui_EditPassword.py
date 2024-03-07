# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditPasswordQFhuPg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_DialogEditPassword(object):
    def setupUi(self, DialogEditPassword):
        if not DialogEditPassword.objectName():
            DialogEditPassword.setObjectName(u"DialogEditPassword")
        DialogEditPassword.resize(400, 320)
        self.verticalLayout_2 = QVBoxLayout(DialogEditPassword)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(DialogEditPassword)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.label)

        self.le_new_password = QLineEdit(DialogEditPassword)
        self.le_new_password.setObjectName(u"le_new_password")
        self.le_new_password.setMinimumSize(QSize(0, 40))
        self.le_new_password.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.le_new_password)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(DialogEditPassword)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.label_2)

        self.le_repeat_password = QLineEdit(DialogEditPassword)
        self.le_repeat_password.setObjectName(u"le_repeat_password")
        self.le_repeat_password.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.le_repeat_password)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.Responser = QLabel(DialogEditPassword)
        self.Responser.setObjectName(u"Responser")
        self.Responser.setMinimumSize(QSize(0, 24))
        self.Responser.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Responser)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(DialogEditPassword)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setCursor(QCursor(Qt.ArrowCursor))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(DialogEditPassword)
        self.buttonBox.accepted.connect(DialogEditPassword.accept)
        self.buttonBox.rejected.connect(DialogEditPassword.reject)

        QMetaObject.connectSlotsByName(DialogEditPassword)
    # setupUi

    def retranslateUi(self, DialogEditPassword):
        DialogEditPassword.setWindowTitle(QCoreApplication.translate("DialogEditPassword", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("DialogEditPassword", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("DialogEditPassword", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u0432\u0432\u043e\u0434 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.Responser.setText("")
    # retranslateUi

