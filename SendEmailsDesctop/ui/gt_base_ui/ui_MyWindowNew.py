# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyWindowNewhgRfyR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc
import resource_rc

class Ui_WindowAllSettings(object):
    def setupUi(self, WindowAllSettings):
        if not WindowAllSettings.objectName():
            WindowAllSettings.setObjectName(u"WindowAllSettings")
        WindowAllSettings.resize(1621, 925)
        self.centralwidget = QWidget(WindowAllSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.widget_2)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 50))
        self.top_frame.setMaximumSize(QSize(16777215, 50))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.ledit_page = QLineEdit(self.top_frame)
        self.ledit_page.setObjectName(u"ledit_page")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_page.sizePolicy().hasHeightForWidth())
        self.ledit_page.setSizePolicy(sizePolicy)
        self.ledit_page.setMinimumSize(QSize(30, 30))
        self.ledit_page.setMaximumSize(QSize(0, 0))
        self.ledit_page.setCursor(QCursor(Qt.ArrowCursor))
        self.ledit_page.setMouseTracking(False)
        self.ledit_page.setAcceptDrops(False)
        self.ledit_page.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.ledit_page)

        self.main_header_frame = QLabel(self.top_frame)
        self.main_header_frame.setObjectName(u"main_header_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_header_frame.sizePolicy().hasHeightForWidth())
        self.main_header_frame.setSizePolicy(sizePolicy1)
        self.main_header_frame.setMinimumSize(QSize(0, 0))
        self.main_header_frame.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_header_frame.setFont(font)
        self.main_header_frame.setCursor(QCursor(Qt.SizeAllCursor))
        self.main_header_frame.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.main_header_frame)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 5, -1)
        self.btn_minimazed = QPushButton(self.top_frame)
        self.btn_minimazed.setObjectName(u"btn_minimazed")
        self.btn_minimazed.setMinimumSize(QSize(36, 36))
        self.btn_minimazed.setMaximumSize(QSize(36, 36))
        self.btn_minimazed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimazed.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(62, 90, 116);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimazed.setIcon(icon)
        self.btn_minimazed.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_minimazed)

        self.btn_maximazed = QPushButton(self.top_frame)
        self.btn_maximazed.setObjectName(u"btn_maximazed")
        self.btn_maximazed.setMinimumSize(QSize(36, 36))
        self.btn_maximazed.setMaximumSize(QSize(36, 36))
        self.btn_maximazed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximazed.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(62, 90, 116);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize-2_.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons/minimize-2_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_maximazed.setIcon(icon1)
        self.btn_maximazed.setIconSize(QSize(30, 30))
        self.btn_maximazed.setCheckable(True)
        self.btn_maximazed.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btn_maximazed)

        self.btn_close = QPushButton(self.top_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(36, 36))
        self.btn_close.setMaximumSize(QSize(36, 36))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(235, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout.addWidget(self.top_frame, 0, 0, 1, 3)

        self.central_frame = QFrame(self.widget_2)
        self.central_frame.setObjectName(u"central_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.central_frame.sizePolicy().hasHeightForWidth())
        self.central_frame.setSizePolicy(sizePolicy2)
        self.central_frame.setFrameShape(QFrame.NoFrame)
        self.central_frame.setFrameShadow(QFrame.Plain)
        self.central_frame.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.central_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.central_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 5, 0)
        self.btn_change = QPushButton(self.widget)
        self.btn_change.setObjectName(u"btn_change")
        self.btn_change.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/menu_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_change.setIcon(icon3)
        self.btn_change.setIconSize(QSize(30, 30))
        self.btn_change.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_change)

        self.horizontalSpacer = QSpacerItem(422, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_input = QLineEdit(self.widget)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.search_input)

        self.search_btn = QPushButton(self.widget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(0, 40))
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.search_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(422, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_user = QPushButton(self.widget)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/icons/user_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_user.setIcon(icon5)
        self.btn_user.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_user)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.central_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_add_email_operator = QWidget()
        self.page_add_email_operator.setObjectName(u"page_add_email_operator")
        self.horizontalLayout_9 = QHBoxLayout(self.page_add_email_operator)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.page_add_email_operator)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_operator = QLabel(self.frame_5)
        self.label_operator.setObjectName(u"label_operator")
        sizePolicy1.setHeightForWidth(self.label_operator.sizePolicy().hasHeightForWidth())
        self.label_operator.setSizePolicy(sizePolicy1)
        self.label_operator.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setKerning(True)
        self.label_operator.setFont(font1)
        self.label_operator.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_operator)

        self.cb_list_operators = QComboBox(self.frame_5)
        self.cb_list_operators.setObjectName(u"cb_list_operators")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cb_list_operators.sizePolicy().hasHeightForWidth())
        self.cb_list_operators.setSizePolicy(sizePolicy3)
        self.cb_list_operators.setMinimumSize(QSize(0, 45))
        self.cb_list_operators.setMaximumSize(QSize(16777215, 16777215))
        self.cb_list_operators.setFont(font1)
        self.cb_list_operators.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_list_operators.setStyleSheet(u"")
        self.cb_list_operators.setEditable(False)
        self.cb_list_operators.setMaxVisibleItems(20)
        self.cb_list_operators.setMinimumContentsLength(15)

        self.verticalLayout_6.addWidget(self.cb_list_operators)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_8)

        self.labelOperatorID = QLabel(self.frame_5)
        self.labelOperatorID.setObjectName(u"labelOperatorID")
        self.labelOperatorID.setMaximumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.labelOperatorID)

        self.btn_add_field_email_operator = QPushButton(self.frame_5)
        self.btn_add_field_email_operator.setObjectName(u"btn_add_field_email_operator")
        self.btn_add_field_email_operator.setMinimumSize(QSize(0, 50))
        self.btn_add_field_email_operator.setMaximumSize(QSize(16777215, 50))
        self.btn_add_field_email_operator.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_add_field_email_operator)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.scrollArea = QScrollArea(self.page_add_email_operator)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 587, 548))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.add_widget_layout = QVBoxLayout()
        self.add_widget_layout.setSpacing(0)
        self.add_widget_layout.setObjectName(u"add_widget_layout")
        self.add_widget_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.add_widget_layout.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_9.addLayout(self.add_widget_layout)

        self.verticalSpacer_3 = QSpacerItem(20, 453, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.btn_save_emails_operator = QPushButton(self.page_add_email_operator)
        self.btn_save_emails_operator.setObjectName(u"btn_save_emails_operator")
        sizePolicy1.setHeightForWidth(self.btn_save_emails_operator.sizePolicy().hasHeightForWidth())
        self.btn_save_emails_operator.setSizePolicy(sizePolicy1)
        self.btn_save_emails_operator.setMinimumSize(QSize(0, 45))
        self.btn_save_emails_operator.setMaximumSize(QSize(16777215, 45))
        self.btn_save_emails_operator.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_emails_operator.setIcon(icon6)
        self.btn_save_emails_operator.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.btn_save_emails_operator)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.frame_sp_operator = QFrame(self.page_add_email_operator)
        self.frame_sp_operator.setObjectName(u"frame_sp_operator")
        sizePolicy1.setHeightForWidth(self.frame_sp_operator.sizePolicy().hasHeightForWidth())
        self.frame_sp_operator.setSizePolicy(sizePolicy1)
        self.frame_sp_operator.setMinimumSize(QSize(750, 0))
        self.frame_sp_operator.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.frame_sp_operator.setFont(font2)
        self.frame_sp_operator.setStyleSheet(u"*{font: 12pt \"Arial\";}\n"
"\n"
"QTableView::item:selected { color:white; background:rgb(33, 47, 61); font-weight:900; }\n"
"QTableCornerButton::section { background-color:#232326; }\n"
"QHeaderView::section { color:white; background-color:rgb(33, 47, 61); }\n"
"\n"
"QScrollArea {\n"
"        border: none;\n"
"    }\n"
"\n"
"    QScrollBar {\n"
"        background: rgb(84, 122, 158);\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QScrollBar:horizontal {\n"
"        height: 13px;\n"
"    }\n"
"\n"
"    QScrollBar:vertical {\n"
"        width: 13px;\n"
"    }\n"
"\n"
"    QScrollBar::handle {\n"
"        background: rgb(84, 122, 158);\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal {\n"
"        height: 25px;\n"
"        min-width: 10px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        width: 25px;\n"
"        min-height: 10px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line {\n"
"        border: none;\n"
"        background: none;\n"
"    }\n"
"\n"
"    "
                        "QScrollBar::sub-line {\n"
"        border: none;\n"
"        background: none;\n"
"    }")
        self.frame_sp_operator.setFrameShape(QFrame.StyledPanel)
        self.frame_sp_operator.setFrameShadow(QFrame.Raised)
        self.frame_sp_operator.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_sp_operator)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_sp_operator = QScrollArea(self.frame_sp_operator)
        self.scrollArea_sp_operator.setObjectName(u"scrollArea_sp_operator")
        self.scrollArea_sp_operator.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 748, 760))
        self.verticalLayout_sp_operator = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_sp_operator.setObjectName(u"verticalLayout_sp_operator")
        self.verticalLayout_sp_operator.setContentsMargins(0, 0, 0, 0)
        self.frame_count_sp = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_count_sp.setObjectName(u"frame_count_sp")
        self.frame_count_sp.setStyleSheet(u"")
        self.frame_count_sp.setFrameShape(QFrame.StyledPanel)
        self.frame_count_sp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_count_sp)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 10)
        self.label = QLabel(self.frame_count_sp)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))
        self.label.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_7.addWidget(self.label)

        self.count_sp = QLabel(self.frame_count_sp)
        self.count_sp.setObjectName(u"count_sp")
        self.count_sp.setLineWidth(1)

        self.horizontalLayout_7.addWidget(self.count_sp)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.sp_operator = QTableWidget(self.frame_count_sp)
        if (self.sp_operator.columnCount() < 2):
            self.sp_operator.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.sp_operator.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sp_operator.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.sp_operator.setObjectName(u"sp_operator")
        self.sp_operator.setStyleSheet(u"")
        self.sp_operator.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.sp_operator.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sp_operator.setSortingEnabled(True)
        self.sp_operator.horizontalHeader().setProperty("showSortIndicator", False)
        self.sp_operator.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_11.addWidget(self.sp_operator)


        self.verticalLayout_sp_operator.addWidget(self.frame_count_sp)

        self.scrollArea_sp_operator.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_sp_operator)


        self.horizontalLayout_9.addWidget(self.frame_sp_operator)

        self.stackedWidget.addWidget(self.page_add_email_operator)
        self.page_add_emails_region = QWidget()
        self.page_add_emails_region.setObjectName(u"page_add_emails_region")
        self.label_5 = QLabel(self.page_add_emails_region)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 20, 151, 31))
        self.stackedWidget.addWidget(self.page_add_emails_region)
        self.page_pandas_html_load = QWidget()
        self.page_pandas_html_load.setObjectName(u"page_pandas_html_load")
        self.label_6 = QLabel(self.page_pandas_html_load)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(580, 20, 151, 31))
        self.stackedWidget.addWidget(self.page_pandas_html_load)
        self.page_log = QWidget()
        self.page_log.setObjectName(u"page_log")
        self.label_7 = QLabel(self.page_log)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(580, 10, 151, 31))
        self.stackedWidget.addWidget(self.page_log)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.central_frame, 1, 2, 1, 1)

        self.full_menu_frame = QFrame(self.widget_2)
        self.full_menu_frame.setObjectName(u"full_menu_frame")
        sizePolicy4.setHeightForWidth(self.full_menu_frame.sizePolicy().hasHeightForWidth())
        self.full_menu_frame.setSizePolicy(sizePolicy4)
        self.full_menu_frame.setStyleSheet(u"")
        self.full_menu_frame.setFrameShape(QFrame.NoFrame)
        self.full_menu_frame.setFrameShadow(QFrame.Plain)
        self.full_menu_frame.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label_2 = QLabel(self.full_menu_frame)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setMinimumSize(QSize(40, 40))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u":/icons/icons/git-pull-request.svg"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.logo_label_2)

        self.label_3 = QLabel(self.full_menu_frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(15)
        self.label_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_page_add_email_operator_2 = QPushButton(self.full_menu_frame)
        self.btn_page_add_email_operator_2.setObjectName(u"btn_page_add_email_operator_2")
        self.btn_page_add_email_operator_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/icons/mail_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_page_add_email_operator_2.setIcon(icon7)
        self.btn_page_add_email_operator_2.setIconSize(QSize(30, 30))
        self.btn_page_add_email_operator_2.setCheckable(True)
        self.btn_page_add_email_operator_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_page_add_email_operator_2)

        self.btn_page_add_emails_region_2 = QPushButton(self.full_menu_frame)
        self.btn_page_add_emails_region_2.setObjectName(u"btn_page_add_emails_region_2")
        self.btn_page_add_emails_region_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icons/icons/users_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_page_add_emails_region_2.setIcon(icon8)
        self.btn_page_add_emails_region_2.setIconSize(QSize(30, 30))
        self.btn_page_add_emails_region_2.setCheckable(True)
        self.btn_page_add_emails_region_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_page_add_emails_region_2)

        self.btn_page_pandas_html_load_2 = QPushButton(self.full_menu_frame)
        self.btn_page_pandas_html_load_2.setObjectName(u"btn_page_pandas_html_load_2")
        self.btn_page_pandas_html_load_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/icons/book-open_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_page_pandas_html_load_2.setIcon(icon9)
        self.btn_page_pandas_html_load_2.setIconSize(QSize(30, 30))
        self.btn_page_pandas_html_load_2.setCheckable(True)
        self.btn_page_pandas_html_load_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_page_pandas_html_load_2)

        self.btn_log_2 = QPushButton(self.full_menu_frame)
        self.btn_log_2.setObjectName(u"btn_log_2")
        self.btn_log_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/icons/eye_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_log_2.setIcon(icon10)
        self.btn_log_2.setIconSize(QSize(30, 30))
        self.btn_log_2.setCheckable(True)
        self.btn_log_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_log_2)

        self.btn_upload_all_emails_2 = QPushButton(self.full_menu_frame)
        self.btn_upload_all_emails_2.setObjectName(u"btn_upload_all_emails_2")
        self.btn_upload_all_emails_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/icons/upload_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_upload_all_emails_2.setIcon(icon11)
        self.btn_upload_all_emails_2.setIconSize(QSize(30, 30))
        self.btn_upload_all_emails_2.setCheckable(True)
        self.btn_upload_all_emails_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_upload_all_emails_2)

        self.btn_download_all_emails_2 = QPushButton(self.full_menu_frame)
        self.btn_download_all_emails_2.setObjectName(u"btn_download_all_emails_2")
        self.btn_download_all_emails_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icons/icons/download_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_download_all_emails_2.setIcon(icon12)
        self.btn_download_all_emails_2.setIconSize(QSize(30, 30))
        self.btn_download_all_emails_2.setCheckable(True)
        self.btn_download_all_emails_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_download_all_emails_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 527, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_settings__2 = QPushButton(self.full_menu_frame)
        self.btn_settings__2.setObjectName(u"btn_settings__2")
        self.btn_settings__2.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icons/icons/settings_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_settings__2.setIcon(icon13)
        self.btn_settings__2.setIconSize(QSize(30, 30))
        self.btn_settings__2.setCheckable(True)
        self.btn_settings__2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btn_settings__2, 0, Qt.AlignBottom)


        self.gridLayout.addWidget(self.full_menu_frame, 1, 1, 1, 1)

        self.icon_only_frame = QFrame(self.widget_2)
        self.icon_only_frame.setObjectName(u"icon_only_frame")
        sizePolicy4.setHeightForWidth(self.icon_only_frame.sizePolicy().hasHeightForWidth())
        self.icon_only_frame.setSizePolicy(sizePolicy4)
        self.icon_only_frame.setStyleSheet(u"")
        self.icon_only_frame.setFrameShape(QFrame.NoFrame)
        self.icon_only_frame.setFrameShadow(QFrame.Plain)
        self.icon_only_frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.icon_only_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logo_label_1 = QLabel(self.icon_only_frame)
        self.logo_label_1.setObjectName(u"logo_label_1")
        self.logo_label_1.setMinimumSize(QSize(40, 40))
        self.logo_label_1.setMaximumSize(QSize(40, 40))
        self.logo_label_1.setPixmap(QPixmap(u":/icons/icons/git-pull-request.svg"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.logo_label_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_page_add_email_operator_1 = QPushButton(self.icon_only_frame)
        self.btn_page_add_email_operator_1.setObjectName(u"btn_page_add_email_operator_1")
        self.btn_page_add_email_operator_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_add_email_operator_1.setIcon(icon7)
        self.btn_page_add_email_operator_1.setIconSize(QSize(30, 30))
        self.btn_page_add_email_operator_1.setCheckable(True)
        self.btn_page_add_email_operator_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_page_add_email_operator_1)

        self.btn_page_add_emails_region_1 = QPushButton(self.icon_only_frame)
        self.btn_page_add_emails_region_1.setObjectName(u"btn_page_add_emails_region_1")
        self.btn_page_add_emails_region_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_add_emails_region_1.setIcon(icon8)
        self.btn_page_add_emails_region_1.setIconSize(QSize(30, 30))
        self.btn_page_add_emails_region_1.setCheckable(True)
        self.btn_page_add_emails_region_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_page_add_emails_region_1)

        self.btn_page_pandas_html_load_1 = QPushButton(self.icon_only_frame)
        self.btn_page_pandas_html_load_1.setObjectName(u"btn_page_pandas_html_load_1")
        self.btn_page_pandas_html_load_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_pandas_html_load_1.setIcon(icon9)
        self.btn_page_pandas_html_load_1.setIconSize(QSize(30, 30))
        self.btn_page_pandas_html_load_1.setCheckable(True)
        self.btn_page_pandas_html_load_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_page_pandas_html_load_1)

        self.btn_log_1 = QPushButton(self.icon_only_frame)
        self.btn_log_1.setObjectName(u"btn_log_1")
        self.btn_log_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_log_1.setIcon(icon10)
        self.btn_log_1.setIconSize(QSize(30, 30))
        self.btn_log_1.setCheckable(True)
        self.btn_log_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_log_1)

        self.btn_upload_all_emails_1 = QPushButton(self.icon_only_frame)
        self.btn_upload_all_emails_1.setObjectName(u"btn_upload_all_emails_1")
        self.btn_upload_all_emails_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upload_all_emails_1.setIcon(icon11)
        self.btn_upload_all_emails_1.setIconSize(QSize(30, 30))
        self.btn_upload_all_emails_1.setCheckable(True)
        self.btn_upload_all_emails_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_upload_all_emails_1)

        self.btn_download_all_emails_1 = QPushButton(self.icon_only_frame)
        self.btn_download_all_emails_1.setObjectName(u"btn_download_all_emails_1")
        self.btn_download_all_emails_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_download_all_emails_1.setIcon(icon12)
        self.btn_download_all_emails_1.setIconSize(QSize(30, 30))
        self.btn_download_all_emails_1.setCheckable(True)
        self.btn_download_all_emails_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_download_all_emails_1)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 527, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_settings_1 = QPushButton(self.icon_only_frame)
        self.btn_settings_1.setObjectName(u"btn_settings_1")
        self.btn_settings_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_1.setIcon(icon13)
        self.btn_settings_1.setIconSize(QSize(30, 30))
        self.btn_settings_1.setCheckable(True)
        self.btn_settings_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_settings_1, 0, Qt.AlignBottom)


        self.gridLayout.addWidget(self.icon_only_frame, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.widget_2)

        WindowAllSettings.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(WindowAllSettings)
        self.statusbar.setObjectName(u"statusbar")
        WindowAllSettings.setStatusBar(self.statusbar)

        self.retranslateUi(WindowAllSettings)
        self.btn_page_add_email_operator_1.toggled.connect(self.btn_page_add_email_operator_2.setChecked)
        self.btn_page_add_email_operator_2.toggled.connect(self.btn_page_add_email_operator_1.setChecked)
        self.btn_page_add_emails_region_1.toggled.connect(self.btn_page_add_emails_region_2.setChecked)
        self.btn_page_add_emails_region_2.toggled.connect(self.btn_page_add_emails_region_1.setChecked)
        self.btn_page_pandas_html_load_1.toggled.connect(self.btn_page_pandas_html_load_2.setChecked)
        self.btn_page_pandas_html_load_2.toggled.connect(self.btn_page_pandas_html_load_1.setChecked)
        self.btn_log_1.toggled.connect(self.btn_log_2.setChecked)
        self.btn_log_2.toggled.connect(self.btn_log_1.setChecked)
        self.btn_log_2.toggled.connect(self.btn_log_1.setChecked)
        self.btn_upload_all_emails_1.toggled.connect(self.btn_upload_all_emails_2.setChecked)
        self.btn_upload_all_emails_2.toggled.connect(self.btn_upload_all_emails_1.setChecked)
        self.btn_upload_all_emails_2.toggled.connect(self.btn_upload_all_emails_1.setChecked)
        self.btn_download_all_emails_1.toggled.connect(self.btn_download_all_emails_2.setChecked)
        self.btn_download_all_emails_2.toggled.connect(self.btn_download_all_emails_1.setChecked)
        self.btn_settings_1.toggled.connect(self.btn_settings__2.setChecked)
        self.btn_settings__2.toggled.connect(self.btn_settings_1.setChecked)
        self.btn_change.toggled.connect(self.icon_only_frame.setVisible)
        self.btn_change.toggled.connect(self.full_menu_frame.setHidden)
        self.btn_close.clicked.connect(WindowAllSettings.close)
        self.btn_minimazed.clicked.connect(WindowAllSettings.showMinimized)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WindowAllSettings)
    # setupUi

    def retranslateUi(self, WindowAllSettings):
        WindowAllSettings.setWindowTitle("")
        self.ledit_page.setText(QCoreApplication.translate("WindowAllSettings", u"0", None))
        self.main_header_frame.setText(QCoreApplication.translate("WindowAllSettings", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430\u043c\u0438", None))
        self.btn_minimazed.setText("")
        self.btn_maximazed.setText("")
        self.btn_close.setText("")
        self.btn_change.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("WindowAllSettings", u"\u041d\u0430\u0439\u0442\u0438...", None))
        self.search_btn.setText("")
        self.btn_user.setText("")
        self.label_operator.setText(QCoreApplication.translate("WindowAllSettings", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430:", None))
        self.cb_list_operators.setCurrentText("")
        self.label_8.setText(QCoreApplication.translate("WindowAllSettings", u"\u0414\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430 \u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0432 \u043f\u043e\u043b\u0435 \u0432\u044b\u0448\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430.", None))
        self.labelOperatorID.setText("")
        self.btn_add_field_email_operator.setText(QCoreApplication.translate("WindowAllSettings", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c E-mail", None))
        self.btn_save_emails_operator.setText(QCoreApplication.translate("WindowAllSettings", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("WindowAllSettings", u"\u0412\u0441\u0435\u0433\u043e SP:", None))
        self.count_sp.setText("")
        ___qtablewidgetitem = self.sp_operator.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WindowAllSettings", u"SP", None));
        ___qtablewidgetitem1 = self.sp_operator.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WindowAllSettings", u"\u041c\u0435\u0441\u0442\u043e \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None));
        self.label_5.setText(QCoreApplication.translate("WindowAllSettings", u"E-mail \u0440\u0435\u0433\u0438\u043e\u043d\u043e\u0432", None))
        self.label_6.setText(QCoreApplication.translate("WindowAllSettings", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438", None))
        self.label_7.setText(QCoreApplication.translate("WindowAllSettings", u"\u041b\u043e\u0433", None))
        self.logo_label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("WindowAllSettings", u"\u041c\u0435\u043d\u044e", None))
        self.btn_page_add_email_operator_2.setText(QCoreApplication.translate("WindowAllSettings", u"E-mail \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u0432", None))
        self.btn_page_add_emails_region_2.setText(QCoreApplication.translate("WindowAllSettings", u"E-mail \u0440\u0435\u0433\u0438\u043e\u043d\u043e\u0432", None))
        self.btn_page_pandas_html_load_2.setText(QCoreApplication.translate("WindowAllSettings", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438", None))
        self.btn_log_2.setText(QCoreApplication.translate("WindowAllSettings", u"\u041b\u043e\u0433", None))
        self.btn_upload_all_emails_2.setText(QCoreApplication.translate("WindowAllSettings", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c E-mail \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u0432", None))
        self.btn_download_all_emails_2.setText(QCoreApplication.translate("WindowAllSettings", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c E-mail \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u0432", None))
        self.btn_settings__2.setText(QCoreApplication.translate("WindowAllSettings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.logo_label_1.setText("")
        self.btn_page_add_email_operator_1.setText("")
        self.btn_page_add_emails_region_1.setText("")
        self.btn_page_pandas_html_load_1.setText("")
        self.btn_log_1.setText("")
        self.btn_upload_all_emails_1.setText("")
        self.btn_download_all_emails_1.setText("")
        self.btn_settings_1.setText("")
    # retranslateUi

