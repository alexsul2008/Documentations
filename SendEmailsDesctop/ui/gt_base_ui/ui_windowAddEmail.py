# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowAddEmailsESgGt.ui'
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

class Ui_WindowAddEmailOperator(object):
    def setupUi(self, WindowAddEmailOperator):
        if not WindowAddEmailOperator.objectName():
            WindowAddEmailOperator.setObjectName(u"WindowAddEmailOperator")
        WindowAddEmailOperator.resize(1593, 1112)
        self.centralwidget = QWidget(WindowAddEmailOperator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_11 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.frame_central = QFrame(self.centralwidget)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setFrameShape(QFrame.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Raised)
        self.frame_central.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_central)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_top = QFrame(self.frame_central)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setEnabled(True)
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ledit_page = QLineEdit(self.frame_top)
        self.ledit_page.setObjectName(u"ledit_page")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_page.sizePolicy().hasHeightForWidth())
        self.ledit_page.setSizePolicy(sizePolicy)
        self.ledit_page.setMinimumSize(QSize(0, 0))
        self.ledit_page.setMaximumSize(QSize(0, 0))
        self.ledit_page.setCursor(QCursor(Qt.ArrowCursor))
        self.ledit_page.setMouseTracking(False)
        self.ledit_page.setAcceptDrops(False)
        self.ledit_page.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.ledit_page, 0, Qt.AlignTop)

        self.ledit_statistics_page = QLineEdit(self.frame_top)
        self.ledit_statistics_page.setObjectName(u"ledit_statistics_page")
        sizePolicy.setHeightForWidth(self.ledit_statistics_page.sizePolicy().hasHeightForWidth())
        self.ledit_statistics_page.setSizePolicy(sizePolicy)
        self.ledit_statistics_page.setMinimumSize(QSize(0, 0))
        self.ledit_statistics_page.setMaximumSize(QSize(0, 0))
        self.ledit_statistics_page.setCursor(QCursor(Qt.ArrowCursor))
        self.ledit_statistics_page.setMouseTracking(False)
        self.ledit_statistics_page.setAcceptDrops(False)
        self.ledit_statistics_page.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.ledit_statistics_page)

        self.main_header_frame = QLabel(self.frame_top)
        self.main_header_frame.setObjectName(u"main_header_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_header_frame.sizePolicy().hasHeightForWidth())
        self.main_header_frame.setSizePolicy(sizePolicy1)
        self.main_header_frame.setMinimumSize(QSize(0, 40))
        self.main_header_frame.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_header_frame.setFont(font)
        self.main_header_frame.setCursor(QCursor(Qt.SizeAllCursor))
        self.main_header_frame.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.main_header_frame)

        self.frame_2 = QFrame(self.frame_top)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimazed = QPushButton(self.frame_2)
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

        self.btn_maximazed = QPushButton(self.frame_2)
        self.btn_maximazed.setObjectName(u"btn_maximazed")
        self.btn_maximazed.setMinimumSize(QSize(36, 36))
        self.btn_maximazed.setMaximumSize(QSize(36, 36))
        self.btn_maximazed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximazed.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(62, 90, 116);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize-2_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximazed.setIcon(icon1)
        self.btn_maximazed.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_maximazed)

        self.btn_close = QPushButton(self.frame_2)
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


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.top_statistics_frame = QFrame(self.frame_central)
        self.top_statistics_frame.setObjectName(u"top_statistics_frame")
        sizePolicy.setHeightForWidth(self.top_statistics_frame.sizePolicy().hasHeightForWidth())
        self.top_statistics_frame.setSizePolicy(sizePolicy)
        self.top_statistics_frame.setMinimumSize(QSize(0, 100))
        self.top_statistics_Layout = QHBoxLayout(self.top_statistics_frame)
        self.top_statistics_Layout.setSpacing(20)
        self.top_statistics_Layout.setObjectName(u"top_statistics_Layout")
        self.top_statistics_Layout.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_2 = QSpacerItem(525, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_statistics_Layout.addItem(self.horizontalSpacer_2)

        self.stat_inc_grb = QGroupBox(self.top_statistics_frame)
        self.stat_inc_grb.setObjectName(u"stat_inc_grb")
        self.horizontalLayout_28 = QHBoxLayout(self.stat_inc_grb)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(15, 5, 15, 5)
        self.all_inc_frm = QFrame(self.stat_inc_grb)
        self.all_inc_frm.setObjectName(u"all_inc_frm")
        self.all_inc_frm.setCursor(QCursor(Qt.PointingHandCursor))
        self.all_inc_frm.setLineWidth(0)
        self.horizontalLayout_21 = QHBoxLayout(self.all_inc_frm)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.all_inc_frm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setLineWidth(0)
        self.label_8.setPixmap(QPixmap(u":/icons/icons/trello_.svg"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_8)

        self.frame_31 = QFrame(self.all_inc_frm)
        self.frame_31.setObjectName(u"frame_31")
        self.verticalLayout_53 = QVBoxLayout(self.frame_31)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_31)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_53.addWidget(self.label_19)

        self.total_inc_lbl = QLabel(self.frame_31)
        self.total_inc_lbl.setObjectName(u"total_inc_lbl")

        self.verticalLayout_53.addWidget(self.total_inc_lbl)


        self.horizontalLayout_21.addWidget(self.frame_31, 0, Qt.AlignTop)


        self.horizontalLayout_28.addWidget(self.all_inc_frm)


        self.top_statistics_Layout.addWidget(self.stat_inc_grb, 0, Qt.AlignVCenter)

        self.stat_operators_grb = QGroupBox(self.top_statistics_frame)
        self.stat_operators_grb.setObjectName(u"stat_operators_grb")
        self.horizontalLayout_27 = QHBoxLayout(self.stat_operators_grb)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(15, 5, 15, 5)
        self.all_operators_frm = QFrame(self.stat_operators_grb)
        self.all_operators_frm.setObjectName(u"all_operators_frm")
        self.all_operators_frm.setCursor(QCursor(Qt.PointingHandCursor))
        self.all_operators_frm.setLineWidth(0)
        self.horizontalLayout_22 = QHBoxLayout(self.all_operators_frm)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.all_operators_frm)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(40, 40))
        self.label_21.setMaximumSize(QSize(40, 40))
        self.label_21.setLineWidth(0)
        self.label_21.setPixmap(QPixmap(u":/icons/icons/folder_.svg"))
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_21)

        self.frame_24 = QFrame(self.all_operators_frm)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setLineWidth(0)
        self.verticalLayout_54 = QVBoxLayout(self.frame_24)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_24)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_54.addWidget(self.label_22)

        self.operators_total_lbl = QLabel(self.frame_24)
        self.operators_total_lbl.setObjectName(u"operators_total_lbl")

        self.verticalLayout_54.addWidget(self.operators_total_lbl, 0, Qt.AlignTop)


        self.horizontalLayout_22.addWidget(self.frame_24, 0, Qt.AlignTop)


        self.horizontalLayout_27.addWidget(self.all_operators_frm)

        self.operators_with_emails = QFrame(self.stat_operators_grb)
        self.operators_with_emails.setObjectName(u"operators_with_emails")
        self.operators_with_emails.setCursor(QCursor(Qt.PointingHandCursor))
        self.operators_with_emails.setLineWidth(0)
        self.horizontalLayout_23 = QHBoxLayout(self.operators_with_emails)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.operators_with_emails)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(40, 40))
        self.label_25.setMaximumSize(QSize(40, 40))
        self.label_25.setLineWidth(0)
        self.label_25.setPixmap(QPixmap(u":/icons/icons/folder-plus_.svg"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_25)

        self.frame_30 = QFrame(self.operators_with_emails)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setLineWidth(0)
        self.verticalLayout_55 = QVBoxLayout(self.frame_30)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_30)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_55.addWidget(self.label_29)

        self.operators_total_emails_lbl = QLabel(self.frame_30)
        self.operators_total_emails_lbl.setObjectName(u"operators_total_emails_lbl")

        self.verticalLayout_55.addWidget(self.operators_total_emails_lbl)


        self.horizontalLayout_23.addWidget(self.frame_30, 0, Qt.AlignTop)


        self.horizontalLayout_27.addWidget(self.operators_with_emails)

        self.operators_without_emails = QFrame(self.stat_operators_grb)
        self.operators_without_emails.setObjectName(u"operators_without_emails")
        self.operators_without_emails.setCursor(QCursor(Qt.PointingHandCursor))
        self.operators_without_emails.setLineWidth(0)
        self.horizontalLayout_26 = QHBoxLayout(self.operators_without_emails)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.operators_without_emails)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(40, 40))
        self.label_30.setMaximumSize(QSize(40, 40))
        self.label_30.setLineWidth(0)
        self.label_30.setPixmap(QPixmap(u":/icons/icons/folder-minus_.svg"))
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_30)

        self.frame_29 = QFrame(self.operators_without_emails)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setLineWidth(0)
        self.verticalLayout_56 = QVBoxLayout(self.frame_29)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_29)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_56.addWidget(self.label_31)

        self.operators_total_out_emails_lbl = QLabel(self.frame_29)
        self.operators_total_out_emails_lbl.setObjectName(u"operators_total_out_emails_lbl")

        self.verticalLayout_56.addWidget(self.operators_total_out_emails_lbl)


        self.horizontalLayout_26.addWidget(self.frame_29, 0, Qt.AlignTop)


        self.horizontalLayout_27.addWidget(self.operators_without_emails)


        self.top_statistics_Layout.addWidget(self.stat_operators_grb, 0, Qt.AlignVCenter)

        self.stat_users_grb = QGroupBox(self.top_statistics_frame)
        self.stat_users_grb.setObjectName(u"stat_users_grb")
        self.horizontalLayout_30 = QHBoxLayout(self.stat_users_grb)
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(15, 5, 15, 5)
        self.users_frm = QFrame(self.stat_users_grb)
        self.users_frm.setObjectName(u"users_frm")
        self.users_frm.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_frm.setLineWidth(0)
        self.horizontalLayout_29 = QHBoxLayout(self.users_frm)
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.users_frm)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(40, 40))
        self.label_27.setMaximumSize(QSize(40, 40))
        self.label_27.setLineWidth(0)
        self.label_27.setPixmap(QPixmap(u":/icons/icons/users_.svg"))
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_27)

        self.frame_32 = QFrame(self.users_frm)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setLineWidth(0)
        self.verticalLayout_57 = QVBoxLayout(self.frame_32)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_32)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_57.addWidget(self.label_32)

        self.users_total_lbl = QLabel(self.frame_32)
        self.users_total_lbl.setObjectName(u"users_total_lbl")

        self.verticalLayout_57.addWidget(self.users_total_lbl)


        self.horizontalLayout_29.addWidget(self.frame_32, 0, Qt.AlignTop)


        self.horizontalLayout_30.addWidget(self.users_frm)


        self.top_statistics_Layout.addWidget(self.stat_users_grb, 0, Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(524, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_statistics_Layout.addItem(self.horizontalSpacer_3)

        self.frame_25 = QFrame(self.top_statistics_frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(50, 50))
        self.frame_25.setMaximumSize(QSize(50, 16777215))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Plain)
        self.frame_25.setLineWidth(0)
        self.verticalLayout_60 = QVBoxLayout(self.frame_25)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.loading_lbl = QLabel(self.frame_25)
        self.loading_lbl.setObjectName(u"loading_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loading_lbl.sizePolicy().hasHeightForWidth())
        self.loading_lbl.setSizePolicy(sizePolicy2)
        self.loading_lbl.setMinimumSize(QSize(50, 50))
        self.loading_lbl.setMaximumSize(QSize(50, 50))
        self.loading_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_60.addWidget(self.loading_lbl)


        self.top_statistics_Layout.addWidget(self.frame_25, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.top_statistics_frame)

        self.frame_23 = QFrame(self.frame_central)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 5, 5)
        self.toggle_menu_btn = QPushButton(self.frame_23)
        self.toggle_menu_btn.setObjectName(u"toggle_menu_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toggle_menu_btn.sizePolicy().hasHeightForWidth())
        self.toggle_menu_btn.setSizePolicy(sizePolicy3)
        self.toggle_menu_btn.setMinimumSize(QSize(40, 40))
        self.toggle_menu_btn.setMaximumSize(QSize(40, 40))
        self.toggle_menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x_.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/menu_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.toggle_menu_btn.setIcon(icon3)
        self.toggle_menu_btn.setIconSize(QSize(30, 30))
        self.toggle_menu_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.toggle_menu_btn)

        self.horizontalSpacer = QSpacerItem(1528, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_23)

        self.main_frame = QFrame(self.frame_central)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Plain)
        self.main_frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.main_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        sizePolicy.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.menu_frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_only_icons = QFrame(self.menu_frame)
        self.frame_only_icons.setObjectName(u"frame_only_icons")
        self.frame_only_icons.setMinimumSize(QSize(48, 0))
        self.frame_only_icons.setMaximumSize(QSize(48, 16777215))
        self.frame_only_icons.setFrameShape(QFrame.NoFrame)
        self.frame_only_icons.setFrameShadow(QFrame.Plain)
        self.frame_only_icons.setLineWidth(0)
        self.verticalLayout_33 = QVBoxLayout(self.frame_only_icons)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.btn_page_add_email_operator_2 = QPushButton(self.frame_only_icons)
        self.btn_page_add_email_operator_2.setObjectName(u"btn_page_add_email_operator_2")
        self.btn_page_add_email_operator_2.setMinimumSize(QSize(0, 48))
        self.btn_page_add_email_operator_2.setMaximumSize(QSize(16777215, 16777215))
        self.btn_page_add_email_operator_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icons/send_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_page_add_email_operator_2.setIcon(icon4)
        self.btn_page_add_email_operator_2.setIconSize(QSize(30, 30))
        self.btn_page_add_email_operator_2.setCheckable(True)
        self.btn_page_add_email_operator_2.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.btn_page_add_email_operator_2)

        self.btn_page_add_emails_region_2 = QPushButton(self.frame_only_icons)
        self.btn_page_add_emails_region_2.setObjectName(u"btn_page_add_emails_region_2")
        self.btn_page_add_emails_region_2.setMinimumSize(QSize(0, 48))
        self.btn_page_add_emails_region_2.setMaximumSize(QSize(16777215, 16777215))
        self.btn_page_add_emails_region_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/icons/users_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_page_add_emails_region_2.setIcon(icon5)
        self.btn_page_add_emails_region_2.setIconSize(QSize(30, 30))
        self.btn_page_add_emails_region_2.setCheckable(True)
        self.btn_page_add_emails_region_2.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.btn_page_add_emails_region_2)

        self.btn_page_pandas_html_load_2 = QPushButton(self.frame_only_icons)
        self.btn_page_pandas_html_load_2.setObjectName(u"btn_page_pandas_html_load_2")
        self.btn_page_pandas_html_load_2.setMinimumSize(QSize(0, 48))
        self.btn_page_pandas_html_load_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/icons/book-open_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_page_pandas_html_load_2.setIcon(icon6)
        self.btn_page_pandas_html_load_2.setIconSize(QSize(30, 30))
        self.btn_page_pandas_html_load_2.setCheckable(True)
        self.btn_page_pandas_html_load_2.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.btn_page_pandas_html_load_2)

        self.admin__btn_log_2 = QPushButton(self.frame_only_icons)
        self.admin__btn_log_2.setObjectName(u"admin__btn_log_2")
        self.admin__btn_log_2.setMinimumSize(QSize(0, 48))
        self.admin__btn_log_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/icons/eye_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.admin__btn_log_2.setIcon(icon7)
        self.admin__btn_log_2.setIconSize(QSize(30, 30))
        self.admin__btn_log_2.setCheckable(True)
        self.admin__btn_log_2.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.admin__btn_log_2)

        self.admin__btn_upload_all_emails_2 = QPushButton(self.frame_only_icons)
        self.admin__btn_upload_all_emails_2.setObjectName(u"admin__btn_upload_all_emails_2")
        self.admin__btn_upload_all_emails_2.setMinimumSize(QSize(0, 48))
        self.admin__btn_upload_all_emails_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icons/icons/upload_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.admin__btn_upload_all_emails_2.setIcon(icon8)
        self.admin__btn_upload_all_emails_2.setIconSize(QSize(30, 30))
        self.admin__btn_upload_all_emails_2.setCheckable(True)
        self.admin__btn_upload_all_emails_2.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.admin__btn_upload_all_emails_2)

        self.admin__btn_download_all_emails_2 = QPushButton(self.frame_only_icons)
        self.admin__btn_download_all_emails_2.setObjectName(u"admin__btn_download_all_emails_2")
        self.admin__btn_download_all_emails_2.setMinimumSize(QSize(0, 48))
        self.admin__btn_download_all_emails_2.setSizeIncrement(QSize(0, 0))
        self.admin__btn_download_all_emails_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/icons/download_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.admin__btn_download_all_emails_2.setIcon(icon9)
        self.admin__btn_download_all_emails_2.setIconSize(QSize(30, 30))
        self.admin__btn_download_all_emails_2.setCheckable(True)
        self.admin__btn_download_all_emails_2.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.admin__btn_download_all_emails_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_5)

        self.admin__btn_statistics_2 = QPushButton(self.frame_only_icons)
        self.admin__btn_statistics_2.setObjectName(u"admin__btn_statistics_2")
        self.admin__btn_statistics_2.setMinimumSize(QSize(0, 48))
        self.admin__btn_statistics_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/icons/activity_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.admin__btn_statistics_2.setIcon(icon10)
        self.admin__btn_statistics_2.setIconSize(QSize(30, 30))
        self.admin__btn_statistics_2.setCheckable(True)
        self.admin__btn_statistics_2.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.admin__btn_statistics_2)


        self.horizontalLayout_17.addWidget(self.frame_only_icons)

        self.frame_full_menu = QFrame(self.menu_frame)
        self.frame_full_menu.setObjectName(u"frame_full_menu")
        sizePolicy.setHeightForWidth(self.frame_full_menu.sizePolicy().hasHeightForWidth())
        self.frame_full_menu.setSizePolicy(sizePolicy)
        self.frame_full_menu.setMinimumSize(QSize(50, 0))
        self.frame_full_menu.setMaximumSize(QSize(280, 16777215))
        self.frame_full_menu.setStyleSheet(u"")
        self.frame_full_menu.setFrameShape(QFrame.NoFrame)
        self.frame_full_menu.setFrameShadow(QFrame.Plain)
        self.frame_full_menu.setLineWidth(0)
        self.verticalLayout_34 = QVBoxLayout(self.frame_full_menu)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.btn_page_add_email_operator = QPushButton(self.frame_full_menu)
        self.btn_page_add_email_operator.setObjectName(u"btn_page_add_email_operator")
        sizePolicy1.setHeightForWidth(self.btn_page_add_email_operator.sizePolicy().hasHeightForWidth())
        self.btn_page_add_email_operator.setSizePolicy(sizePolicy1)
        self.btn_page_add_email_operator.setMinimumSize(QSize(0, 48))
        self.btn_page_add_email_operator.setMaximumSize(QSize(16777215, 48))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.btn_page_add_email_operator.setFont(font1)
        self.btn_page_add_email_operator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_add_email_operator.setStyleSheet(u"")
        self.btn_page_add_email_operator.setIcon(icon4)
        self.btn_page_add_email_operator.setIconSize(QSize(30, 30))
        self.btn_page_add_email_operator.setCheckable(True)
        self.btn_page_add_email_operator.setAutoExclusive(True)
        self.btn_page_add_email_operator.setAutoDefault(True)
        self.btn_page_add_email_operator.setFlat(False)

        self.verticalLayout_34.addWidget(self.btn_page_add_email_operator)

        self.btn_page_add_emails_region = QPushButton(self.frame_full_menu)
        self.btn_page_add_emails_region.setObjectName(u"btn_page_add_emails_region")
        sizePolicy1.setHeightForWidth(self.btn_page_add_emails_region.sizePolicy().hasHeightForWidth())
        self.btn_page_add_emails_region.setSizePolicy(sizePolicy1)
        self.btn_page_add_emails_region.setMinimumSize(QSize(0, 48))
        self.btn_page_add_emails_region.setMaximumSize(QSize(16777215, 48))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        self.btn_page_add_emails_region.setFont(font2)
        self.btn_page_add_emails_region.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_add_emails_region.setIcon(icon5)
        self.btn_page_add_emails_region.setIconSize(QSize(30, 30))
        self.btn_page_add_emails_region.setCheckable(True)
        self.btn_page_add_emails_region.setAutoExclusive(True)

        self.verticalLayout_34.addWidget(self.btn_page_add_emails_region)

        self.btn_page_pandas_html_load = QPushButton(self.frame_full_menu)
        self.btn_page_pandas_html_load.setObjectName(u"btn_page_pandas_html_load")
        sizePolicy1.setHeightForWidth(self.btn_page_pandas_html_load.sizePolicy().hasHeightForWidth())
        self.btn_page_pandas_html_load.setSizePolicy(sizePolicy1)
        self.btn_page_pandas_html_load.setMinimumSize(QSize(0, 48))
        self.btn_page_pandas_html_load.setMaximumSize(QSize(16777215, 48))
        self.btn_page_pandas_html_load.setFont(font1)
        self.btn_page_pandas_html_load.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_pandas_html_load.setStyleSheet(u"")
        self.btn_page_pandas_html_load.setIcon(icon6)
        self.btn_page_pandas_html_load.setIconSize(QSize(30, 30))
        self.btn_page_pandas_html_load.setCheckable(True)
        self.btn_page_pandas_html_load.setAutoExclusive(True)

        self.verticalLayout_34.addWidget(self.btn_page_pandas_html_load)

        self.admin__btn_log = QPushButton(self.frame_full_menu)
        self.admin__btn_log.setObjectName(u"admin__btn_log")
        sizePolicy1.setHeightForWidth(self.admin__btn_log.sizePolicy().hasHeightForWidth())
        self.admin__btn_log.setSizePolicy(sizePolicy1)
        self.admin__btn_log.setMinimumSize(QSize(0, 48))
        self.admin__btn_log.setMaximumSize(QSize(16777215, 48))
        self.admin__btn_log.setFont(font1)
        self.admin__btn_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin__btn_log.setStyleSheet(u"")
        self.admin__btn_log.setIcon(icon7)
        self.admin__btn_log.setIconSize(QSize(30, 30))
        self.admin__btn_log.setCheckable(True)
        self.admin__btn_log.setAutoExclusive(True)
        self.admin__btn_log.setAutoDefault(True)

        self.verticalLayout_34.addWidget(self.admin__btn_log)

        self.admin__btn_upload_all_emails = QPushButton(self.frame_full_menu)
        self.admin__btn_upload_all_emails.setObjectName(u"admin__btn_upload_all_emails")
        sizePolicy1.setHeightForWidth(self.admin__btn_upload_all_emails.sizePolicy().hasHeightForWidth())
        self.admin__btn_upload_all_emails.setSizePolicy(sizePolicy1)
        self.admin__btn_upload_all_emails.setMinimumSize(QSize(0, 48))
        self.admin__btn_upload_all_emails.setMaximumSize(QSize(16777215, 48))
        self.admin__btn_upload_all_emails.setFont(font1)
        self.admin__btn_upload_all_emails.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin__btn_upload_all_emails.setStyleSheet(u"")
        self.admin__btn_upload_all_emails.setIcon(icon8)
        self.admin__btn_upload_all_emails.setIconSize(QSize(30, 30))
        self.admin__btn_upload_all_emails.setCheckable(True)
        self.admin__btn_upload_all_emails.setAutoExclusive(True)

        self.verticalLayout_34.addWidget(self.admin__btn_upload_all_emails)

        self.admin__btn_download_all_emails = QPushButton(self.frame_full_menu)
        self.admin__btn_download_all_emails.setObjectName(u"admin__btn_download_all_emails")
        sizePolicy1.setHeightForWidth(self.admin__btn_download_all_emails.sizePolicy().hasHeightForWidth())
        self.admin__btn_download_all_emails.setSizePolicy(sizePolicy1)
        self.admin__btn_download_all_emails.setMinimumSize(QSize(0, 48))
        self.admin__btn_download_all_emails.setMaximumSize(QSize(16777215, 48))
        self.admin__btn_download_all_emails.setFont(font1)
        self.admin__btn_download_all_emails.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin__btn_download_all_emails.setStyleSheet(u"")
        self.admin__btn_download_all_emails.setIcon(icon9)
        self.admin__btn_download_all_emails.setIconSize(QSize(30, 30))
        self.admin__btn_download_all_emails.setCheckable(True)
        self.admin__btn_download_all_emails.setAutoExclusive(True)

        self.verticalLayout_34.addWidget(self.admin__btn_download_all_emails)

        self.verticalSpacer_2 = QSpacerItem(20, 560, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_2)

        self.admin__btn_statistics = QPushButton(self.frame_full_menu)
        self.admin__btn_statistics.setObjectName(u"admin__btn_statistics")
        self.admin__btn_statistics.setMinimumSize(QSize(0, 48))
        self.admin__btn_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin__btn_statistics.setIcon(icon10)
        self.admin__btn_statistics.setIconSize(QSize(30, 30))
        self.admin__btn_statistics.setCheckable(True)
        self.admin__btn_statistics.setAutoExclusive(True)

        self.verticalLayout_34.addWidget(self.admin__btn_statistics)


        self.horizontalLayout_17.addWidget(self.frame_full_menu)


        self.horizontalLayout.addWidget(self.menu_frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.main_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Plain)
        self.frame_12.setLineWidth(0)
        self.verticalLayout_24 = QVBoxLayout(self.frame_12)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frm_status_progress = QFrame(self.frame_12)
        self.frm_status_progress.setObjectName(u"frm_status_progress")
        sizePolicy.setHeightForWidth(self.frm_status_progress.sizePolicy().hasHeightForWidth())
        self.frm_status_progress.setSizePolicy(sizePolicy)
        self.frm_status_progress.setFrameShape(QFrame.NoFrame)
        self.frm_status_progress.setFrameShadow(QFrame.Plain)
        self.frm_status_progress.setLineWidth(0)
        self.verticalLayout_25 = QVBoxLayout(self.frm_status_progress)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frm_status_progress)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setKerning(True)
        self.stackedWidget.setFont(font3)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page_add_email_operator = QWidget()
        self.page_add_email_operator.setObjectName(u"page_add_email_operator")
        self.page_add_email_operator.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.page_add_email_operator)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 5)
        self.frame_5 = QFrame(self.page_add_email_operator)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(550, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.label_operator = QLabel(self.frame_6)
        self.label_operator.setObjectName(u"label_operator")
        sizePolicy1.setHeightForWidth(self.label_operator.sizePolicy().hasHeightForWidth())
        self.label_operator.setSizePolicy(sizePolicy1)
        self.label_operator.setMinimumSize(QSize(0, 43))
        self.label_operator.setMaximumSize(QSize(16777215, 16777215))
        self.label_operator.setFont(font3)
        self.label_operator.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_operator)

        self.cb_list_operators = QComboBox(self.frame_6)
        self.cb_list_operators.setObjectName(u"cb_list_operators")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cb_list_operators.sizePolicy().hasHeightForWidth())
        self.cb_list_operators.setSizePolicy(sizePolicy4)
        self.cb_list_operators.setMinimumSize(QSize(0, 45))
        self.cb_list_operators.setMaximumSize(QSize(16777215, 16777215))
        self.cb_list_operators.setFont(font3)
        self.cb_list_operators.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_list_operators.setStyleSheet(u"")
        self.cb_list_operators.setEditable(False)
        self.cb_list_operators.setMaxVisibleItems(20)
        self.cb_list_operators.setMinimumContentsLength(15)

        self.verticalLayout_4.addWidget(self.cb_list_operators)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label_4)

        self.labelOperatorID = QLabel(self.frame_6)
        self.labelOperatorID.setObjectName(u"labelOperatorID")
        self.labelOperatorID.setMaximumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.labelOperatorID)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_add_field_email_operator = QPushButton(self.frame_4)
        self.btn_add_field_email_operator.setObjectName(u"btn_add_field_email_operator")
        self.btn_add_field_email_operator.setMinimumSize(QSize(0, 50))
        self.btn_add_field_email_operator.setMaximumSize(QSize(16777215, 50))
        self.btn_add_field_email_operator.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.btn_add_field_email_operator)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.page_add_email_operator)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(550, 16777215))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(1)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 5, 0, 0)
        self.btn_save_emails_operator = QPushButton(self.frame_8)
        self.btn_save_emails_operator.setObjectName(u"btn_save_emails_operator")
        sizePolicy1.setHeightForWidth(self.btn_save_emails_operator.sizePolicy().hasHeightForWidth())
        self.btn_save_emails_operator.setSizePolicy(sizePolicy1)
        self.btn_save_emails_operator.setMinimumSize(QSize(0, 45))
        self.btn_save_emails_operator.setMaximumSize(QSize(16777215, 45))
        self.btn_save_emails_operator.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_emails_operator.setIcon(icon11)
        self.btn_save_emails_operator.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.btn_save_emails_operator)


        self.gridLayout_2.addWidget(self.frame_8, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.page_add_email_operator)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 548, 573))
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

        self.verticalSpacer = QSpacerItem(20, 453, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.frame_sp_operator = QFrame(self.page_add_email_operator)
        self.frame_sp_operator.setObjectName(u"frame_sp_operator")
        sizePolicy1.setHeightForWidth(self.frame_sp_operator.sizePolicy().hasHeightForWidth())
        self.frame_sp_operator.setSizePolicy(sizePolicy1)
        self.frame_sp_operator.setMinimumSize(QSize(650, 0))
        self.frame_sp_operator.setMaximumSize(QSize(16777215, 16777215))
        self.frame_sp_operator.setFont(font1)
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
        self.verticalLayout_6 = QVBoxLayout(self.frame_sp_operator)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.scrollArea_sp_operator = QScrollArea(self.frame_sp_operator)
        self.scrollArea_sp_operator.setObjectName(u"scrollArea_sp_operator")
        self.scrollArea_sp_operator.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 695, 834))
        self.verticalLayout_sp_operator = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_sp_operator.setObjectName(u"verticalLayout_sp_operator")
        self.verticalLayout_sp_operator.setContentsMargins(0, 0, 0, 0)
        self.frame_count_sp = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_count_sp.setObjectName(u"frame_count_sp")
        self.frame_count_sp.setStyleSheet(u"")
        self.frame_count_sp.setFrameShape(QFrame.StyledPanel)
        self.frame_count_sp.setFrameShadow(QFrame.Raised)
        self.frame_count_sp.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.frame_count_sp)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_count_sp)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.label_44 = QLabel(self.frame_10)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 35))
        self.label_44.setMaximumSize(QSize(128, 16777215))

        self.horizontalLayout_6.addWidget(self.label_44)

        self.lbl_operator = QLabel(self.frame_10)
        self.lbl_operator.setObjectName(u"lbl_operator")
        sizePolicy1.setHeightForWidth(self.lbl_operator.sizePolicy().hasHeightForWidth())
        self.lbl_operator.setSizePolicy(sizePolicy1)
        self.lbl_operator.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_6.addWidget(self.lbl_operator)

        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(177, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.label)

        self.count_sp = QLabel(self.frame_10)
        self.count_sp.setObjectName(u"count_sp")
        self.count_sp.setMinimumSize(QSize(50, 0))
        self.count_sp.setMaximumSize(QSize(100, 16777215))
        self.count_sp.setLineWidth(1)
        self.count_sp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.count_sp)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_14.addWidget(self.frame_10)

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

        self.verticalLayout_14.addWidget(self.sp_operator)


        self.verticalLayout_sp_operator.addWidget(self.frame_count_sp)

        self.scrollArea_sp_operator.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea_sp_operator)


        self.gridLayout_2.addWidget(self.frame_sp_operator, 0, 1, 3, 1)

        self.stackedWidget.addWidget(self.page_add_email_operator)
        self.page_add_emails_region = QWidget()
        self.page_add_emails_region.setObjectName(u"page_add_emails_region")
        self.page_add_emails_region.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.page_add_emails_region)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 5)
        self.frame_region_emals = QFrame(self.page_add_emails_region)
        self.frame_region_emals.setObjectName(u"frame_region_emals")
        sizePolicy1.setHeightForWidth(self.frame_region_emals.sizePolicy().hasHeightForWidth())
        self.frame_region_emals.setSizePolicy(sizePolicy1)
        self.frame_region_emals.setMinimumSize(QSize(0, 0))
        self.frame_region_emals.setStyleSheet(u"*{font: 12pt \"Arial\";}\n"
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
        self.frame_region_emals.setFrameShape(QFrame.StyledPanel)
        self.frame_region_emals.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_region_emals)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 0, 0, 0)
        self.scrollArea_emails_operator = QScrollArea(self.frame_region_emals)
        self.scrollArea_emails_operator.setObjectName(u"scrollArea_emails_operator")
        self.scrollArea_emails_operator.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 695, 834))
        self.verticalLayout_sp_operator_3 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_sp_operator_3.setObjectName(u"verticalLayout_sp_operator_3")
        self.verticalLayout_sp_operator_3.setContentsMargins(0, 0, 0, 0)
        self.frame_count_regions = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_count_regions.setObjectName(u"frame_count_regions")
        self.frame_count_regions.setStyleSheet(u"")
        self.frame_count_regions.setFrameShape(QFrame.StyledPanel)
        self.frame_count_regions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_count_regions)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_count_regions)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 5)
        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(125, 35))
        self.label_24.setMaximumSize(QSize(125, 16777215))
        self.label_24.setWordWrap(False)

        self.horizontalLayout_18.addWidget(self.label_24)

        self.count_regions = QLabel(self.frame_20)
        self.count_regions.setObjectName(u"count_regions")
        self.count_regions.setMinimumSize(QSize(50, 0))
        self.count_regions.setMaximumSize(QSize(50, 16777215))
        self.count_regions.setScaledContents(False)
        self.count_regions.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.count_regions)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)


        self.verticalLayout_30.addWidget(self.frame_20)

        self.emails_region = QTableWidget(self.frame_count_regions)
        if (self.emails_region.columnCount() < 2):
            self.emails_region.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.emails_region.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.emails_region.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.emails_region.setObjectName(u"emails_region")
        self.emails_region.setStyleSheet(u"")
        self.emails_region.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.emails_region.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.emails_region.setSortingEnabled(True)
        self.emails_region.horizontalHeader().setDefaultSectionSize(300)
        self.emails_region.horizontalHeader().setProperty("showSortIndicator", True)
        self.emails_region.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_30.addWidget(self.emails_region)


        self.verticalLayout_sp_operator_3.addWidget(self.frame_count_regions)

        self.scrollArea_emails_operator.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_31.addWidget(self.scrollArea_emails_operator)


        self.gridLayout_4.addWidget(self.frame_region_emals, 0, 1, 4, 1)

        self.frame_11 = QFrame(self.page_add_emails_region)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(550, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setLineWidth(1)
        self.verticalLayout_29 = QVBoxLayout(self.frame_11)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_save_emails_region = QPushButton(self.frame_11)
        self.btn_save_emails_region.setObjectName(u"btn_save_emails_region")
        sizePolicy4.setHeightForWidth(self.btn_save_emails_region.sizePolicy().hasHeightForWidth())
        self.btn_save_emails_region.setSizePolicy(sizePolicy4)
        self.btn_save_emails_region.setMinimumSize(QSize(0, 45))
        self.btn_save_emails_region.setMaximumSize(QSize(16777215, 16777215))
        self.btn_save_emails_region.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_emails_region.setIcon(icon11)
        self.btn_save_emails_region.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.btn_save_emails_region)

        self.frame_18 = QFrame(self.frame_11)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setLineWidth(1)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 10, 0, 0)
        self.btn_export_regions = QPushButton(self.frame_18)
        self.btn_export_regions.setObjectName(u"btn_export_regions")
        sizePolicy4.setHeightForWidth(self.btn_export_regions.sizePolicy().hasHeightForWidth())
        self.btn_export_regions.setSizePolicy(sizePolicy4)
        self.btn_export_regions.setMinimumSize(QSize(0, 45))
        self.btn_export_regions.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/circle_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_regions.setIcon(icon12)
        self.btn_export_regions.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.btn_export_regions)


        self.verticalLayout_29.addWidget(self.frame_18)


        self.gridLayout_4.addWidget(self.frame_11, 3, 0, 1, 1)

        self.scrollArea_5 = QScrollArea(self.page_add_emails_region)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy)
        self.scrollArea_5.setMaximumSize(QSize(550, 16777215))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 548, 525))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 10, 0, 10)
        self.add_widget_layout_region = QVBoxLayout()
        self.add_widget_layout_region.setSpacing(5)
        self.add_widget_layout_region.setObjectName(u"add_widget_layout_region")
        self.add_widget_layout_region.setSizeConstraint(QLayout.SetNoConstraint)
        self.add_widget_layout_region.setContentsMargins(-1, -1, 0, 0)

        self.verticalLayout_32.addLayout(self.add_widget_layout_region)

        self.verticalSpacer_3 = QSpacerItem(20, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_3)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_4.addWidget(self.scrollArea_5, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.page_add_emails_region)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(550, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_9)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 10)
        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setLineWidth(0)
        self.verticalLayout_26 = QVBoxLayout(self.frame_16)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 10)
        self.label_region = QLabel(self.frame_16)
        self.label_region.setObjectName(u"label_region")
        self.label_region.setMinimumSize(QSize(0, 37))
        self.label_region.setMaximumSize(QSize(200, 16777215))
        self.label_region.setFont(font3)
        self.label_region.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.label_region)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.btn_change_name_region = QPushButton(self.frame_19)
        self.btn_change_name_region.setObjectName(u"btn_change_name_region")
        self.btn_change_name_region.setEnabled(False)
        self.btn_change_name_region.setMinimumSize(QSize(45, 45))
        self.btn_change_name_region.setMaximumSize(QSize(45, 45))
        self.btn_change_name_region.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/edit_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_change_name_region.setIcon(icon13)
        self.btn_change_name_region.setIconSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.btn_change_name_region)

        self.cb_list_regions = QComboBox(self.frame_19)
        self.cb_list_regions.setObjectName(u"cb_list_regions")
        self.cb_list_regions.setEnabled(True)
        self.cb_list_regions.setMinimumSize(QSize(0, 45))
        self.cb_list_regions.setMaximumSize(QSize(16777215, 16777215))
        self.cb_list_regions.setFont(font3)
        self.cb_list_regions.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_list_regions.setStyleSheet(u"")
        self.cb_list_regions.setEditable(False)
        self.cb_list_regions.setMaxVisibleItems(30)
        self.cb_list_regions.setMinimumContentsLength(15)

        self.horizontalLayout_24.addWidget(self.cb_list_regions)


        self.verticalLayout_26.addWidget(self.frame_19)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 30))
        self.label_23.setMaximumSize(QSize(16777215, 16777215))
        self.label_23.setFont(font3)
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_26.addWidget(self.label_23)

        self.frame_21 = QFrame(self.frame_16)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setLineWidth(0)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.labelRegionID = QLabel(self.frame_21)
        self.labelRegionID.setObjectName(u"labelRegionID")
        self.labelRegionID.setMinimumSize(QSize(30, 30))
        self.labelRegionID.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_25.addWidget(self.labelRegionID)

        self.lbl_selected_region = QLabel(self.frame_21)
        self.lbl_selected_region.setObjectName(u"lbl_selected_region")
        sizePolicy1.setHeightForWidth(self.lbl_selected_region.sizePolicy().hasHeightForWidth())
        self.lbl_selected_region.setSizePolicy(sizePolicy1)
        self.lbl_selected_region.setMinimumSize(QSize(0, 30))
        self.lbl_selected_region.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_25.addWidget(self.lbl_selected_region)


        self.verticalLayout_26.addWidget(self.frame_21)


        self.verticalLayout_28.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setLineWidth(0)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_add_field_email_region = QPushButton(self.frame_17)
        self.btn_add_field_email_region.setObjectName(u"btn_add_field_email_region")
        self.btn_add_field_email_region.setMinimumSize(QSize(0, 50))
        self.btn_add_field_email_region.setMaximumSize(QSize(16777215, 50))
        self.btn_add_field_email_region.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btn_add_field_email_region)


        self.verticalLayout_28.addWidget(self.frame_17)


        self.gridLayout_4.addWidget(self.frame_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_add_emails_region)
        self.page_pandas_html_load = QWidget()
        self.page_pandas_html_load.setObjectName(u"page_pandas_html_load")
        sizePolicy3.setHeightForWidth(self.page_pandas_html_load.sizePolicy().hasHeightForWidth())
        self.page_pandas_html_load.setSizePolicy(sizePolicy3)
        self.page_pandas_html_load.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.page_pandas_html_load)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 5)
        self.frame_tab = QFrame(self.page_pandas_html_load)
        self.frame_tab.setObjectName(u"frame_tab")
        sizePolicy3.setHeightForWidth(self.frame_tab.sizePolicy().hasHeightForWidth())
        self.frame_tab.setSizePolicy(sizePolicy3)
        self.frame_tab.setStyleSheet(u"")
        self.frame_tab.setFrameShape(QFrame.StyledPanel)
        self.frame_tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tabWidget = QTabWidget(self.frame_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 700))
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabRossreestr = QWidget()
        self.tabRossreestr.setObjectName(u"tabRossreestr")
        sizePolicy.setHeightForWidth(self.tabRossreestr.sizePolicy().hasHeightForWidth())
        self.tabRossreestr.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.tabRossreestr)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 10, 0, 0)
        self.frame_rossreestr = QFrame(self.tabRossreestr)
        self.frame_rossreestr.setObjectName(u"frame_rossreestr")
        self.frame_rossreestr.setMinimumSize(QSize(0, 0))
        self.frame_rossreestr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_rossreestr.setFont(font3)
        self.frame_rossreestr.setFrameShape(QFrame.NoFrame)
        self.frame_rossreestr.setFrameShadow(QFrame.Plain)
        self.frame_rossreestr.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_rossreestr)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.le_search_rossreestr = QLineEdit(self.frame_rossreestr)
        self.le_search_rossreestr.setObjectName(u"le_search_rossreestr")
        self.le_search_rossreestr.setMinimumSize(QSize(0, 45))
        self.le_search_rossreestr.setMaximumSize(QSize(16777215, 45))
        self.le_search_rossreestr.setFont(font3)
        self.le_search_rossreestr.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.le_search_rossreestr)

        self.btn_pandas_upload = QPushButton(self.frame_rossreestr)
        self.btn_pandas_upload.setObjectName(u"btn_pandas_upload")
        self.btn_pandas_upload.setEnabled(False)
        self.btn_pandas_upload.setMinimumSize(QSize(45, 45))
        self.btn_pandas_upload.setMaximumSize(QSize(16777215, 45))
        self.btn_pandas_upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pandas_upload.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/download-cloud_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pandas_upload.setIcon(icon14)
        self.btn_pandas_upload.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.btn_pandas_upload)


        self.verticalLayout_10.addWidget(self.frame_rossreestr, 0, Qt.AlignTop)

        self.scrollArea_4 = QScrollArea(self.tabRossreestr)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(0, 0))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1229, 483))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents_5.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbl_data_pandas = QTableView(self.scrollAreaWidgetContents_5)
        self.tbl_data_pandas.setObjectName(u"tbl_data_pandas")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tbl_data_pandas.sizePolicy().hasHeightForWidth())
        self.tbl_data_pandas.setSizePolicy(sizePolicy5)
        self.tbl_data_pandas.setMinimumSize(QSize(0, 0))
        self.tbl_data_pandas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_data_pandas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_data_pandas.setSortingEnabled(True)
        self.tbl_data_pandas.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbl_data_pandas.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_3.addWidget(self.tbl_data_pandas)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_10.addWidget(self.scrollArea_4)

        self.frm_info_oper_2 = QFrame(self.tabRossreestr)
        self.frm_info_oper_2.setObjectName(u"frm_info_oper_2")
        self.frm_info_oper_2.setMinimumSize(QSize(0, 0))
        self.frm_info_oper_2.setMaximumSize(QSize(16777215, 16777215))
        self.frm_info_oper_2.setFrameShape(QFrame.NoFrame)
        self.frm_info_oper_2.setFrameShadow(QFrame.Plain)
        self.frm_info_oper_2.setLineWidth(0)
        self.verticalLayout_50 = QVBoxLayout(self.frm_info_oper_2)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_17 = QLabel(self.frm_info_oper_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 0))

        self.verticalLayout_44.addWidget(self.label_17)

        self.le_operator = QLineEdit(self.frm_info_oper_2)
        self.le_operator.setObjectName(u"le_operator")
        self.le_operator.setMinimumSize(QSize(0, 0))

        self.verticalLayout_44.addWidget(self.le_operator)


        self.horizontalLayout_14.addLayout(self.verticalLayout_44)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_18 = QLabel(self.frm_info_oper_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))

        self.verticalLayout_45.addWidget(self.label_18)

        self.le_zone_obslujivaniya = QLineEdit(self.frm_info_oper_2)
        self.le_zone_obslujivaniya.setObjectName(u"le_zone_obslujivaniya")
        self.le_zone_obslujivaniya.setMinimumSize(QSize(0, 0))

        self.verticalLayout_45.addWidget(self.le_zone_obslujivaniya)


        self.horizontalLayout_14.addLayout(self.verticalLayout_45)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_14 = QLabel(self.frm_info_oper_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))

        self.verticalLayout_46.addWidget(self.label_14)

        self.le_mesto_ustanovki = QLineEdit(self.frm_info_oper_2)
        self.le_mesto_ustanovki.setObjectName(u"le_mesto_ustanovki")
        self.le_mesto_ustanovki.setMinimumSize(QSize(0, 0))

        self.verticalLayout_46.addWidget(self.le_mesto_ustanovki)


        self.horizontalLayout_14.addLayout(self.verticalLayout_46)


        self.verticalLayout_50.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_16 = QLabel(self.frm_info_oper_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))

        self.verticalLayout_47.addWidget(self.label_16)

        self.le_decadnii = QLineEdit(self.frm_info_oper_2)
        self.le_decadnii.setObjectName(u"le_decadnii")
        self.le_decadnii.setMinimumSize(QSize(0, 0))

        self.verticalLayout_47.addWidget(self.le_decadnii)


        self.horizontalLayout_15.addLayout(self.verticalLayout_47)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_20 = QLabel(self.frm_info_oper_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))

        self.verticalLayout_48.addWidget(self.label_20)

        self.le_abc_def = QLineEdit(self.frm_info_oper_2)
        self.le_abc_def.setObjectName(u"le_abc_def")
        self.le_abc_def.setMinimumSize(QSize(0, 0))

        self.verticalLayout_48.addWidget(self.le_abc_def)


        self.horizontalLayout_15.addLayout(self.verticalLayout_48)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_15 = QLabel(self.frm_info_oper_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))

        self.verticalLayout_49.addWidget(self.label_15)

        self.le_structurnii = QLineEdit(self.frm_info_oper_2)
        self.le_structurnii.setObjectName(u"le_structurnii")
        self.le_structurnii.setMinimumSize(QSize(0, 0))

        self.verticalLayout_49.addWidget(self.le_structurnii)


        self.horizontalLayout_15.addLayout(self.verticalLayout_49)


        self.verticalLayout_50.addLayout(self.horizontalLayout_15)


        self.verticalLayout_10.addWidget(self.frm_info_oper_2)

        self.tabWidget.addTab(self.tabRossreestr, "")
        self.tabOutlook = QWidget()
        self.tabOutlook.setObjectName(u"tabOutlook")
        sizePolicy.setHeightForWidth(self.tabOutlook.sizePolicy().hasHeightForWidth())
        self.tabOutlook.setSizePolicy(sizePolicy)
        self.tabOutlook.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_11 = QVBoxLayout(self.tabOutlook)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 10, 0, 0)
        self.frame_outlook = QFrame(self.tabOutlook)
        self.frame_outlook.setObjectName(u"frame_outlook")
        self.frame_outlook.setMinimumSize(QSize(0, 0))
        self.frame_outlook.setMaximumSize(QSize(16777215, 16777215))
        self.frame_outlook.setFrameShape(QFrame.NoFrame)
        self.frame_outlook.setFrameShadow(QFrame.Plain)
        self.frame_outlook.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_outlook)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.le_search = QLineEdit(self.frame_outlook)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMinimumSize(QSize(0, 45))
        self.le_search.setMaximumSize(QSize(16777215, 45))
        self.le_search.setFont(font3)
        self.le_search.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.le_search)

        self.btn_upload_mgmn_outlook = QPushButton(self.frame_outlook)
        self.btn_upload_mgmn_outlook.setObjectName(u"btn_upload_mgmn_outlook")
        self.btn_upload_mgmn_outlook.setEnabled(False)
        self.btn_upload_mgmn_outlook.setMinimumSize(QSize(45, 45))
        self.btn_upload_mgmn_outlook.setMaximumSize(QSize(16777215, 45))
        self.btn_upload_mgmn_outlook.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upload_mgmn_outlook.setFocusPolicy(Qt.NoFocus)
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/download_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_upload_mgmn_outlook.setIcon(icon15)
        self.btn_upload_mgmn_outlook.setIconSize(QSize(24, 24))
        self.btn_upload_mgmn_outlook.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btn_upload_mgmn_outlook)


        self.verticalLayout_11.addWidget(self.frame_outlook)

        self.frame = QFrame(self.tabOutlook)
        self.frame.setObjectName(u"frame")
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.frame)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1229, 483))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tbl_data_pandas_mgmn = QTableView(self.scrollAreaWidgetContents_2)
        self.tbl_data_pandas_mgmn.setObjectName(u"tbl_data_pandas_mgmn")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        font4.setKerning(True)
        self.tbl_data_pandas_mgmn.setFont(font4)
        self.tbl_data_pandas_mgmn.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tbl_data_pandas_mgmn.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tbl_data_pandas_mgmn.setAutoScroll(True)
        self.tbl_data_pandas_mgmn.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tbl_data_pandas_mgmn.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tbl_data_pandas_mgmn.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_data_pandas_mgmn.setSortingEnabled(True)
        self.tbl_data_pandas_mgmn.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbl_data_pandas_mgmn.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_13.addWidget(self.tbl_data_pandas_mgmn)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_18.addWidget(self.scrollArea_2)


        self.verticalLayout_11.addWidget(self.frame)

        self.frm_info_oper = QFrame(self.tabOutlook)
        self.frm_info_oper.setObjectName(u"frm_info_oper")
        self.frm_info_oper.setFrameShape(QFrame.NoFrame)
        self.frm_info_oper.setFrameShadow(QFrame.Plain)
        self.frm_info_oper.setLineWidth(0)
        self.verticalLayout_43 = QVBoxLayout(self.frm_info_oper)
        self.verticalLayout_43.setSpacing(5)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_2 = QLabel(self.frm_info_oper)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_35.addWidget(self.label_2)

        self.le_kommutator = QLineEdit(self.frm_info_oper)
        self.le_kommutator.setObjectName(u"le_kommutator")

        self.verticalLayout_35.addWidget(self.le_kommutator)


        self.horizontalLayout_7.addLayout(self.verticalLayout_35)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_9 = QLabel(self.frm_info_oper)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_36.addWidget(self.label_9)

        self.le_name_trank = QLineEdit(self.frm_info_oper)
        self.le_name_trank.setObjectName(u"le_name_trank")

        self.verticalLayout_36.addWidget(self.le_name_trank)


        self.horizontalLayout_7.addLayout(self.verticalLayout_36)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_6 = QLabel(self.frm_info_oper)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_37.addWidget(self.label_6)

        self.le_region_kommutatora = QLineEdit(self.frm_info_oper)
        self.le_region_kommutatora.setObjectName(u"le_region_kommutatora")

        self.verticalLayout_37.addWidget(self.le_region_kommutatora)


        self.horizontalLayout_7.addLayout(self.verticalLayout_37)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_13 = QLabel(self.frm_info_oper)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_38.addWidget(self.label_13)

        self.le_region_shluza = QLineEdit(self.frm_info_oper)
        self.le_region_shluza.setObjectName(u"le_region_shluza")

        self.verticalLayout_38.addWidget(self.le_region_shluza)


        self.horizontalLayout_7.addLayout(self.verticalLayout_38)


        self.verticalLayout_43.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_5 = QLabel(self.frm_info_oper)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_39.addWidget(self.label_5)

        self.le_operator_name = QLineEdit(self.frm_info_oper)
        self.le_operator_name.setObjectName(u"le_operator_name")

        self.verticalLayout_39.addWidget(self.le_operator_name)


        self.horizontalLayout_13.addLayout(self.verticalLayout_39)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_10 = QLabel(self.frm_info_oper)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_40.addWidget(self.label_10)

        self.le_opc = QLineEdit(self.frm_info_oper)
        self.le_opc.setObjectName(u"le_opc")

        self.verticalLayout_40.addWidget(self.le_opc)


        self.horizontalLayout_13.addLayout(self.verticalLayout_40)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_12 = QLabel(self.frm_info_oper)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_41.addWidget(self.label_12)

        self.le_dpc_name = QLineEdit(self.frm_info_oper)
        self.le_dpc_name.setObjectName(u"le_dpc_name")

        self.verticalLayout_41.addWidget(self.le_dpc_name)


        self.horizontalLayout_13.addLayout(self.verticalLayout_41)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_11 = QLabel(self.frm_info_oper)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_42.addWidget(self.label_11)

        self.le_uroven_prisoedineniya = QLineEdit(self.frm_info_oper)
        self.le_uroven_prisoedineniya.setObjectName(u"le_uroven_prisoedineniya")

        self.verticalLayout_42.addWidget(self.le_uroven_prisoedineniya)


        self.horizontalLayout_13.addLayout(self.verticalLayout_42)


        self.verticalLayout_43.addLayout(self.horizontalLayout_13)


        self.verticalLayout_11.addWidget(self.frm_info_oper)

        self.tabWidget.addTab(self.tabOutlook, "")

        self.verticalLayout_12.addWidget(self.tabWidget)

        self.listWidget_operations = QListWidget(self.frame_tab)
        self.listWidget_operations.setObjectName(u"listWidget_operations")
        sizePolicy5.setHeightForWidth(self.listWidget_operations.sizePolicy().hasHeightForWidth())
        self.listWidget_operations.setSizePolicy(sizePolicy5)
        self.listWidget_operations.setMinimumSize(QSize(0, 110))
        self.listWidget_operations.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_operations.setStyleSheet(u"")
        self.listWidget_operations.setAutoScroll(True)

        self.verticalLayout_12.addWidget(self.listWidget_operations)


        self.verticalLayout_16.addWidget(self.frame_tab)

        self.stackedWidget.addWidget(self.page_pandas_html_load)
        self.page_log = QWidget()
        self.page_log.setObjectName(u"page_log")
        self.page_log.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.page_log)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 5)
        self.frame_log = QFrame(self.page_log)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setFrameShape(QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_log)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lbl_log_and_admin = QLabel(self.frame_log)
        self.lbl_log_and_admin.setObjectName(u"lbl_log_and_admin")
        self.lbl_log_and_admin.setMinimumSize(QSize(0, 40))
        self.lbl_log_and_admin.setMaximumSize(QSize(16777215, 40))
        self.lbl_log_and_admin.setAlignment(Qt.AlignCenter)
        self.lbl_log_and_admin.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.lbl_log_and_admin)


        self.verticalLayout_17.addWidget(self.frame_log)

        self.frame_22 = QFrame(self.page_log)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_22)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_page_log = QFrame(self.frame_22)
        self.frame_page_log.setObjectName(u"frame_page_log")
        sizePolicy1.setHeightForWidth(self.frame_page_log.sizePolicy().hasHeightForWidth())
        self.frame_page_log.setSizePolicy(sizePolicy1)
        self.frame_page_log.setMinimumSize(QSize(0, 0))
        self.frame_page_log.setMaximumSize(QSize(16777215, 16777215))
        self.frame_page_log.setFont(font3)
        self.frame_page_log.setStyleSheet(u"")
        self.frame_page_log.setFrameShape(QFrame.StyledPanel)
        self.frame_page_log.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_page_log)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 5, 0, 0)
        self.scrollArea_sp_operator_2 = QScrollArea(self.frame_page_log)
        self.scrollArea_sp_operator_2.setObjectName(u"scrollArea_sp_operator_2")
        self.scrollArea_sp_operator_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 891, 783))
        self.verticalLayout_sp_operator_2 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_sp_operator_2.setSpacing(0)
        self.verticalLayout_sp_operator_2.setObjectName(u"verticalLayout_sp_operator_2")
        self.verticalLayout_sp_operator_2.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_15)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_15)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(0)
        self.verticalLayout_21 = QVBoxLayout(self.frame_7)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 40))
        self.label_43.setMaximumSize(QSize(16777215, 40))
        self.label_43.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.label_43)

        self.layoutFiltrsLogs = QHBoxLayout()
        self.layoutFiltrsLogs.setSpacing(10)
        self.layoutFiltrsLogs.setObjectName(u"layoutFiltrsLogs")
        self.status = QComboBox(self.frame_7)
        self.status.setObjectName(u"status")
        sizePolicy4.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy4)
        self.status.setMinimumSize(QSize(0, 45))
        self.status.setCursor(QCursor(Qt.PointingHandCursor))
        self.status.setMinimumContentsLength(10)

        self.layoutFiltrsLogs.addWidget(self.status)

        self.creator = QComboBox(self.frame_7)
        self.creator.setObjectName(u"creator")
        sizePolicy1.setHeightForWidth(self.creator.sizePolicy().hasHeightForWidth())
        self.creator.setSizePolicy(sizePolicy1)
        self.creator.setMinimumSize(QSize(0, 45))
        self.creator.setCursor(QCursor(Qt.PointingHandCursor))
        self.creator.setStyleSheet(u"")
        self.creator.setMinimumContentsLength(20)

        self.layoutFiltrsLogs.addWidget(self.creator)

        self.label_28 = QLabel(self.frame_7)
        self.label_28.setObjectName(u"label_28")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy6)
        self.label_28.setMinimumSize(QSize(0, 0))

        self.layoutFiltrsLogs.addWidget(self.label_28, 0, Qt.AlignRight)

        self.date_create__start = QDateEdit(self.frame_7)
        self.date_create__start.setObjectName(u"date_create__start")
        self.date_create__start.setMinimumSize(QSize(0, 45))
        self.date_create__start.setMaximumSize(QSize(180, 16777215))
        self.date_create__start.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_create__start.setWrapping(True)
        self.date_create__start.setProperty("showGroupSeparator", True)
        self.date_create__start.setCalendarPopup(True)

        self.layoutFiltrsLogs.addWidget(self.date_create__start)

        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        sizePolicy6.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy6)
        self.label_26.setMinimumSize(QSize(0, 0))

        self.layoutFiltrsLogs.addWidget(self.label_26, 0, Qt.AlignRight)

        self.date_create__end = QDateEdit(self.frame_7)
        self.date_create__end.setObjectName(u"date_create__end")
        self.date_create__end.setMinimumSize(QSize(0, 45))
        self.date_create__end.setMaximumSize(QSize(180, 16777215))
        self.date_create__end.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_create__end.setWrapping(False)
        self.date_create__end.setCalendarPopup(True)
        self.date_create__end.setTimeSpec(Qt.LocalTime)

        self.layoutFiltrsLogs.addWidget(self.date_create__end)


        self.verticalLayout_21.addLayout(self.layoutFiltrsLogs)


        self.verticalLayout_19.addWidget(self.frame_7)

        self.scrollArea_3 = QScrollArea(self.frame_15)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 887, 623))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.tbl_log = QTableView(self.scrollAreaWidgetContents_6)
        self.tbl_log.setObjectName(u"tbl_log")
        self.tbl_log.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tbl_log.setStyleSheet(u"")
        self.tbl_log.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.SelectedClicked)
        self.tbl_log.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tbl_log.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_log.setIconSize(QSize(16, 16))
        self.tbl_log.setTextElideMode(Qt.ElideLeft)
        self.tbl_log.setSortingEnabled(True)
        self.tbl_log.horizontalHeader().setStretchLastSection(False)
        self.tbl_log.verticalHeader().setVisible(False)
        self.tbl_log.verticalHeader().setCascadingSectionResizes(True)
        self.tbl_log.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_23.addWidget(self.tbl_log)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_19.addWidget(self.scrollArea_3)

        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 45))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_delete_row_log = QPushButton(self.frame_14)
        self.btn_delete_row_log.setObjectName(u"btn_delete_row_log")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_delete_row_log.sizePolicy().hasHeightForWidth())
        self.btn_delete_row_log.setSizePolicy(sizePolicy7)
        self.btn_delete_row_log.setMinimumSize(QSize(0, 50))
        self.btn_delete_row_log.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/trash-2_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_row_log.setIcon(icon16)
        self.btn_delete_row_log.setIconSize(QSize(24, 24))
        self.btn_delete_row_log.setFlat(False)

        self.horizontalLayout_16.addWidget(self.btn_delete_row_log)

        self.btn_clear_log = QPushButton(self.frame_14)
        self.btn_clear_log.setObjectName(u"btn_clear_log")
        sizePolicy4.setHeightForWidth(self.btn_clear_log.sizePolicy().hasHeightForWidth())
        self.btn_clear_log.setSizePolicy(sizePolicy4)
        self.btn_clear_log.setMinimumSize(QSize(0, 50))
        self.btn_clear_log.setMaximumSize(QSize(16777215, 50))
        self.btn_clear_log.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.btn_clear_log)


        self.verticalLayout_19.addWidget(self.frame_14)


        self.verticalLayout_sp_operator_2.addWidget(self.frame_15)

        self.scrollArea_sp_operator_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_22.addWidget(self.scrollArea_sp_operator_2)


        self.gridLayout_5.addWidget(self.frame_page_log, 0, 1, 1, 1)

        self.frame_users = QFrame(self.frame_22)
        self.frame_users.setObjectName(u"frame_users")
        self.frame_users.setMinimumSize(QSize(350, 0))
        self.frame_users.setMaximumSize(QSize(300, 16777215))
        self.frame_users.setStyleSheet(u"")
        self.frame_users.setFrameShape(QFrame.StyledPanel)
        self.frame_users.setFrameShadow(QFrame.Raised)
        self.frame_users.setLineWidth(0)
        self.verticalLayout_27 = QVBoxLayout(self.frame_users)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 5, 0, 0)
        self.lbl_admins = QLabel(self.frame_users)
        self.lbl_admins.setObjectName(u"lbl_admins")
        self.lbl_admins.setMinimumSize(QSize(0, 40))
        self.lbl_admins.setMaximumSize(QSize(16777215, 40))
        self.lbl_admins.setScaledContents(False)
        self.lbl_admins.setAlignment(Qt.AlignCenter)
        self.lbl_admins.setMargin(0)

        self.verticalLayout_27.addWidget(self.lbl_admins)

        self.scrollAreaAdmins = QScrollArea(self.frame_users)
        self.scrollAreaAdmins.setObjectName(u"scrollAreaAdmins")
        self.scrollAreaAdmins.setWidgetResizable(True)
        self.scroll_admins = QWidget()
        self.scroll_admins.setObjectName(u"scroll_admins")
        self.scroll_admins.setGeometry(QRect(0, 0, 346, 681))
        self.verticalLayout_20 = QVBoxLayout(self.scroll_admins)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.layout_view_admins = QVBoxLayout()
        self.layout_view_admins.setSpacing(5)
        self.layout_view_admins.setObjectName(u"layout_view_admins")

        self.verticalLayout_20.addLayout(self.layout_view_admins)

        self.verticalSpacer_4 = QSpacerItem(20, 398, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_4)

        self.scrollAreaAdmins.setWidget(self.scroll_admins)

        self.verticalLayout_27.addWidget(self.scrollAreaAdmins)

        self.frame_13 = QFrame(self.frame_users)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_add_admin = QPushButton(self.frame_13)
        self.btn_add_admin.setObjectName(u"btn_add_admin")
        self.btn_add_admin.setMinimumSize(QSize(0, 50))
        self.btn_add_admin.setMaximumSize(QSize(16777215, 50))
        self.btn_add_admin.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/user-plus_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_admin.setIcon(icon17)
        self.btn_add_admin.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_add_admin)


        self.verticalLayout_27.addWidget(self.frame_13)


        self.gridLayout_5.addWidget(self.frame_users, 0, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_log)
        self.page_statistics = QWidget()
        self.page_statistics.setObjectName(u"page_statistics")
        self.verticalLayout_51 = QVBoxLayout(self.page_statistics)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(10, 0, 0, 0)
        self.stat_frame = QFrame(self.page_statistics)
        self.stat_frame.setObjectName(u"stat_frame")
        self.stat_frame.setLineWidth(0)
        self.verticalLayout_52 = QVBoxLayout(self.stat_frame)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.stat_contain_frame = QFrame(self.stat_frame)
        self.stat_contain_frame.setObjectName(u"stat_contain_frame")
        self.stat_contain_frame.setFrameShape(QFrame.NoFrame)
        self.stat_contain_frame.setFrameShadow(QFrame.Plain)
        self.stat_contain_frame.setLineWidth(0)
        self.verticalLayout_61 = QVBoxLayout(self.stat_contain_frame)
        self.verticalLayout_61.setSpacing(10)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frm_top_title = QFrame(self.stat_contain_frame)
        self.frm_top_title.setObjectName(u"frm_top_title")
        self.frm_top_title.setFrameShape(QFrame.StyledPanel)
        self.frm_top_title.setFrameShadow(QFrame.Raised)
        self.frm_top_title.setLineWidth(1)
        self.horizontalLayout_34 = QHBoxLayout(self.frm_top_title)
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 5, 5, 5)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_4)

        self.title_inc_lbl = QLabel(self.frm_top_title)
        self.title_inc_lbl.setObjectName(u"title_inc_lbl")
        self.title_inc_lbl.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_34.addWidget(self.title_inc_lbl)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_8)


        self.verticalLayout_61.addWidget(self.frm_top_title)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.statistics_menu_listWidget = QListWidget(self.stat_contain_frame)
        self.statistics_menu_listWidget.setObjectName(u"statistics_menu_listWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.statistics_menu_listWidget.sizePolicy().hasHeightForWidth())
        self.statistics_menu_listWidget.setSizePolicy(sizePolicy8)
        self.statistics_menu_listWidget.setMinimumSize(QSize(280, 0))
        self.statistics_menu_listWidget.setMaximumSize(QSize(280, 16777215))
        self.statistics_menu_listWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.statistics_menu_listWidget.setFrameShape(QFrame.NoFrame)
        self.statistics_menu_listWidget.setFrameShadow(QFrame.Plain)
        self.statistics_menu_listWidget.setLineWidth(0)
        self.statistics_menu_listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.statistics_menu_listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.statistics_menu_listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.statistics_menu_listWidget.setIconSize(QSize(30, 30))

        self.horizontalLayout_19.addWidget(self.statistics_menu_listWidget)

        self.statistics_stackedWidget = QStackedWidget(self.stat_contain_frame)
        self.statistics_stackedWidget.setObjectName(u"statistics_stackedWidget")
        self.statistics_stackedWidget.setFrameShape(QFrame.NoFrame)
        self.statistics_stackedWidget.setLineWidth(0)
        self.operators_page = QWidget()
        self.operators_page.setObjectName(u"operators_page")
        self.horizontalLayout_47 = QHBoxLayout(self.operators_page)
        self.horizontalLayout_47.setSpacing(5)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(10, 0, 0, 0)
        self.operators_listWidget = QListWidget(self.operators_page)
        self.operators_listWidget.setObjectName(u"operators_listWidget")
        self.operators_listWidget.setMinimumSize(QSize(0, 0))
        self.operators_listWidget.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_47.addWidget(self.operators_listWidget)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_9)

        self.statistics_stackedWidget.addWidget(self.operators_page)
        self.users_page = QWidget()
        self.users_page.setObjectName(u"users_page")
        self.label_7 = QLabel(self.users_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 180, 221, 51))
        self.statistics_stackedWidget.addWidget(self.users_page)
        self.all_inc_page = QWidget()
        self.all_inc_page.setObjectName(u"all_inc_page")
        self.horizontalLayout_35 = QHBoxLayout(self.all_inc_page)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 10, 10, 0)
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(10)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.all_inc_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(300, 0))
        self.frame_26.setMaximumSize(QSize(300, 16777215))
        self.frame_26.setLineWidth(0)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(10, 5, 10, 5)
        self.cmb_sorting_inc = QComboBox(self.frame_26)
        self.cmb_sorting_inc.setObjectName(u"cmb_sorting_inc")
        self.cmb_sorting_inc.setMinimumSize(QSize(0, 40))
        self.cmb_sorting_inc.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmb_sorting_inc.setEditable(True)

        self.horizontalLayout_31.addWidget(self.cmb_sorting_inc)

        self.btn_delete_inc = QPushButton(self.frame_26)
        self.btn_delete_inc.setObjectName(u"btn_delete_inc")
        self.btn_delete_inc.setMinimumSize(QSize(40, 40))
        self.btn_delete_inc.setMaximumSize(QSize(40, 40))
        self.btn_delete_inc.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_inc.setIcon(icon18)
        self.btn_delete_inc.setIconSize(QSize(30, 30))

        self.horizontalLayout_31.addWidget(self.btn_delete_inc)


        self.verticalLayout_59.addWidget(self.frame_26)

        self.scrollAreaIncidents = QScrollArea(self.all_inc_page)
        self.scrollAreaIncidents.setObjectName(u"scrollAreaIncidents")
        sizePolicy.setHeightForWidth(self.scrollAreaIncidents.sizePolicy().hasHeightForWidth())
        self.scrollAreaIncidents.setSizePolicy(sizePolicy)
        self.scrollAreaIncidents.setMinimumSize(QSize(300, 0))
        self.scrollAreaIncidents.setMaximumSize(QSize(300, 16777215))
        self.scrollAreaIncidents.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 298, 712))
        self.verticalLayout_58 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.list_incidents_layout = QVBoxLayout()
        self.list_incidents_layout.setSpacing(5)
        self.list_incidents_layout.setObjectName(u"list_incidents_layout")
        self.list_incidents_layout.setContentsMargins(0, -1, 0, -1)

        self.verticalLayout_58.addLayout(self.list_incidents_layout)

        self.verticalSpacer_6 = QSpacerItem(20, 712, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_6)

        self.scrollAreaIncidents.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_59.addWidget(self.scrollAreaIncidents)


        self.horizontalLayout_33.addLayout(self.verticalLayout_59)

        self.frame_27 = QFrame(self.all_inc_page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Plain)
        self.frame_27.setLineWidth(0)
        self.verticalLayout_63 = QVBoxLayout(self.frame_27)
        self.verticalLayout_63.setSpacing(15)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(10, 0, 0, 5)
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(5)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_3 = QLabel(self.frame_27)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_38.addWidget(self.label_3)

        self.le_inc_stat = QLineEdit(self.frame_27)
        self.le_inc_stat.setObjectName(u"le_inc_stat")
        self.le_inc_stat.setMinimumSize(QSize(0, 40))
        self.le_inc_stat.setMaximumSize(QSize(380, 16777215))

        self.horizontalLayout_38.addWidget(self.le_inc_stat)


        self.horizontalLayout_44.addLayout(self.horizontalLayout_38)

        self.grb_status_inc = QGroupBox(self.frame_27)
        self.grb_status_inc.setObjectName(u"grb_status_inc")
        self.grb_status_inc.setMinimumSize(QSize(370, 0))
        self.verticalLayout_62 = QVBoxLayout(self.grb_status_inc)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(5, 0, 5, 0)
        self.lbl_status_inc_stat = QLabel(self.grb_status_inc)
        self.lbl_status_inc_stat.setObjectName(u"lbl_status_inc_stat")

        self.verticalLayout_62.addWidget(self.lbl_status_inc_stat)


        self.horizontalLayout_44.addWidget(self.grb_status_inc)


        self.verticalLayout_63.addLayout(self.horizontalLayout_44)

        self.inc_stat_toolBox = QToolBox(self.frame_27)
        self.inc_stat_toolBox.setObjectName(u"inc_stat_toolBox")
        self.inc_stat_toolBox.setCursor(QCursor(Qt.ArrowCursor))
        self.inc_stat_toolBox.setFrameShape(QFrame.StyledPanel)
        self.inc_stat_toolBox.setLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 650, 401))
        self.verticalLayout_64 = QVBoxLayout(self.page)
        self.verticalLayout_64.setSpacing(10)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_36 = QLabel(self.page)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 0))
        self.label_36.setMaximumSize(QSize(200, 16777215))
        self.label_36.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_39.addWidget(self.label_36)

        self.lbl_operator_stat_inc = QLabel(self.page)
        self.lbl_operator_stat_inc.setObjectName(u"lbl_operator_stat_inc")
        self.lbl_operator_stat_inc.setMinimumSize(QSize(0, 40))
        self.lbl_operator_stat_inc.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_39.addWidget(self.lbl_operator_stat_inc)


        self.verticalLayout_64.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_33 = QLabel(self.page)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(200, 16777215))
        self.label_33.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_40.addWidget(self.label_33)

        self.cb_type_operator = QComboBox(self.page)
        self.cb_type_operator.addItem("")
        self.cb_type_operator.addItem("")
        self.cb_type_operator.addItem("")
        self.cb_type_operator.setObjectName(u"cb_type_operator")
        self.cb_type_operator.setEnabled(False)
        self.cb_type_operator.setMinimumSize(QSize(0, 40))
        self.cb_type_operator.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_40.addWidget(self.cb_type_operator)


        self.verticalLayout_64.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_37 = QLabel(self.page)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_36.addWidget(self.label_37)

        self.lbl_location_operator_stat = QLabel(self.page)
        self.lbl_location_operator_stat.setObjectName(u"lbl_location_operator_stat")
        self.lbl_location_operator_stat.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_36.addWidget(self.lbl_location_operator_stat)


        self.verticalLayout_64.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setSpacing(5)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_28 = QFrame(self.page)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(200, 16777215))
        self.frame_28.setLineWidth(0)
        self.verticalLayout_66 = QVBoxLayout(self.frame_28)
        self.verticalLayout_66.setSpacing(5)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(90, 0))
        self.label_35.setMaximumSize(QSize(16777215, 16777215))
        self.label_35.setLayoutDirection(Qt.LeftToRight)
        self.label_35.setLineWidth(0)
        self.label_35.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_41.addWidget(self.label_35)

        self.le_dpc_stat = QLineEdit(self.frame_28)
        self.le_dpc_stat.setObjectName(u"le_dpc_stat")
        self.le_dpc_stat.setMinimumSize(QSize(0, 40))
        self.le_dpc_stat.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_41.addWidget(self.le_dpc_stat)


        self.verticalLayout_66.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(90, 0))
        self.label_34.setMaximumSize(QSize(16777215, 16777215))
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_34.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_32.addWidget(self.label_34)

        self.le_opc_stat = QLineEdit(self.frame_28)
        self.le_opc_stat.setObjectName(u"le_opc_stat")
        self.le_opc_stat.setMinimumSize(QSize(0, 40))
        self.le_opc_stat.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_32.addWidget(self.le_opc_stat)


        self.verticalLayout_66.addLayout(self.horizontalLayout_32)


        self.horizontalLayout_45.addWidget(self.frame_28, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.label_38 = QLabel(self.page)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.label_38)

        self.email_operator_listWidget = QListWidget(self.page)
        self.email_operator_listWidget.setObjectName(u"email_operator_listWidget")
        self.email_operator_listWidget.setMaximumSize(QSize(350, 16777215))
        self.email_operator_listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.email_operator_listWidget.setItemAlignment(Qt.AlignLeading)

        self.verticalLayout.addWidget(self.email_operator_listWidget)


        self.horizontalLayout_45.addLayout(self.verticalLayout)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_5)


        self.verticalLayout_64.addLayout(self.horizontalLayout_45)

        self.inc_stat_toolBox.addItem(self.page, u"\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0443")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 650, 283))
        self.verticalLayout_65 = QVBoxLayout(self.page_2)
        self.verticalLayout_65.setSpacing(10)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_40 = QLabel(self.page_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_37.addWidget(self.label_40)

        self.lbl_link_inc = QLabel(self.page_2)
        self.lbl_link_inc.setObjectName(u"lbl_link_inc")
        self.lbl_link_inc.setMinimumSize(QSize(0, 30))
        self.lbl_link_inc.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_link_inc.setFocusPolicy(Qt.StrongFocus)
        self.lbl_link_inc.setOpenExternalLinks(True)
        self.lbl_link_inc.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_37.addWidget(self.lbl_link_inc)


        self.verticalLayout_65.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_41 = QLabel(self.page_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_43.addWidget(self.label_41)

        self.lbl_cause_inc_stat = QLabel(self.page_2)
        self.lbl_cause_inc_stat.setObjectName(u"lbl_cause_inc_stat")
        self.lbl_cause_inc_stat.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_43.addWidget(self.lbl_cause_inc_stat)


        self.verticalLayout_65.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_39 = QLabel(self.page_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_42.addWidget(self.label_39)

        self.lbl_source_inc_stat = QLabel(self.page_2)
        self.lbl_source_inc_stat.setObjectName(u"lbl_source_inc_stat")
        self.lbl_source_inc_stat.setMinimumSize(QSize(0, 30))
        self.lbl_source_inc_stat.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_42.addWidget(self.lbl_source_inc_stat)


        self.verticalLayout_65.addLayout(self.horizontalLayout_42)

        self.frame_33 = QFrame(self.page_2)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"")
        self.frame_33.setLineWidth(0)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_33)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(170, 0))
        self.label_42.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_46.addWidget(self.label_42)

        self.le_parent_inc = QLineEdit(self.frame_33)
        self.le_parent_inc.setObjectName(u"le_parent_inc")
        sizePolicy2.setHeightForWidth(self.le_parent_inc.sizePolicy().hasHeightForWidth())
        self.le_parent_inc.setSizePolicy(sizePolicy2)
        self.le_parent_inc.setMinimumSize(QSize(200, 30))
        self.le_parent_inc.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_46.addWidget(self.le_parent_inc)


        self.verticalLayout_65.addWidget(self.frame_33, 0, Qt.AlignLeft)

        self.verticalSpacer_8 = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_8)

        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/chevron-down_.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon19.addFile(u":/icons/icons/chevron-up_.svg", QSize(), QIcon.Normal, QIcon.On)
        self.inc_stat_toolBox.addItem(self.page_2, icon19, u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0443")

        self.verticalLayout_63.addWidget(self.inc_stat_toolBox)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_7)


        self.horizontalLayout_33.addWidget(self.frame_27)

        self.horizontalLayout_33.setStretch(1, 1)

        self.horizontalLayout_35.addLayout(self.horizontalLayout_33)

        self.statistics_stackedWidget.addWidget(self.all_inc_page)

        self.horizontalLayout_19.addWidget(self.statistics_stackedWidget)


        self.verticalLayout_61.addLayout(self.horizontalLayout_19)


        self.verticalLayout_52.addWidget(self.stat_contain_frame)


        self.verticalLayout_51.addWidget(self.stat_frame)

        self.stackedWidget.addWidget(self.page_statistics)

        self.verticalLayout_25.addWidget(self.stackedWidget)


        self.verticalLayout_24.addWidget(self.frm_status_progress)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.main_frame)


        self.horizontalLayout_11.addWidget(self.frame_central)

        WindowAddEmailOperator.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(WindowAddEmailOperator)
        self.statusBar.setObjectName(u"statusBar")
        WindowAddEmailOperator.setStatusBar(self.statusBar)

        self.retranslateUi(WindowAddEmailOperator)
        self.toggle_menu_btn.toggled.connect(self.frame_only_icons.setVisible)
        self.toggle_menu_btn.toggled.connect(self.frame_full_menu.setHidden)
        self.btn_page_add_email_operator_2.toggled.connect(self.btn_page_add_email_operator.setChecked)
        self.btn_page_add_email_operator.toggled.connect(self.btn_page_add_email_operator_2.setChecked)
        self.btn_page_add_emails_region_2.toggled.connect(self.btn_page_add_emails_region.setChecked)
        self.btn_page_add_emails_region.toggled.connect(self.btn_page_add_emails_region_2.setChecked)
        self.btn_page_pandas_html_load_2.toggled.connect(self.btn_page_pandas_html_load.setChecked)
        self.btn_page_pandas_html_load.toggled.connect(self.btn_page_pandas_html_load_2.setChecked)
        self.admin__btn_log_2.toggled.connect(self.admin__btn_log.setChecked)
        self.admin__btn_log.toggled.connect(self.admin__btn_log_2.setChecked)
        self.admin__btn_upload_all_emails_2.toggled.connect(self.admin__btn_upload_all_emails.setChecked)
        self.admin__btn_upload_all_emails.toggled.connect(self.admin__btn_upload_all_emails_2.setChecked)
        self.admin__btn_download_all_emails_2.toggled.connect(self.admin__btn_download_all_emails.setChecked)
        self.admin__btn_download_all_emails.toggled.connect(self.admin__btn_download_all_emails_2.setChecked)
        self.admin__btn_statistics_2.toggled.connect(self.admin__btn_statistics.setChecked)
        self.admin__btn_statistics.toggled.connect(self.admin__btn_statistics_2.setChecked)

        self.stackedWidget.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(1)
        self.statistics_stackedWidget.setCurrentIndex(0)
        self.inc_stat_toolBox.setCurrentIndex(0)
        self.inc_stat_toolBox.layout().setSpacing(5)


        QMetaObject.connectSlotsByName(WindowAddEmailOperator)
    # setupUi

    def retranslateUi(self, WindowAddEmailOperator):
        WindowAddEmailOperator.setWindowTitle(QCoreApplication.translate("WindowAddEmailOperator", u"MainWindow", None))
        self.ledit_page.setText(QCoreApplication.translate("WindowAddEmailOperator", u"0", None))
        self.ledit_statistics_page.setText(QCoreApplication.translate("WindowAddEmailOperator", u"0", None))
        self.main_header_frame.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430\u043c\u0438", None))
        self.btn_minimazed.setText("")
        self.btn_maximazed.setText("")
        self.btn_close.setText("")
        self.stat_inc_grb.setTitle(QCoreApplication.translate("WindowAddEmailOperator", u"\u0418\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.label_8.setText("")
        self.label_19.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0412\u0441\u0435\u0433\u043e:", None))
        self.total_inc_lbl.setText(QCoreApplication.translate("WindowAddEmailOperator", u"10", None))
        self.stat_operators_grb.setTitle(QCoreApplication.translate("WindowAddEmailOperator", u"\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u0432", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0412\u0441\u0435\u0433\u043e:", None))
        self.operators_total_lbl.setText(QCoreApplication.translate("WindowAddEmailOperator", u"100", None))
        self.label_25.setText("")
        self.label_29.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421 E-mail:", None))
        self.operators_total_emails_lbl.setText(QCoreApplication.translate("WindowAddEmailOperator", u"100", None))
        self.label_30.setText("")
        self.label_31.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0411\u0435\u0437 E-mail:", None))
        self.operators_total_out_emails_lbl.setText(QCoreApplication.translate("WindowAddEmailOperator", u"100", None))
        self.stat_users_grb.setTitle(QCoreApplication.translate("WindowAddEmailOperator", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.label_27.setText("")
        self.label_32.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0412\u0441\u0435\u0433\u043e:", None))
        self.users_total_lbl.setText(QCoreApplication.translate("WindowAddEmailOperator", u"10", None))
        self.loading_lbl.setText("")
#if QT_CONFIG(tooltip)
        self.toggle_menu_btn.setToolTip(QCoreApplication.translate("WindowAddEmailOperator", u"\u041c\u0435\u043d\u044e", None))
#endif // QT_CONFIG(tooltip)
        self.toggle_menu_btn.setText("")
        self.btn_page_add_email_operator_2.setText("")
        self.btn_page_add_emails_region_2.setText("")
        self.btn_page_pandas_html_load_2.setText("")
        self.admin__btn_log_2.setText("")
        self.admin__btn_upload_all_emails_2.setText("")
        self.admin__btn_download_all_emails_2.setText("")
#if QT_CONFIG(tooltip)
        self.admin__btn_statistics_2.setToolTip(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.admin__btn_statistics_2.setText("")
        self.btn_page_add_email_operator.setText(QCoreApplication.translate("WindowAddEmailOperator", u"   \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c E-mail", None))
        self.btn_page_add_emails_region.setText(QCoreApplication.translate("WindowAddEmailOperator", u"   \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c E-mail \u0440\u0435\u0433\u0438\u043e\u043d\u0430", None))
        self.btn_page_pandas_html_load.setText(QCoreApplication.translate("WindowAddEmailOperator", u"   \u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u0420\u043e\u0441\u0441\u0440\u0435\u0435\u0441\u0442\u0440", None))
        self.admin__btn_log.setText(QCoreApplication.translate("WindowAddEmailOperator", u"   \u041b\u043e\u0433 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439", None))
        self.admin__btn_upload_all_emails.setText(QCoreApplication.translate("WindowAddEmailOperator", u"   \u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u0441\u0435 e-mail", None))
        self.admin__btn_download_all_emails.setText(QCoreApplication.translate("WindowAddEmailOperator", u"   \u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u0441\u0435 e-mail", None))
        self.admin__btn_statistics.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_operator.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430:", None))
        self.cb_list_operators.setCurrentText("")
        self.label_4.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430 \u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0432 \u043f\u043e\u043b\u0435 \u0432\u044b\u0448\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430.", None))
        self.labelOperatorID.setText("")
        self.btn_add_field_email_operator.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c E-mail", None))
        self.btn_save_emails_operator.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_44.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u043b\u044f \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430 - ", None))
        self.lbl_operator.setText("")
        self.label.setText(QCoreApplication.translate("WindowAddEmailOperator", u"   \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043e SP:", None))
        self.count_sp.setText("")
        ___qtablewidgetitem = self.sp_operator.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WindowAddEmailOperator", u"SP", None));
        ___qtablewidgetitem1 = self.sp_operator.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041c\u0435\u0441\u0442\u043e \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None));
        self.label_24.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0412\u0441\u0435\u0433\u043e \u0440\u0435\u0433\u0438\u043e\u043d\u043e\u0432:", None))
        self.count_regions.setText("")
        ___qtablewidgetitem2 = self.emails_region.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0420\u0435\u0433\u0438\u043e\u043d", None));
        ___qtablewidgetitem3 = self.emails_region.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WindowAddEmailOperator", u"E-mail", None));
        self.btn_save_emails_region.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_export_regions.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c E-mail \u0440\u0435\u0433\u0438\u043e\u043d\u043e\u0432", None))
        self.label_region.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0435\u0433\u0438\u043e\u043d:", None))
#if QT_CONFIG(tooltip)
        self.btn_change_name_region.setToolTip(QCoreApplication.translate("WindowAddEmailOperator", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0433\u0438\u043e\u043d\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_change_name_region.setText("")
        self.cb_list_regions.setCurrentText("")
        self.label_23.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0440\u0435\u0433\u0438\u043e\u043d\u0430 \u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0432 \u043f\u043e\u043b\u0435 \u0432\u044b\u0448\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0433\u0438\u043e\u043d\u0430.", None))
        self.labelRegionID.setText("")
        self.lbl_selected_region.setText("")
        self.btn_add_field_email_region.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c E-mail", None))
        self.btn_pandas_upload.setText(QCoreApplication.translate("WindowAddEmailOperator", u"  \u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u0420\u043e\u0441\u0441\u0440\u0435\u0435\u0441\u0442\u0440\u0430", None))
        self.label_17.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.label_18.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0417\u043e\u043d\u0430 \u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.label_14.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041c\u0435\u0441\u0442\u043e \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.label_16.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u0435\u043a\u0430\u0434\u043d\u044b\u0439", None))
        self.label_20.setText(QCoreApplication.translate("WindowAddEmailOperator", u"ABC/DEF", None))
        self.label_15.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u044b\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRossreestr), QCoreApplication.translate("WindowAddEmailOperator", u"\u0420\u043e\u0441\u0441\u0440\u0435\u0435\u0441\u0442\u0440", None))
        self.btn_upload_mgmn_outlook.setText(QCoreApplication.translate("WindowAddEmailOperator", u"  \u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u0442\u0440\u0430\u043d\u043a\u0433\u0440\u0443\u043f\u043f \u041c\u0433\u041c\u043d  ", None))
        self.label_2.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440", None))
        self.label_9.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0440\u0430\u043d\u043a\u0430", None))
        self.label_6.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0420\u0435\u0433\u0438\u043e\u043d \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440\u0430", None))
        self.label_13.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0420\u0435\u0433\u0438\u043e\u043d \u0448\u043b\u044e\u0437\u0430", None))
        self.label_5.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0442\u0440\u0430\u043d\u043a\u0430", None))
        self.label_10.setText(QCoreApplication.translate("WindowAddEmailOperator", u"OPC / IP A", None))
        self.label_12.setText(QCoreApplication.translate("WindowAddEmailOperator", u"DPC / IP B", None))
        self.label_11.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u0440\u0438\u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOutlook), QCoreApplication.translate("WindowAddEmailOperator", u"Outlook", None))
        self.lbl_log_and_admin.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041b\u043e\u0433\u0438 \u0438 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u044b", None))
        self.label_43.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0424\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.status.setPlaceholderText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041f\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f\u043c", None))
        self.creator.setPlaceholderText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041f\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c", None))
        self.label_28.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421:", None))
        self.date_create__start.setDisplayFormat(QCoreApplication.translate("WindowAddEmailOperator", u"dd-MM-yyyy", None))
        self.label_26.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041f\u043e:", None))
        self.date_create__end.setDisplayFormat(QCoreApplication.translate("WindowAddEmailOperator", u"dd-MM-yyyy", None))
        self.btn_delete_row_log.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.btn_clear_log.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u041b\u043e\u0433", None))
        self.lbl_admins.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u044b", None))
        self.btn_add_admin.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.title_inc_lbl.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0418\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u044b", None))
        self.label_7.setText(QCoreApplication.translate("WindowAddEmailOperator", u"Users", None))
#if QT_CONFIG(tooltip)
        self.btn_delete_inc.setToolTip(QCoreApplication.translate("WindowAddEmailOperator", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0435 \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.btn_delete_inc.setText("")
        self.label_3.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0418\u043d\u0446\u0438\u0434\u0435\u043d\u0442", None))
        self.le_inc_stat.setPlaceholderText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041d\u043e\u043c\u0435\u0440 \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0430", None))
        self.grb_status_inc.setTitle(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0430:", None))
        self.lbl_status_inc_stat.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0417\u0430\u043a\u0440\u044b\u0442", None))
        self.label_36.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.lbl_operator_stat_inc.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440 \u0438\u0437 \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0430", None))
        self.label_33.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.cb_type_operator.setItemText(0, QCoreApplication.translate("WindowAddEmailOperator", u"\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.cb_type_operator.setItemText(1, QCoreApplication.translate("WindowAddEmailOperator", u"\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0441\u0435\u0433\u043c\u0435\u043d\u0442", None))
        self.cb_type_operator.setItemText(2, QCoreApplication.translate("WindowAddEmailOperator", u"\u041c\u0433\u041c\u043d \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))

        self.label_37.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0417\u043e\u043d\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430:", None))
        self.lbl_location_operator_stat.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0417\u043e\u043d\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.label_35.setText(QCoreApplication.translate("WindowAddEmailOperator", u"DPC", None))
        self.le_dpc_stat.setPlaceholderText(QCoreApplication.translate("WindowAddEmailOperator", u"DPC", None))
        self.label_34.setText(QCoreApplication.translate("WindowAddEmailOperator", u"OPC", None))
        self.le_opc_stat.setPlaceholderText(QCoreApplication.translate("WindowAddEmailOperator", u"OPC", None))
        self.label_38.setText(QCoreApplication.translate("WindowAddEmailOperator", u"E-mail \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.inc_stat_toolBox.setItemText(self.inc_stat_toolBox.indexOf(self.page), QCoreApplication.translate("WindowAddEmailOperator", u"\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0443", None))
        self.label_40.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u0432 Remedy:", None))
        self.lbl_link_inc.setText("")
        self.label_41.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430 \u0430\u0432\u0430\u0440\u0438\u0438:", None))
        self.lbl_cause_inc_stat.setText("")
        self.label_39.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438:", None))
        self.lbl_source_inc_stat.setText("")
        self.label_42.setText(QCoreApplication.translate("WindowAddEmailOperator", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442:", None))
        self.inc_stat_toolBox.setItemText(self.inc_stat_toolBox.indexOf(self.page_2), QCoreApplication.translate("WindowAddEmailOperator", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u0438\u043d\u0446\u0438\u0434\u0435\u043d\u0442\u0443", None))
    # retranslateUi

