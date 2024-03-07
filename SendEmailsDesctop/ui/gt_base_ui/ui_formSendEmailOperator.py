# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formSendEmailOperatorgQIJRj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_FormSendEmailOperator(object):
    def setupUi(self, FormSendEmailOperator):
        if not FormSendEmailOperator.objectName():
            FormSendEmailOperator.setObjectName(u"FormSendEmailOperator")
        FormSendEmailOperator.resize(1362, 906)
        FormSendEmailOperator.setStyleSheet(u"*{\n"
"	font: 14pt \"Arial\";\n"
"	background-color:rgb(42, 61, 79);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QToolButton{	\n"
"	font: 12pt \"Arial\";\n"
"	background-color: rgb(29, 32, 35);\n"
"	border: 2px solid #c6c6c6;\n"
"	border-radius: 3px;\n"
"	text-align: center;\n"
"	padding: 25px 0px 10px 0px;\n"
"}\n"
"QToolButton:hover{	\n"
"	background-color: rgb(118, 121, 124);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #1d2023;\n"
"    padding:5px;\n"
"    border-style: solid;\n"
"    border: 2px solid #76797c;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"\n"
"QTextEdit, QLineEdit\n"
"{\n"
"    border: 2px solid #c6c6c6;\n"
"    border-radius:2px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:open\n"
"{\n"
"    border-width: 2px;\n"
"    border-color: #76797c;\n"
"}\n"
"\n"
"QPushButton:closed\n"
"{\n"
"    border-width: 0.04em;\n"
"    border-color: #76797c;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	font: 12pt \"Arial\";\n"
"	background-color: rgb(255, 255, "
                        "255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QTextEdit:hover,\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid #3daee9;\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus,\n"
"QAbstractSpinBox:hover,\n"
"QAbstractSpinBox:focus,\n"
"QPlainTextEdit:hover,\n"
"QPlainTextEdit:focus,\n"
"QAbstractView:hover,\n"
"QToolButton:hover\n"
"{\n"
"    border: 2px solid #3daee9;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover:pressed,\n"
"QPushButton:hover:pressed,\n"
"QAbstractSpinBox:hover:pressed,\n"
"QTextEdit:hover:pressed,\n"
"QPlainTextEdit:hover:pressed,\n"
"QAbstractView:hover:pressed\n"
"{\n"
"    background-color: #31363b;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(FormSendEmailOperator)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.centralwidget = QWidget(FormSendEmailOperator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.lbl_top_main_header_frame = QLabel(self.frame_top)
        self.lbl_top_main_header_frame.setObjectName(u"lbl_top_main_header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_top_main_header_frame.sizePolicy().hasHeightForWidth())
        self.lbl_top_main_header_frame.setSizePolicy(sizePolicy)
        self.lbl_top_main_header_frame.setMinimumSize(QSize(0, 50))
        self.lbl_top_main_header_frame.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_top_main_header_frame.setFont(font)
        self.lbl_top_main_header_frame.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbl_top_main_header_frame, 0, Qt.AlignLeft)

        self.lbl_top_name_operaror = QLabel(self.frame_top)
        self.lbl_top_name_operaror.setObjectName(u"lbl_top_name_operaror")
        sizePolicy.setHeightForWidth(self.lbl_top_name_operaror.sizePolicy().hasHeightForWidth())
        self.lbl_top_name_operaror.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.lbl_top_name_operaror)

        self.frame_3 = QFrame(self.frame_top)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(62, 90, 116);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_minimazed = QPushButton(self.frame_3)
        self.btn_minimazed.setObjectName(u"btn_minimazed")
        self.btn_minimazed.setMinimumSize(QSize(32, 32))
        self.btn_minimazed.setMaximumSize(QSize(32, 32))
        self.btn_minimazed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimazed.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimazed.setIcon(icon)
        self.btn_minimazed.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_minimazed)

        self.btn_maximized = QPushButton(self.frame_3)
        self.btn_maximized.setObjectName(u"btn_maximized")
        self.btn_maximized.setMinimumSize(QSize(32, 32))
        self.btn_maximized.setMaximumSize(QSize(32, 32))
        self.btn_maximized.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize-2_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximized.setIcon(icon1)
        self.btn_maximized.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_maximized)

        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(235, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_close)


        self.horizontalLayout_7.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_top)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnSendEmail = QToolButton(self.frame_5)
        self.btnSendEmail.setObjectName(u"btnSendEmail")
        self.btnSendEmail.setMinimumSize(QSize(105, 105))
        self.btnSendEmail.setMaximumSize(QSize(105, 105))
        self.btnSendEmail.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSendEmail.setAutoFillBackground(False)
        self.btnSendEmail.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/send-mail-2574_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSendEmail.setIcon(icon3)
        self.btnSendEmail.setIconSize(QSize(32, 32))
        self.btnSendEmail.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btnSendEmail.setAutoRaise(False)
        self.btnSendEmail.setArrowType(Qt.NoArrow)

        self.verticalLayout_2.addWidget(self.btnSendEmail)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_7)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.frame_To = QFrame(self.frame_7)
        self.frame_To.setObjectName(u"frame_To")
        self.frame_To.setMinimumSize(QSize(0, 50))
        self.frame_To.setMaximumSize(QSize(16777215, 50))
        self.frame_To.setFrameShape(QFrame.StyledPanel)
        self.frame_To.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_To)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
        self.label = QLabel(self.frame_To)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.label)

        self.le_To = QLineEdit(self.frame_To)
        self.le_To.setObjectName(u"le_To")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_To.sizePolicy().hasHeightForWidth())
        self.le_To.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.le_To)


        self.verticalLayout.addWidget(self.frame_To)

        self.frame_Cc = QFrame(self.frame_7)
        self.frame_Cc.setObjectName(u"frame_Cc")
        self.frame_Cc.setMinimumSize(QSize(0, 50))
        self.frame_Cc.setMaximumSize(QSize(16777215, 50))
        self.frame_Cc.setFrameShape(QFrame.StyledPanel)
        self.frame_Cc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_Cc)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.label_2 = QLabel(self.frame_Cc)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_Cc = QLineEdit(self.frame_Cc)
        self.le_Cc.setObjectName(u"le_Cc")
        sizePolicy1.setHeightForWidth(self.le_Cc.sizePolicy().hasHeightForWidth())
        self.le_Cc.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.le_Cc)


        self.verticalLayout.addWidget(self.frame_Cc)

        self.frame_Subject = QFrame(self.frame_7)
        self.frame_Subject.setObjectName(u"frame_Subject")
        self.frame_Subject.setMinimumSize(QSize(0, 50))
        self.frame_Subject.setMaximumSize(QSize(16777215, 50))
        self.frame_Subject.setFrameShape(QFrame.StyledPanel)
        self.frame_Subject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_Subject)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.label_4 = QLabel(self.frame_Subject)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.le_Subject = QLineEdit(self.frame_Subject)
        self.le_Subject.setObjectName(u"le_Subject")
        sizePolicy1.setHeightForWidth(self.le_Subject.sizePolicy().hasHeightForWidth())
        self.le_Subject.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.le_Subject)


        self.verticalLayout.addWidget(self.frame_Subject)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame)

        self.te_Message = QTextEdit(self.centralwidget)
        self.te_Message.setObjectName(u"te_Message")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.te_Message.setFont(font1)

        self.verticalLayout_4.addWidget(self.te_Message)

        self.grip_size = QFrame(self.centralwidget)
        self.grip_size.setObjectName(u"grip_size")
        self.grip_size.setMinimumSize(QSize(10, 10))
        self.grip_size.setMaximumSize(QSize(10, 10))
        self.grip_size.setFrameShape(QFrame.StyledPanel)
        self.grip_size.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.grip_size, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.centralwidget)


        self.retranslateUi(FormSendEmailOperator)

        QMetaObject.connectSlotsByName(FormSendEmailOperator)
    # setupUi

    def retranslateUi(self, FormSendEmailOperator):
        FormSendEmailOperator.setWindowTitle(QCoreApplication.translate("FormSendEmailOperator", u"Form", None))
        self.lbl_top_main_header_frame.setText(QCoreApplication.translate("FormSendEmailOperator", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u043c\u044b\u0439 E-mail \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0443: ", None))
        self.lbl_top_name_operaror.setText("")
        self.btn_minimazed.setText("")
        self.btn_maximized.setText("")
        self.btn_close.setText("")
        self.btnSendEmail.setText(QCoreApplication.translate("FormSendEmailOperator", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("FormSendEmailOperator", u"\u041a\u043e\u043c\u0443...", None))
        self.label_2.setText(QCoreApplication.translate("FormSendEmailOperator", u"\u041a\u043e\u043f\u0438\u044f...", None))
        self.label_4.setText(QCoreApplication.translate("FormSendEmailOperator", u"\u0422\u0435\u043c\u0430", None))
    # retranslateUi

