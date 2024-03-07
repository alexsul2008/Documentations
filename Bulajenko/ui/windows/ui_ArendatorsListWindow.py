# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArendatorsListWindowctSCGr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ArendatorsListWindow(object):
    def setupUi(self, ArendatorsListWindow):
        if not ArendatorsListWindow.objectName():
            ArendatorsListWindow.setObjectName(u"ArendatorsListWindow")
        ArendatorsListWindow.resize(1291, 896)
        self.centralwidget = QWidget(ArendatorsListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_arendators = QFrame(self.centralwidget)
        self.frm_arendators.setObjectName(u"frm_arendators")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_arendators.sizePolicy().hasHeightForWidth())
        self.frm_arendators.setSizePolicy(sizePolicy)
        self.frm_arendators.setFrameShape(QFrame.StyledPanel)
        self.frm_arendators.setFrameShadow(QFrame.Raised)
        self.frm_arendators.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frm_arendators)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 10, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 5)
        self.layoutSearchArendator = QHBoxLayout()
        self.layoutSearchArendator.setSpacing(5)
        self.layoutSearchArendator.setObjectName(u"layoutSearchArendator")
        self.layoutSearchArendator.setContentsMargins(-1, -1, -1, 15)
        self.surname___text = QLineEdit(self.frm_arendators)
        self.surname___text.setObjectName(u"surname___text")
        self.surname___text.setMinimumSize(QSize(0, 40))
        self.surname___text.setClearButtonEnabled(True)

        self.layoutSearchArendator.addWidget(self.surname___text)

        self.cb_arendators = QComboBox(self.frm_arendators)
        self.cb_arendators.setObjectName(u"cb_arendators")
        self.cb_arendators.setMinimumSize(QSize(200, 40))

        self.layoutSearchArendator.addWidget(self.cb_arendators)

        self.groupBox = QGroupBox(self.frm_arendators)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.hiden_arendator__all = QRadioButton(self.groupBox)
        self.hiden_arendator__all.setObjectName(u"hiden_arendator__all")
        self.hiden_arendator__all.setMinimumSize(QSize(0, 30))
        self.hiden_arendator__all.setChecked(True)

        self.horizontalLayout_6.addWidget(self.hiden_arendator__all)

        self.hiden_arendator__active = QRadioButton(self.groupBox)
        self.hiden_arendator__active.setObjectName(u"hiden_arendator__active")
        self.hiden_arendator__active.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.hiden_arendator__active)

        self.hiden_arendator__hidened = QRadioButton(self.groupBox)
        self.hiden_arendator__hidened.setObjectName(u"hiden_arendator__hidened")
        self.hiden_arendator__hidened.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.hiden_arendator__hidened)


        self.layoutSearchArendator.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.layoutSearchArendator)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.frm_arendators)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(60, 40))
        self.label.setMaximumSize(QSize(60, 40))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.frm_arendators)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.label_3 = QLabel(self.frm_arendators)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(150, 40))
        self.label_3.setMaximumSize(QSize(150, 40))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.frm_arendators)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(80, 40))
        self.label_4.setMaximumSize(QSize(80, 40))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.lbl_indent_elements = QLabel(self.frm_arendators)
        self.lbl_indent_elements.setObjectName(u"lbl_indent_elements")
        sizePolicy3.setHeightForWidth(self.lbl_indent_elements.sizePolicy().hasHeightForWidth())
        self.lbl_indent_elements.setSizePolicy(sizePolicy3)
        self.lbl_indent_elements.setMinimumSize(QSize(40, 40))
        self.lbl_indent_elements.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.lbl_indent_elements, 0, Qt.AlignTop)

        self.label_6 = QLabel(self.frm_arendators)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(19, 40))
        self.label_6.setMaximumSize(QSize(0, 40))

        self.horizontalLayout_7.addWidget(self.label_6, 0, Qt.AlignTop)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.scrollArea = QScrollArea(self.frm_arendators)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1267, 770))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.arendators_base_layout = QVBoxLayout()
        self.arendators_base_layout.setSpacing(5)
        self.arendators_base_layout.setObjectName(u"arendators_base_layout")

        self.verticalLayout_3.addLayout(self.arendators_base_layout)

        self.verticalSpacer = QSpacerItem(20, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frm_arendators)

        ArendatorsListWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArendatorsListWindow)

        QMetaObject.connectSlotsByName(ArendatorsListWindow)
    # setupUi

    def retranslateUi(self, ArendatorsListWindow):
        ArendatorsListWindow.setWindowTitle(QCoreApplication.translate("ArendatorsListWindow", u"MainWindow", None))
        self.cb_arendators.setPlaceholderText(QCoreApplication.translate("ArendatorsListWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e...", None))
        self.groupBox.setTitle("")
        self.hiden_arendator__all.setText(QCoreApplication.translate("ArendatorsListWindow", u"\u0412\u0441\u0435", None))
        self.hiden_arendator__active.setText(QCoreApplication.translate("ArendatorsListWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0435", None))
        self.hiden_arendator__hidened.setText(QCoreApplication.translate("ArendatorsListWindow", u"\u0421\u043a\u0440\u044b\u0442\u044b\u0435", None))
        self.label.setText(QCoreApplication.translate("ArendatorsListWindow", u"\u2116\n"
"\u043f/\u043f", None))
        self.label_2.setText(QCoreApplication.translate("ArendatorsListWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_3.setText(QCoreApplication.translate("ArendatorsListWindow", u"\u0414\u0430\u0442\u0430\n"
"\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.label_4.setText(QCoreApplication.translate("ArendatorsListWindow", u"\u0412\u0441\u0435\u0433\u043e\n"
"\u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432", None))
        self.lbl_indent_elements.setText("")
        self.label_6.setText("")
    # retranslateUi

