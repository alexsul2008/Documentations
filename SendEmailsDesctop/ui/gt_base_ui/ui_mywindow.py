# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyWindowvOaaEu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 585)
        MainWindow.setMinimumSize(QSize(0, 545))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"../../../../icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.frame)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(40, 40))
        self.menu_btn.setMaximumSize(QSize(40, 40))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.menu_btn.setFont(font)
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/chevrons-right_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.menu_btn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.main_header_frame = QFrame(self.header_frame)
        self.main_header_frame.setObjectName(u"main_header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_header_frame.sizePolicy().hasHeightForWidth())
        self.main_header_frame.setSizePolicy(sizePolicy)
        self.main_header_frame.setCursor(QCursor(Qt.SizeAllCursor))
        self.main_header_frame.setFrameShape(QFrame.StyledPanel)
        self.main_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.main_header_frame)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizated_btn = QPushButton(self.frame_2)
        self.minimizated_btn.setObjectName(u"minimizated_btn")
        self.minimizated_btn.setMinimumSize(QSize(40, 0))
        self.minimizated_btn.setMaximumSize(QSize(40, 40))
        self.minimizated_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizated_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizated_btn.setIcon(icon2)
        self.minimizated_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizated_btn)

        self.close_btn = QPushButton(self.frame_2)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(40, 0))
        self.close_btn.setMaximumSize(QSize(40, 40))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.frame_5 = QFrame(self.main_frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 10)
        self.le_cur_cb = QLineEdit(self.frame_5)
        self.le_cur_cb.setObjectName(u"le_cur_cb")
        self.le_cur_cb.setMaximumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.le_cur_cb)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 5)
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_9.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_9)

        self.rbtn_rossvyaz = QRadioButton(self.frame_8)
        self.rbtn_rossvyaz.setObjectName(u"rbtn_rossvyaz")
        self.rbtn_rossvyaz.setMinimumSize(QSize(130, 40))
        self.rbtn_rossvyaz.setMaximumSize(QSize(16777215, 40))
        self.rbtn_rossvyaz.setCursor(QCursor(Qt.PointingHandCursor))
        self.rbtn_rossvyaz.setChecked(True)

        self.horizontalLayout_14.addWidget(self.rbtn_rossvyaz)

        self.rbtn_mgmn = QRadioButton(self.frame_8)
        self.rbtn_mgmn.setObjectName(u"rbtn_mgmn")
        self.rbtn_mgmn.setMinimumSize(QSize(0, 40))
        self.rbtn_mgmn.setMaximumSize(QSize(16777215, 40))
        self.rbtn_mgmn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rbtn_mgmn.setIconSize(QSize(26, 26))

        self.horizontalLayout_14.addWidget(self.rbtn_mgmn)

        self.cb_mgmn_msx = QComboBox(self.frame_8)
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.addItem("")
        self.cb_mgmn_msx.setObjectName(u"cb_mgmn_msx")
        self.cb_mgmn_msx.setEnabled(False)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        self.cb_mgmn_msx.setFont(font2)
        self.cb_mgmn_msx.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.cb_mgmn_msx)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_opc = QFrame(self.frame_5)
        self.frame_opc.setObjectName(u"frame_opc")
        self.frame_opc.setMinimumSize(QSize(0, 0))
        self.frame_opc.setMaximumSize(QSize(16777215, 16777215))
        self.frame_opc.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_opc)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.label_3 = QLabel(self.frame_opc)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.le_opc = QLineEdit(self.frame_opc)
        self.le_opc.setObjectName(u"le_opc")
        self.le_opc.setMinimumSize(QSize(0, 40))
        self.le_opc.setMaximumSize(QSize(16777215, 40))
        self.le_opc.setFont(font1)
        self.le_opc.setStyleSheet(u"")
        self.le_opc.setMaxLength(30)

        self.horizontalLayout_5.addWidget(self.le_opc)


        self.verticalLayout_2.addWidget(self.frame_opc)

        self.frame_51 = QFrame(self.frame_5)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 0))
        self.frame_51.setMaximumSize(QSize(16777215, 16777215))
        self.frame_51.setFont(font2)
        self.frame_51.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.lbl_dpc = QLabel(self.frame_51)
        self.lbl_dpc.setObjectName(u"lbl_dpc")
        self.lbl_dpc.setMinimumSize(QSize(150, 0))
        self.lbl_dpc.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(8)
        self.lbl_dpc.setFont(font3)

        self.horizontalLayout_6.addWidget(self.lbl_dpc)

        self.le_dpc = QLineEdit(self.frame_51)
        self.le_dpc.setObjectName(u"le_dpc")
        self.le_dpc.setMinimumSize(QSize(0, 40))
        self.le_dpc.setMaximumSize(QSize(16777215, 40))
        self.le_dpc.setFont(font1)
        self.le_dpc.setInputMethodHints(Qt.ImhNone)
        self.le_dpc.setMaxLength(30)

        self.horizontalLayout_6.addWidget(self.le_dpc)


        self.verticalLayout_2.addWidget(self.frame_51)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.le_inc = QLineEdit(self.frame_4)
        self.le_inc.setObjectName(u"le_inc")
        self.le_inc.setMinimumSize(QSize(0, 40))
        self.le_inc.setMaximumSize(QSize(16777215, 40))
        self.le_inc.setFont(font1)
        self.le_inc.setMaxLength(15)

        self.horizontalLayout_7.addWidget(self.le_inc)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 5)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))
        self.label_6.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.label_6)

        self.frame1 = QFrame(self.frame_6)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frame1)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.rbtn_sp = QRadioButton(self.frame1)
        self.rbtn_sp.setObjectName(u"rbtn_sp")
        self.rbtn_sp.setMinimumSize(QSize(0, 40))
        self.rbtn_sp.setMaximumSize(QSize(16777215, 40))
        self.rbtn_sp.setChecked(True)

        self.horizontalLayout_9.addWidget(self.rbtn_sp)

        self.rbtn_cic = QRadioButton(self.frame1)
        self.rbtn_cic.setObjectName(u"rbtn_cic")
        self.rbtn_cic.setMinimumSize(QSize(0, 40))
        self.rbtn_cic.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_9.addWidget(self.rbtn_cic)


        self.horizontalLayout_8.addWidget(self.frame1)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_CIC = QFrame(self.frame_5)
        self.frame_CIC.setObjectName(u"frame_CIC")
        self.frame_CIC.setMinimumSize(QSize(0, 0))
        self.frame_CIC.setMaximumSize(QSize(16777215, 0))
        self.frame_CIC.setLineWidth(0)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_CIC)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_CIC)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.label_8)

        self.le_CIC = QLineEdit(self.frame_CIC)
        self.le_CIC.setObjectName(u"le_CIC")
        self.le_CIC.setMinimumSize(QSize(0, 40))
        self.le_CIC.setMaximumSize(QSize(16777215, 40))
        self.le_CIC.setFont(font1)
        self.le_CIC.setMaxLength(15)

        self.horizontalLayout_13.addWidget(self.le_CIC)


        self.verticalLayout_2.addWidget(self.frame_CIC)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.lbl_error = QLabel(self.frame_5)
        self.lbl_error.setObjectName(u"lbl_error")
        self.lbl_error.setMinimumSize(QSize(0, 30))
        self.lbl_error.setMaximumSize(QSize(16777215, 30))
        self.lbl_error.setStyleSheet(u"")
        self.lbl_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_error)

        self.lbl_loading = QLabel(self.frame_5)
        self.lbl_loading.setObjectName(u"lbl_loading")
        self.lbl_loading.setMinimumSize(QSize(50, 50))
        self.lbl_loading.setMaximumSize(QSize(50, 50))
        self.lbl_loading.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.lbl_loading, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 15))
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_2.addWidget(self.label_2)

        self.search_btn = QPushButton(self.frame_5)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy2)
        self.search_btn.setMinimumSize(QSize(0, 50))
        self.search_btn.setMaximumSize(QSize(16777215, 50))
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/search_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.search_btn)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(8)
        self.footer_frame.setFont(font4)
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 0, 5, 0)
        self.label = QLabel(self.footer_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.label.setFont(font5)

        self.horizontalLayout_15.addWidget(self.label)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizated_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043e\u043a\u043d\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.minimizated_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.label_9.setText("")
        self.rbtn_rossvyaz.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0441\u0441\u0432\u044f\u0437\u044c", None))
        self.rbtn_mgmn.setText(QCoreApplication.translate("MainWindow", u"\u0422\u041c\u0433\u0423\u0421 / \u0422\u041c\u043d\u0423\u0421:", None))
        self.cb_mgmn_msx.setItemText(0, "")
        self.cb_mgmn_msx.setItemText(1, QCoreApplication.translate("MainWindow", u"CN-MSK-MSX", None))
        self.cb_mgmn_msx.setItemText(2, QCoreApplication.translate("MainWindow", u"NW-SPB-MSX", None))
        self.cb_mgmn_msx.setItemText(3, QCoreApplication.translate("MainWindow", u"SU-KRD-MSX", None))
        self.cb_mgmn_msx.setItemText(4, QCoreApplication.translate("MainWindow", u"UR-EKT-MSX", None))
        self.cb_mgmn_msx.setItemText(5, QCoreApplication.translate("MainWindow", u"PV-NNV-MSX", None))
        self.cb_mgmn_msx.setItemText(6, QCoreApplication.translate("MainWindow", u"SB-NSK-MSX", None))
        self.cb_mgmn_msx.setItemText(7, QCoreApplication.translate("MainWindow", u"DV-VLD-MSX", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"OPC:", None))
        self.lbl_dpc.setText(QCoreApplication.translate("MainWindow", u"DPC:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0446\u0438\u0434\u0435\u043d\u0442:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u0438\u0441\u044c\u043c\u0430:", None))
        self.rbtn_sp.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0433\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u0442\u043e\u0447\u043a\u0430", None))
        self.rbtn_cic.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043a\u0430\u043d\u0430\u043b\u043e\u0432", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CIC:", None))
        self.lbl_error.setText("")
        self.lbl_loading.setText("")
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.search_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u043e \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created by avsulyay@mts.ru", None))
    # retranslateUi

