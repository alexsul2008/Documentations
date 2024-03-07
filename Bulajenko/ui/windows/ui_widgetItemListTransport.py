# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetItemListTransportYRLsPU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_WidgetItemListTransport(object):
    def setupUi(self, WidgetItemListTransport):
        if not WidgetItemListTransport.objectName():
            WidgetItemListTransport.setObjectName(u"WidgetItemListTransport")
        WidgetItemListTransport.resize(1232, 84)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetItemListTransport.sizePolicy().hasHeightForWidth())
        WidgetItemListTransport.setSizePolicy(sizePolicy)
        WidgetItemListTransport.setMaximumSize(QSize(16777215, 16777215))
        WidgetItemListTransport.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(WidgetItemListTransport)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WidgetItemListTransport)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, 0)
        self.lbl_color_ts = QLabel(self.frame)
        self.lbl_color_ts.setObjectName(u"lbl_color_ts")
        self.lbl_color_ts.setMinimumSize(QSize(16, 0))
        self.lbl_color_ts.setMaximumSize(QSize(16, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_color_ts)

        self.lbl_photo = QLabel(self.frame)
        self.lbl_photo.setObjectName(u"lbl_photo")
        self.lbl_photo.setMinimumSize(QSize(80, 60))
        self.lbl_photo.setMaximumSize(QSize(80, 60))

        self.horizontalLayout_6.addWidget(self.lbl_photo)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(8)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.lbl_brand = QLineEdit(self.frame)
        self.lbl_brand.setObjectName(u"lbl_brand")
        self.lbl_brand.setEnabled(False)
        self.lbl_brand.setMinimumSize(QSize(150, 26))

        self.horizontalLayout_2.addWidget(self.lbl_brand)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(50, 16777215))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lbl_model = QLineEdit(self.frame)
        self.lbl_model.setObjectName(u"lbl_model")
        self.lbl_model.setEnabled(False)
        self.lbl_model.setMinimumSize(QSize(150, 26))

        self.horizontalLayout_2.addWidget(self.lbl_model)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))
        self.label_3.setMaximumSize(QSize(50, 16777215))
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lbl_vin = QLineEdit(self.frame)
        self.lbl_vin.setObjectName(u"lbl_vin")
        self.lbl_vin.setEnabled(False)
        self.lbl_vin.setMinimumSize(QSize(50, 26))

        self.horizontalLayout_3.addWidget(self.lbl_vin)

        self.lbl_prev_milage = QLabel(self.frame)
        self.lbl_prev_milage.setObjectName(u"lbl_prev_milage")
        self.lbl_prev_milage.setMinimumSize(QSize(45, 15))

        self.horizontalLayout_3.addWidget(self.lbl_prev_milage)

        self.le_prev_milage_list = QLineEdit(self.frame)
        self.le_prev_milage_list.setObjectName(u"le_prev_milage_list")
        self.le_prev_milage_list.setEnabled(False)
        self.le_prev_milage_list.setMinimumSize(QSize(0, 26))
        self.le_prev_milage_list.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_3.addWidget(self.le_prev_milage_list)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.lbl_price_category = QLabel(self.frame)
        self.lbl_price_category.setObjectName(u"lbl_price_category")
        self.lbl_price_category.setMinimumSize(QSize(100, 0))
        self.lbl_price_category.setMaximumSize(QSize(100, 16777215))
        self.lbl_price_category.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lbl_price_category)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 26))
        self.label_6.setMaximumSize(QSize(100, 16777215))
        self.label_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lbl_status = QLabel(self.frame)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setMinimumSize(QSize(210, 26))
        self.lbl_status.setMaximumSize(QSize(210, 16777215))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl_status.setFont(font1)
        self.lbl_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_status)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 26))
        self.label_8.setMaximumSize(QSize(100, 16777215))
        self.label_8.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lbl_mileage = QLineEdit(self.frame)
        self.lbl_mileage.setObjectName(u"lbl_mileage")
        self.lbl_mileage.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lbl_mileage.sizePolicy().hasHeightForWidth())
        self.lbl_mileage.setSizePolicy(sizePolicy)
        self.lbl_mileage.setMinimumSize(QSize(210, 26))
        self.lbl_mileage.setMaximumSize(QSize(210, 16777215))

        self.horizontalLayout_5.addWidget(self.lbl_mileage)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(110, 30))
        self.pushButton.setMaximumSize(QSize(150, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(110, 30))
        self.pushButton_2.setMaximumSize(QSize(150, 16777215))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.btn_calculator = QPushButton(self.frame)
        self.btn_calculator.setObjectName(u"btn_calculator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_calculator.sizePolicy().hasHeightForWidth())
        self.btn_calculator.setSizePolicy(sizePolicy1)
        self.btn_calculator.setMinimumSize(QSize(40, 40))
        self.btn_calculator.setMaximumSize(QSize(40, 40))
        self.btn_calculator.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/calendar_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_calculator.setIcon(icon)
        self.btn_calculator.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.btn_calculator)

        self.btn_delete = QPushButton(self.frame)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy2)
        self.btn_delete.setMinimumSize(QSize(40, 40))
        self.btn_delete.setMaximumSize(QSize(40, 40))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/trash_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_delete)

        self.lbl_id_ts = QLabel(self.frame)
        self.lbl_id_ts.setObjectName(u"lbl_id_ts")
        self.lbl_id_ts.setMinimumSize(QSize(20, 20))
        self.lbl_id_ts.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.lbl_id_ts)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(WidgetItemListTransport)

        QMetaObject.connectSlotsByName(WidgetItemListTransport)
    # setupUi

    def retranslateUi(self, WidgetItemListTransport):
        WidgetItemListTransport.setWindowTitle(QCoreApplication.translate("WidgetItemListTransport", u"Form", None))
        self.lbl_color_ts.setText("")
        self.lbl_photo.setText("")
        self.label.setText(QCoreApplication.translate("WidgetItemListTransport", u"\u041c\u0430\u0440\u043a\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("WidgetItemListTransport", u"\u041c\u043e\u0434\u0435\u043b\u044c:", None))
        self.label_3.setText(QCoreApplication.translate("WidgetItemListTransport", u"VIN:", None))
        self.lbl_prev_milage.setText(QCoreApplication.translate("WidgetItemListTransport", u"\u041f\u0440\u043e\u0431\u0435\u0433:", None))
        self.lbl_price_category.setText(QCoreApplication.translate("WidgetItemListTransport", u"3500 \u0440./\u043d\u0435\u0434", None))
        self.label_6.setText(QCoreApplication.translate("WidgetItemListTransport", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.lbl_status.setText("")
        self.label_8.setText(QCoreApplication.translate("WidgetItemListTransport", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u0422\u041e:", None))
        self.pushButton.setText(QCoreApplication.translate("WidgetItemListTransport", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u044b\u043a\u0443\u043f", None))
        self.pushButton_2.setText(QCoreApplication.translate("WidgetItemListTransport", u"\u0421\u0434\u0430\u0442\u044c \u0432 \u0430\u0440\u0435\u043d\u0434\u0443", None))
#if QT_CONFIG(tooltip)
        self.btn_calculator.setToolTip(QCoreApplication.translate("WidgetItemListTransport", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
#endif // QT_CONFIG(tooltip)
        self.btn_calculator.setText("")
        self.btn_delete.setText("")
        self.lbl_id_ts.setText("")
    # retranslateUi

