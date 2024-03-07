# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetIncidentsPSlkyG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_IncidentWidget(object):
    def setupUi(self, IncidentWidget):
        if not IncidentWidget.objectName():
            IncidentWidget.setObjectName(u"IncidentWidget")
        IncidentWidget.resize(286, 45)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IncidentWidget.sizePolicy().hasHeightForWidth())
        IncidentWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(IncidentWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 3)
        self.chb_inc = QCheckBox(IncidentWidget)
        self.chb_inc.setObjectName(u"chb_inc")
        self.chb_inc.setMinimumSize(QSize(0, 0))
        self.chb_inc.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.chb_inc)

        self.inc_frame = QFrame(IncidentWidget)
        self.inc_frame.setObjectName(u"inc_frame")
        self.inc_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.inc_frame.setFrameShape(QFrame.StyledPanel)
        self.inc_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.inc_frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.incident_lbl = QLabel(self.inc_frame)
        self.incident_lbl.setObjectName(u"incident_lbl")
        self.incident_lbl.setMinimumSize(QSize(150, 27))
        self.incident_lbl.setMaximumSize(QSize(16777215, 27))
        self.incident_lbl.setFrameShape(QFrame.StyledPanel)
        self.incident_lbl.setLineWidth(0)

        self.verticalLayout.addWidget(self.incident_lbl)

        self.operator_name = QLabel(self.inc_frame)
        self.operator_name.setObjectName(u"operator_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.operator_name.sizePolicy().hasHeightForWidth())
        self.operator_name.setSizePolicy(sizePolicy1)
        self.operator_name.setMinimumSize(QSize(0, 10))
        self.operator_name.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout.addWidget(self.operator_name)


        self.horizontalLayout.addWidget(self.inc_frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.id_incident_lbl = QLabel(IncidentWidget)
        self.id_incident_lbl.setObjectName(u"id_incident_lbl")
        self.id_incident_lbl.setMaximumSize(QSize(0, 16777215))

        self.horizontalLayout.addWidget(self.id_incident_lbl)


        self.retranslateUi(IncidentWidget)

        QMetaObject.connectSlotsByName(IncidentWidget)
    # setupUi

    def retranslateUi(self, IncidentWidget):
        IncidentWidget.setWindowTitle(QCoreApplication.translate("IncidentWidget", u"Form", None))
        self.chb_inc.setText("")
        self.incident_lbl.setText("")
        self.operator_name.setText(QCoreApplication.translate("IncidentWidget", u"\u0410\u041e \"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f \u0422\u0440\u0430\u043d\u0441\u0422\u0435\u043b\u0435\u041a\u043e\u043c\"", None))
        self.id_incident_lbl.setText(QCoreApplication.translate("IncidentWidget", u"100", None))
    # retranslateUi

