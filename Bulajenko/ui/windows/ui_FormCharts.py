# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormChartsDBZHvS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_FormCharts(object):
    def setupUi(self, FormCharts):
        if not FormCharts.objectName():
            FormCharts.setObjectName(u"FormCharts")
        FormCharts.resize(1117, 745)
        self.horizontalLayout = QHBoxLayout(FormCharts)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chartLayoutFormArendators = QVBoxLayout()
        self.chartLayoutFormArendators.setObjectName(u"chartLayoutFormArendators")

        self.horizontalLayout.addLayout(self.chartLayoutFormArendators)

        self.chartLayoutFormContract = QVBoxLayout()
        self.chartLayoutFormContract.setObjectName(u"chartLayoutFormContract")

        self.horizontalLayout.addLayout(self.chartLayoutFormContract)


        self.retranslateUi(FormCharts)

        QMetaObject.connectSlotsByName(FormCharts)
    # setupUi

    def retranslateUi(self, FormCharts):
        FormCharts.setWindowTitle(QCoreApplication.translate("FormCharts", u"Form", None))
    # retranslateUi

