# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransportCardWindowfAFeMe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_TransportCardWindow(object):
    def setupUi(self, TransportCardWindow):
        if not TransportCardWindow.objectName():
            TransportCardWindow.setObjectName(u"TransportCardWindow")
        TransportCardWindow.resize(750, 760)
        TransportCardWindow.setMinimumSize(QSize(750, 760))
        TransportCardWindow.setMaximumSize(QSize(16777215, 760))
        self.centralwidget = QWidget(TransportCardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.all_fields_layout = QVBoxLayout()
        self.all_fields_layout.setSpacing(0)
        self.all_fields_layout.setObjectName(u"all_fields_layout")
        self.all_fields_layout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(100, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 69, 268))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_18.addWidget(self.scrollArea)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_photo = QLabel(self.centralwidget)
        self.lbl_photo.setObjectName(u"lbl_photo")
        self.lbl_photo.setMinimumSize(QSize(400, 226))
        self.lbl_photo.setMaximumSize(QSize(400, 226))
        self.lbl_photo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_photo)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_select_status = QPushButton(self.centralwidget)
        self.btn_select_status.setObjectName(u"btn_select_status")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_select_status.sizePolicy().hasHeightForWidth())
        self.btn_select_status.setSizePolicy(sizePolicy)
        self.btn_select_status.setMinimumSize(QSize(0, 34))
        self.btn_select_status.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.btn_select_status)

        self.btn_add_image = QPushButton(self.centralwidget)
        self.btn_add_image.setObjectName(u"btn_add_image")
        self.btn_add_image.setMinimumSize(QSize(34, 34))
        self.btn_add_image.setMaximumSize(QSize(34, 34))
        self.btn_add_image.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/plus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_image.setIcon(icon)

        self.horizontalLayout_17.addWidget(self.btn_add_image)

        self.btn_image_upload = QPushButton(self.centralwidget)
        self.btn_image_upload.setObjectName(u"btn_image_upload")
        self.btn_image_upload.setMinimumSize(QSize(34, 34))
        self.btn_image_upload.setMaximumSize(QSize(34, 34))
        self.btn_image_upload.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/refresh-ccw_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_image_upload.setIcon(icon1)
        self.btn_image_upload.setIconSize(QSize(20, 20))

        self.horizontalLayout_17.addWidget(self.btn_image_upload)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.verticalLayout_3)

        self.technical_info_layout = QVBoxLayout()
        self.technical_info_layout.setSpacing(5)
        self.technical_info_layout.setObjectName(u"technical_info_layout")
        self.technical_info_layout.setContentsMargins(5, 10, 0, -1)
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 26))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"padding-left:5px;")

        self.technical_info_layout.addWidget(self.label_25)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label)

        self.cb_type_transport_id = QComboBox(self.centralwidget)
        self.cb_type_transport_id.setObjectName(u"cb_type_transport_id")
        self.cb_type_transport_id.setMinimumSize(QSize(0, 26))
        self.cb_type_transport_id.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.cb_type_transport_id)


        self.technical_info_layout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.le_brand = QLineEdit(self.centralwidget)
        self.le_brand.setObjectName(u"le_brand")
        self.le_brand.setMinimumSize(QSize(0, 26))

        self.horizontalLayout.addWidget(self.le_brand)


        self.technical_info_layout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.le_model = QLineEdit(self.centralwidget)
        self.le_model.setObjectName(u"le_model")
        self.le_model.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.le_model)


        self.technical_info_layout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.le_bodywork = QLineEdit(self.centralwidget)
        self.le_bodywork.setObjectName(u"le_bodywork")
        self.le_bodywork.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_3.addWidget(self.le_bodywork)


        self.technical_info_layout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_19.addWidget(self.label_9)

        self.le_number_engine = QLineEdit(self.centralwidget)
        self.le_number_engine.setObjectName(u"le_number_engine")
        self.le_number_engine.setMinimumSize(QSize(0, 26))
        self.le_number_engine.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_19.addWidget(self.le_number_engine)


        self.technical_info_layout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.btn_select_color = QPushButton(self.centralwidget)
        self.btn_select_color.setObjectName(u"btn_select_color")
        sizePolicy.setHeightForWidth(self.btn_select_color.sizePolicy().hasHeightForWidth())
        self.btn_select_color.setSizePolicy(sizePolicy)
        self.btn_select_color.setMinimumSize(QSize(0, 28))
        self.btn_select_color.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_select_color)


        self.technical_info_layout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.le_engine_volume = QLineEdit(self.centralwidget)
        self.le_engine_volume.setObjectName(u"le_engine_volume")
        self.le_engine_volume.setMinimumSize(QSize(70, 26))
        self.le_engine_volume.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_5.addWidget(self.le_engine_volume)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(40, 0))
        self.label_20.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.label_20)


        self.technical_info_layout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_18.addLayout(self.technical_info_layout)


        self.all_fields_layout.addLayout(self.horizontalLayout_18)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.all_fields_layout.addItem(self.verticalSpacer)

        self.internal_info_layout = QVBoxLayout()
        self.internal_info_layout.setSpacing(5)
        self.internal_info_layout.setObjectName(u"internal_info_layout")
        self.internal_info_layout.setContentsMargins(-1, 5, -1, 0)
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 26))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"padding-left:5px;")

        self.internal_info_layout.addWidget(self.label_24)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 0))
        self.label_8.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.label_8)

        self.de_date_purchase = QDateEdit(self.centralwidget)
        self.de_date_purchase.setObjectName(u"de_date_purchase")
        self.de_date_purchase.setMinimumSize(QSize(120, 26))
        self.de_date_purchase.setMaximumSize(QSize(120, 16777215))
        self.de_date_purchase.setCursor(QCursor(Qt.PointingHandCursor))
        self.de_date_purchase.setCalendarPopup(True)

        self.horizontalLayout_8.addWidget(self.de_date_purchase)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(140, 0))
        self.label_7.setMaximumSize(QSize(140, 16777215))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.le_place_purchase = QLineEdit(self.centralwidget)
        self.le_place_purchase.setObjectName(u"le_place_purchase")
        self.le_place_purchase.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_8.addWidget(self.le_place_purchase)


        self.internal_info_layout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, -1, -1, 0)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(120, 0))
        self.label_12.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_22.addWidget(self.label_12)

        self.market_price = QLineEdit(self.centralwidget)
        self.market_price.setObjectName(u"market_price")
        self.market_price.setMinimumSize(QSize(120, 26))
        self.market_price.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_22.addWidget(self.market_price)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(140, 0))
        self.label_10.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_22.addWidget(self.label_10)

        self.number_simcard = QLineEdit(self.centralwidget)
        self.number_simcard.setObjectName(u"number_simcard")
        sizePolicy.setHeightForWidth(self.number_simcard.sizePolicy().hasHeightForWidth())
        self.number_simcard.setSizePolicy(sizePolicy)
        self.number_simcard.setMinimumSize(QSize(220, 26))
        self.number_simcard.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_22.addWidget(self.number_simcard)


        self.internal_info_layout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, -1, -1, 0)
        self.frm_purchase_price = QFrame(self.centralwidget)
        self.frm_purchase_price.setObjectName(u"frm_purchase_price")
        self.frm_purchase_price.setEnabled(True)
        self.frm_purchase_price.setMinimumSize(QSize(245, 26))
        self.frm_purchase_price.setMaximumSize(QSize(245, 16777215))
        self.frm_purchase_price.setFrameShape(QFrame.NoFrame)
        self.frm_purchase_price.setFrameShadow(QFrame.Raised)
        self.frm_purchase_price.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.frm_purchase_price)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frm_purchase_price)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(120, 0))
        self.label_16.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_10.addWidget(self.label_16)

        self.purchase_price = QLineEdit(self.frm_purchase_price)
        self.purchase_price.setObjectName(u"purchase_price")
        self.purchase_price.setMinimumSize(QSize(120, 26))
        self.purchase_price.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_10.addWidget(self.purchase_price)


        self.horizontalLayout_23.addWidget(self.frm_purchase_price, 0, Qt.AlignLeft)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(140, 0))
        self.label_11.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_23.addWidget(self.label_11)

        self.gps_id = QLineEdit(self.centralwidget)
        self.gps_id.setObjectName(u"gps_id")
        sizePolicy.setHeightForWidth(self.gps_id.sizePolicy().hasHeightForWidth())
        self.gps_id.setSizePolicy(sizePolicy)
        self.gps_id.setMinimumSize(QSize(220, 26))
        self.gps_id.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_23.addWidget(self.gps_id)


        self.internal_info_layout.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, 0)
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(120, 0))
        self.label_21.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_7.addWidget(self.label_21)

        self.payment_category = QComboBox(self.centralwidget)
        self.payment_category.setObjectName(u"payment_category")
        self.payment_category.setMinimumSize(QSize(120, 26))
        self.payment_category.setMaximumSize(QSize(120, 16777215))
        self.payment_category.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.payment_category)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 0))
        self.label_22.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_7.addWidget(self.label_22)

        self.type_gps = QLineEdit(self.centralwidget)
        self.type_gps.setObjectName(u"type_gps")
        self.type_gps.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_7.addWidget(self.type_gps)


        self.internal_info_layout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 10, -1, 0)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(250, 0))
        self.label_18.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_12.addWidget(self.label_18)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setMinimumSize(QSize(140, 0))
        self.label_17.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_12.addWidget(self.label_17)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)


        self.internal_info_layout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(120, 0))
        self.label_13.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_13.addWidget(self.label_13)

        self.de_date_prev_to = QDateEdit(self.centralwidget)
        self.de_date_prev_to.setObjectName(u"de_date_prev_to")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.de_date_prev_to.sizePolicy().hasHeightForWidth())
        self.de_date_prev_to.setSizePolicy(sizePolicy3)
        self.de_date_prev_to.setMinimumSize(QSize(120, 26))
        self.de_date_prev_to.setMaximumSize(QSize(120, 16777215))
        self.de_date_prev_to.setCursor(QCursor(Qt.PointingHandCursor))
        self.de_date_prev_to.setCalendarPopup(True)

        self.horizontalLayout_13.addWidget(self.de_date_prev_to)

        self.le_prev_mileage = QLineEdit(self.centralwidget)
        self.le_prev_mileage.setObjectName(u"le_prev_mileage")
        self.le_prev_mileage.setMinimumSize(QSize(140, 26))
        self.le_prev_mileage.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_13.addWidget(self.le_prev_mileage)

        self.le_comment_prev_to = QLineEdit(self.centralwidget)
        self.le_comment_prev_to.setObjectName(u"le_comment_prev_to")
        self.le_comment_prev_to.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_13.addWidget(self.le_comment_prev_to)


        self.internal_info_layout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(120, 0))
        self.label_14.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_14.addWidget(self.label_14)

        self.de_date_next_to = QDateEdit(self.centralwidget)
        self.de_date_next_to.setObjectName(u"de_date_next_to")
        self.de_date_next_to.setMinimumSize(QSize(120, 26))
        self.de_date_next_to.setMaximumSize(QSize(120, 16777215))
        self.de_date_next_to.setCursor(QCursor(Qt.PointingHandCursor))
        self.de_date_next_to.setCalendarPopup(True)

        self.horizontalLayout_14.addWidget(self.de_date_next_to)

        self.le_next_mileage = QLineEdit(self.centralwidget)
        self.le_next_mileage.setObjectName(u"le_next_mileage")
        self.le_next_mileage.setMinimumSize(QSize(140, 26))
        self.le_next_mileage.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_14.addWidget(self.le_next_mileage)

        self.le_comment_next_to = QLineEdit(self.centralwidget)
        self.le_comment_next_to.setObjectName(u"le_comment_next_to")
        self.le_comment_next_to.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_14.addWidget(self.le_comment_next_to)


        self.internal_info_layout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(120, 0))
        self.label_15.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_15.addWidget(self.label_15, 0, Qt.AlignTop)

        self.te_comment_general = QTextEdit(self.centralwidget)
        self.te_comment_general.setObjectName(u"te_comment_general")
        self.te_comment_general.setMinimumSize(QSize(0, 70))
        self.te_comment_general.setMaximumSize(QSize(16777215, 70))

        self.horizontalLayout_15.addWidget(self.te_comment_general)


        self.internal_info_layout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_id_status = QLabel(self.centralwidget)
        self.lbl_id_status.setObjectName(u"lbl_id_status")
        self.lbl_id_status.setMinimumSize(QSize(0, 0))
        self.lbl_id_status.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.lbl_id_status)

        self.lbl_id_color = QLabel(self.centralwidget)
        self.lbl_id_color.setObjectName(u"lbl_id_color")
        self.lbl_id_color.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.lbl_id_color)

        self.lbl_filename = QLabel(self.centralwidget)
        self.lbl_filename.setObjectName(u"lbl_filename")
        self.lbl_filename.setEnabled(True)
        self.lbl_filename.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.lbl_filename)

        self.lbl_ts_id = QLabel(self.centralwidget)
        self.lbl_ts_id.setObjectName(u"lbl_ts_id")
        self.lbl_ts_id.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.lbl_ts_id)


        self.internal_info_layout.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.internal_info_layout.addItem(self.verticalSpacer_2)


        self.all_fields_layout.addLayout(self.internal_info_layout)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 40))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.btn_save)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(50, 0))
        self.label_23.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_16.addWidget(self.label_23)

        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.btn_cancel)


        self.all_fields_layout.addLayout(self.horizontalLayout_16)


        self.verticalLayout_4.addLayout(self.all_fields_layout)

        TransportCardWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TransportCardWindow)
        self.statusbar.setObjectName(u"statusbar")
        TransportCardWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TransportCardWindow)

        QMetaObject.connectSlotsByName(TransportCardWindow)
    # setupUi

    def retranslateUi(self, TransportCardWindow):
        TransportCardWindow.setWindowTitle(QCoreApplication.translate("TransportCardWindow", u"MainWindow", None))
        self.lbl_photo.setText("")
#if QT_CONFIG(tooltip)
        self.btn_select_status.setToolTip(QCoreApplication.translate("TransportCardWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0433\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_select_status.setText("")
#if QT_CONFIG(tooltip)
        self.btn_add_image.setToolTip(QCoreApplication.translate("TransportCardWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u043e\u0442\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_image.setText("")
#if QT_CONFIG(tooltip)
        self.btn_image_upload.setToolTip(QCoreApplication.translate("TransportCardWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0444\u043e\u0442\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.btn_image_upload.setText("")
        self.label_25.setText(QCoreApplication.translate("TransportCardWindow", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:", None))
        self.label.setText(QCoreApplication.translate("TransportCardWindow", u"\u0422\u0438\u043f \u0422\u0421", None))
        self.label_2.setText(QCoreApplication.translate("TransportCardWindow", u"\u041c\u0430\u0440\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("TransportCardWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_4.setText(QCoreApplication.translate("TransportCardWindow", u"\u041a\u0443\u0437\u043e\u0432 \u2116", None))
        self.label_9.setText(QCoreApplication.translate("TransportCardWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116", None))
        self.label_5.setText(QCoreApplication.translate("TransportCardWindow", u"\u0426\u0432\u0435\u0442", None))
        self.btn_select_color.setText("")
        self.label_6.setText(QCoreApplication.translate("TransportCardWindow", u"\u041e\u0431\u044a\u0451\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f", None))
        self.label_20.setText(QCoreApplication.translate("TransportCardWindow", u"\u043a\u0443\u0431. \u0441\u043c.", None))
        self.label_24.setText(QCoreApplication.translate("TransportCardWindow", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u044f\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("TransportCardWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.label_7.setText(QCoreApplication.translate("TransportCardWindow", u"\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u0442\u0435\u043d\u0438\u044f", None))
        self.label_12.setText(QCoreApplication.translate("TransportCardWindow", u"\u0420\u044b\u043d\u043e\u0447\u043d\u0430\u044f \u0446\u0435\u043d\u0430", None))
        self.label_10.setText(QCoreApplication.translate("TransportCardWindow", u"\u041d\u043e\u043c\u0435\u0440 SIM-\u043a\u0430\u0440\u0442\u044b", None))
        self.label_16.setText(QCoreApplication.translate("TransportCardWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430\u043a\u0443\u043f\u043a\u0438", None))
        self.label_11.setText(QCoreApplication.translate("TransportCardWindow", u"ID GPS", None))
        self.label_21.setText(QCoreApplication.translate("TransportCardWindow", u"\u0426\u0435\u043d\u043e\u0432\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_22.setText(QCoreApplication.translate("TransportCardWindow", u"\u0422\u0438\u043f GPS", None))
        self.label_18.setText("")
        self.label_17.setText(QCoreApplication.translate("TransportCardWindow", u"\u041f\u0440\u043e\u0431\u0435\u0433", None))
        self.label_19.setText(QCoreApplication.translate("TransportCardWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.label_13.setText(QCoreApplication.translate("TransportCardWindow", u"\u041f\u0440\u043e\u0448\u043b\u043e\u0435 \u0422\u041e", None))
        self.label_14.setText(QCoreApplication.translate("TransportCardWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u0422\u041e", None))
        self.label_15.setText(QCoreApplication.translate("TransportCardWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.lbl_id_status.setText("")
        self.lbl_id_color.setText("")
        self.lbl_filename.setText("")
        self.lbl_ts_id.setText("")
        self.btn_save.setText(QCoreApplication.translate("TransportCardWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_23.setText("")
        self.btn_cancel.setText(QCoreApplication.translate("TransportCardWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

