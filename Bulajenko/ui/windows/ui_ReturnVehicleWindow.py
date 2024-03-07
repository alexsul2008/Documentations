# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReturnVehicleWindowAUzOye.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_WindowReturnVehicle(object):
    def setupUi(self, WindowReturnVehicle):
        if not WindowReturnVehicle.objectName():
            WindowReturnVehicle.setObjectName(u"WindowReturnVehicle")
        WindowReturnVehicle.resize(896, 640)
        WindowReturnVehicle.setMinimumSize(QSize(896, 640))
        WindowReturnVehicle.setMaximumSize(QSize(896, 640))
        WindowReturnVehicle.setStyleSheet(u"")
        self.centralwidget = QWidget(WindowReturnVehicle)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 20, 10, 10)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(170, 0))
        self.label.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_5.addWidget(self.label)

        self.le_fio_arendator = QLineEdit(self.centralwidget)
        self.le_fio_arendator.setObjectName(u"le_fio_arendator")
        self.le_fio_arendator.setEnabled(False)
        self.le_fio_arendator.setMinimumSize(QSize(0, 36))

        self.horizontalLayout_5.addWidget(self.le_fio_arendator)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 10, -1, 10)
        self.lbl_color_ts = QLabel(self.centralwidget)
        self.lbl_color_ts.setObjectName(u"lbl_color_ts")
        self.lbl_color_ts.setMinimumSize(QSize(36, 36))
        self.lbl_color_ts.setMaximumSize(QSize(36, 36))
        self.lbl_color_ts.setStyleSheet(u"background-color: rgb(44, 153, 52);")

        self.horizontalLayout_13.addWidget(self.lbl_color_ts)

        self.lbl_ts = QLineEdit(self.centralwidget)
        self.lbl_ts.setObjectName(u"lbl_ts")
        self.lbl_ts.setEnabled(False)
        self.lbl_ts.setMinimumSize(QSize(340, 36))
        self.lbl_ts.setMaximumSize(QSize(388, 36))

        self.horizontalLayout_13.addWidget(self.lbl_ts)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.label_12)

        self.lbl_vin_ts = QLineEdit(self.centralwidget)
        self.lbl_vin_ts.setObjectName(u"lbl_vin_ts")
        self.lbl_vin_ts.setEnabled(False)
        self.lbl_vin_ts.setMinimumSize(QSize(390, 36))
        self.lbl_vin_ts.setMaximumSize(QSize(390, 36))

        self.horizontalLayout_13.addWidget(self.lbl_vin_ts)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, 0, -1)
        self.grb_equipment = QFrame(self.centralwidget)
        self.grb_equipment.setObjectName(u"grb_equipment")
        self.grb_equipment.setMinimumSize(QSize(380, 245))
        self.grb_equipment.setMaximumSize(QSize(16777215, 245))
        self.grb_equipment.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.grb_equipment)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(45, 0, 12, 0)
        self.label_16 = QLabel(self.grb_equipment)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_4.addWidget(self.label_16)

        self.checkboxes_layout = QVBoxLayout()
        self.checkboxes_layout.setSpacing(10)
        self.checkboxes_layout.setObjectName(u"checkboxes_layout")
        self.checkboxes_layout.setContentsMargins(-1, 0, 0, -1)
        self.chb_lock = QCheckBox(self.grb_equipment)
        self.chb_lock.setObjectName(u"chb_lock")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_lock.sizePolicy().hasHeightForWidth())
        self.chb_lock.setSizePolicy(sizePolicy)
        self.chb_lock.setMinimumSize(QSize(0, 30))
        self.chb_lock.setMaximumSize(QSize(16777215, 30))
        self.chb_lock.setCursor(QCursor(Qt.PointingHandCursor))
        self.chb_lock.setIconSize(QSize(20, 20))

        self.checkboxes_layout.addWidget(self.chb_lock)

        self.chb_shlem = QCheckBox(self.grb_equipment)
        self.chb_shlem.setObjectName(u"chb_shlem")
        sizePolicy.setHeightForWidth(self.chb_shlem.sizePolicy().hasHeightForWidth())
        self.chb_shlem.setSizePolicy(sizePolicy)
        self.chb_shlem.setMinimumSize(QSize(0, 30))
        self.chb_shlem.setMaximumSize(QSize(16777215, 30))
        self.chb_shlem.setCursor(QCursor(Qt.PointingHandCursor))

        self.checkboxes_layout.addWidget(self.chb_shlem)

        self.chb_termocorob = QCheckBox(self.grb_equipment)
        self.chb_termocorob.setObjectName(u"chb_termocorob")
        sizePolicy.setHeightForWidth(self.chb_termocorob.sizePolicy().hasHeightForWidth())
        self.chb_termocorob.setSizePolicy(sizePolicy)
        self.chb_termocorob.setMinimumSize(QSize(0, 30))
        self.chb_termocorob.setMaximumSize(QSize(16777215, 30))
        self.chb_termocorob.setCursor(QCursor(Qt.PointingHandCursor))

        self.checkboxes_layout.addWidget(self.chb_termocorob)

        self.chb_chehol = QCheckBox(self.grb_equipment)
        self.chb_chehol.setObjectName(u"chb_chehol")
        sizePolicy.setHeightForWidth(self.chb_chehol.sizePolicy().hasHeightForWidth())
        self.chb_chehol.setSizePolicy(sizePolicy)
        self.chb_chehol.setMinimumSize(QSize(0, 30))
        self.chb_chehol.setMaximumSize(QSize(16777215, 30))
        self.chb_chehol.setCursor(QCursor(Qt.PointingHandCursor))

        self.checkboxes_layout.addWidget(self.chb_chehol)


        self.verticalLayout_4.addLayout(self.checkboxes_layout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.le_equipment = QLineEdit(self.grb_equipment)
        self.le_equipment.setObjectName(u"le_equipment")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_equipment.sizePolicy().hasHeightForWidth())
        self.le_equipment.setSizePolicy(sizePolicy1)
        self.le_equipment.setMinimumSize(QSize(0, 30))
        self.le_equipment.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.le_equipment)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.grb_equipment)

        self.infoBox = QFrame(self.centralwidget)
        self.infoBox.setObjectName(u"infoBox")
        self.infoBox.setMinimumSize(QSize(440, 245))
        self.infoBox.setMaximumSize(QSize(440, 245))
        self.infoBox.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.infoBox)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.infoBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_2.addWidget(self.label_15)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.infoBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(110, 0))
        self.label_3.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_9.addWidget(self.label_3)

        self.date_return = QLineEdit(self.infoBox)
        self.date_return.setObjectName(u"date_return")
        self.date_return.setEnabled(False)
        self.date_return.setMinimumSize(QSize(150, 30))
        self.date_return.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_9.addWidget(self.date_return)

        self.label_9 = QLabel(self.infoBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.label_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = QLabel(self.infoBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_8.addWidget(self.label_4)

        self.le_prev_mileage = QLineEdit(self.infoBox)
        self.le_prev_mileage.setObjectName(u"le_prev_mileage")
        sizePolicy2.setHeightForWidth(self.le_prev_mileage.sizePolicy().hasHeightForWidth())
        self.le_prev_mileage.setSizePolicy(sizePolicy2)
        self.le_prev_mileage.setMinimumSize(QSize(150, 30))
        self.le_prev_mileage.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_8.addWidget(self.le_prev_mileage)

        self.label_5 = QLabel(self.infoBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.label_5)

        self.lbl_error = QLabel(self.infoBox)
        self.lbl_error.setObjectName(u"lbl_error")
        font = QFont()
        font.setPointSize(7)
        self.lbl_error.setFont(font)

        self.horizontalLayout_8.addWidget(self.lbl_error)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_8 = QLabel(self.infoBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(110, 0))
        self.label_8.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_4.addWidget(self.label_8, 0, Qt.AlignLeft)

        self.le_size_dolg = QLineEdit(self.infoBox)
        self.le_size_dolg.setObjectName(u"le_size_dolg")
        sizePolicy2.setHeightForWidth(self.le_size_dolg.sizePolicy().hasHeightForWidth())
        self.le_size_dolg.setSizePolicy(sizePolicy2)
        self.le_size_dolg.setMinimumSize(QSize(150, 30))
        self.le_size_dolg.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_4.addWidget(self.le_size_dolg)

        self.label_2 = QLabel(self.infoBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lbl_error_2 = QLabel(self.infoBox)
        self.lbl_error_2.setObjectName(u"lbl_error_2")

        self.horizontalLayout_4.addWidget(self.lbl_error_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.le_comment_size_dolg = QLineEdit(self.infoBox)
        self.le_comment_size_dolg.setObjectName(u"le_comment_size_dolg")
        self.le_comment_size_dolg.setMinimumSize(QSize(400, 30))
        self.le_comment_size_dolg.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_10.addWidget(self.le_comment_size_dolg)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.label_11 = QLabel(self.infoBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(110, 0))
        self.label_11.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_6.addWidget(self.label_11)

        self.cb_status_ts = QComboBox(self.infoBox)
        self.cb_status_ts.setObjectName(u"cb_status_ts")
        sizePolicy1.setHeightForWidth(self.cb_status_ts.sizePolicy().hasHeightForWidth())
        self.cb_status_ts.setSizePolicy(sizePolicy1)
        self.cb_status_ts.setMinimumSize(QSize(0, 30))
        self.cb_status_ts.setMaximumSize(QSize(16777215, 30))
        self.cb_status_ts.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.cb_status_ts)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.infoBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.label_10)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 10)
        self.le_defect = QLineEdit(self.centralwidget)
        self.le_defect.setObjectName(u"le_defect")
        self.le_defect.setMinimumSize(QSize(0, 30))
        self.le_defect.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.le_defect)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.lbl_ts_id = QLabel(self.centralwidget)
        self.lbl_ts_id.setObjectName(u"lbl_ts_id")
        self.lbl_ts_id.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_12.addWidget(self.lbl_ts_id)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.lbl_dogovor_id = QLabel(self.centralwidget)
        self.lbl_dogovor_id.setObjectName(u"lbl_dogovor_id")
        self.lbl_dogovor_id.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_12.addWidget(self.lbl_dogovor_id)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(150, 40))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 40))

        self.horizontalLayout_2.addWidget(self.label_14)

        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(150, 40))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_close)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        WindowReturnVehicle.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(WindowReturnVehicle)
        self.statusbar.setObjectName(u"statusbar")
        WindowReturnVehicle.setStatusBar(self.statusbar)

        self.retranslateUi(WindowReturnVehicle)

        QMetaObject.connectSlotsByName(WindowReturnVehicle)
    # setupUi

    def retranslateUi(self, WindowReturnVehicle):
        WindowReturnVehicle.setWindowTitle(QCoreApplication.translate("WindowReturnVehicle", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.le_fio_arendator.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u044c\u0441\u043a\u0438\u0439 \u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u0435\u0446 \u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u044c\u0435\u0432\u0438\u0447", None))
        self.lbl_color_ts.setText("")
        self.lbl_ts.setText(QCoreApplication.translate("WindowReturnVehicle", u"Yamaha Vino", None))
        self.label_12.setText(QCoreApplication.translate("WindowReturnVehicle", u"VIN:", None))
        self.lbl_vin_ts.setText(QCoreApplication.translate("WindowReturnVehicle", u"333-333-333-33", None))
        self.label_16.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0414\u043e\u043f. \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.chb_lock.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0437\u0430\u043c\u043e\u043a", None))
        self.chb_shlem.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0448\u043b\u0435\u043c", None))
        self.chb_termocorob.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0442\u0435\u0440\u043c\u043e\u043a\u043e\u0440\u043e\u0431", None))
        self.chb_chehol.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0447\u0435\u0445\u043e\u043b \u0434\u043b\u044f \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.label_15.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u0422\u0421", None))
        self.label_3.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0414\u0430\u0442\u0430", None))
        self.label_9.setText("")
        self.label_4.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u041f\u0440\u043e\u0431\u0435\u0433", None))
        self.label_5.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u043a\u043c.", None))
        self.lbl_error.setText("")
        self.label_8.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0417\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_2.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0440\u0443\u0431.", None))
        self.lbl_error_2.setText("")
        self.le_comment_size_dolg.setPlaceholderText(QCoreApplication.translate("WindowReturnVehicle", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0437\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u0438.", None))
        self.label_11.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u041f\u0440\u0438\u0441\u0432\u043e\u0438\u0442\u044c \u0441\u0442\u0430\u0442\u0443\u0441:", None))
        self.label_10.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u041f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f \u0422\u0421 \u0432\u044b\u044f\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u043f\u0440\u0438 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0435:", None))
        self.label_13.setText(QCoreApplication.translate("WindowReturnVehicle", u"ID \u0422\u0421", None))
        self.lbl_ts_id.setText("")
        self.label_6.setText(QCoreApplication.translate("WindowReturnVehicle", u"ID \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.lbl_dogovor_id.setText("")
        self.btn_save.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0432\u043e\u0437\u0432\u0440\u0430\u0442", None))
        self.label_14.setText("")
        self.btn_close.setText(QCoreApplication.translate("WindowReturnVehicle", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

