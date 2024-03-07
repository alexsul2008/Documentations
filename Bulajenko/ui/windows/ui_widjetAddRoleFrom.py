# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widjetAddRoleFromfXolUy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_WidjetAddRoleForm(object):
    def setupUi(self, WidjetAddRoleForm):
        if not WidjetAddRoleForm.objectName():
            WidjetAddRoleForm.setObjectName(u"WidjetAddRoleForm")
        WidjetAddRoleForm.resize(586, 45)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidjetAddRoleForm.sizePolicy().hasHeightForWidth())
        WidjetAddRoleForm.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(WidjetAddRoleForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 2, 5, 2)
        self.groupBox = QGroupBox(WidjetAddRoleForm)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(0, 26))
        self.groupBox.setMaximumSize(QSize(16777215, 32))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 1)
        self.le_id = QLineEdit(self.groupBox)
        self.le_id.setObjectName(u"le_id")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_id.sizePolicy().hasHeightForWidth())
        self.le_id.setSizePolicy(sizePolicy2)
        self.le_id.setMinimumSize(QSize(40, 0))
        self.le_id.setMaximumSize(QSize(40, 16777215))
        self.le_id.setFocusPolicy(Qt.StrongFocus)
        self.le_id.setInputMethodHints(Qt.ImhNone)
        self.le_id.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_id)

        self.le_role = QLineEdit(self.groupBox)
        self.le_role.setObjectName(u"le_role")
        sizePolicy2.setHeightForWidth(self.le_role.sizePolicy().hasHeightForWidth())
        self.le_role.setSizePolicy(sizePolicy2)
        self.le_role.setMinimumSize(QSize(70, 0))
        self.le_role.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.le_role, 0, Qt.AlignLeft)

        self.le_name = QLineEdit(self.groupBox)
        self.le_name.setObjectName(u"le_name")
        sizePolicy2.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy2)
        self.le_name.setMinimumSize(QSize(130, 0))
        self.le_name.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.le_name)

        self.btn_save = QPushButton(self.groupBox)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy3)
        self.btn_save.setMinimumSize(QSize(60, 0))
        self.btn_save.setMaximumSize(QSize(60, 16777215))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/save_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_delete = QPushButton(self.groupBox)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy3.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy3)
        self.btn_delete.setMinimumSize(QSize(60, 0))
        self.btn_delete.setMaximumSize(QSize(60, 16777215))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/trash-2_.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.gbx_msg = QGroupBox(WidjetAddRoleForm)
        self.gbx_msg.setObjectName(u"gbx_msg")
        sizePolicy1.setHeightForWidth(self.gbx_msg.sizePolicy().hasHeightForWidth())
        self.gbx_msg.setSizePolicy(sizePolicy1)
        self.layout_msg = QHBoxLayout(self.gbx_msg)
        self.layout_msg.setSpacing(5)
        self.layout_msg.setObjectName(u"layout_msg")
        self.layout_msg.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gbx_msg)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(40, 16777215))

        self.layout_msg.addWidget(self.label)

        self.lbl_msg = QLabel(self.gbx_msg)
        self.lbl_msg.setObjectName(u"lbl_msg")
        sizePolicy1.setHeightForWidth(self.lbl_msg.sizePolicy().hasHeightForWidth())
        self.lbl_msg.setSizePolicy(sizePolicy1)

        self.layout_msg.addWidget(self.lbl_msg)


        self.verticalLayout.addWidget(self.gbx_msg)


        self.retranslateUi(WidjetAddRoleForm)

        QMetaObject.connectSlotsByName(WidjetAddRoleForm)
    # setupUi

    def retranslateUi(self, WidjetAddRoleForm):
        WidjetAddRoleForm.setWindowTitle(QCoreApplication.translate("WidjetAddRoleForm", u"Form", None))
        self.btn_save.setText("")
        self.btn_delete.setText("")
        self.label.setText("")
        self.lbl_msg.setText("")
    # retranslateUi

