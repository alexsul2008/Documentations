# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArendatorWindowvkKIwU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resurce_rc

class Ui_ArendatorWindow(object):
    def setupUi(self, ArendatorWindow):
        if not ArendatorWindow.objectName():
            ArendatorWindow.setObjectName(u"ArendatorWindow")
        ArendatorWindow.resize(900, 940)
        ArendatorWindow.setMinimumSize(QSize(900, 940))
        ArendatorWindow.setMaximumSize(QSize(900, 940))
        ArendatorWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(ArendatorWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 10, 0, 5)
        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 878, 458))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, 20, 0)
        self.driving_license = QCheckBox(self.scrollAreaWidgetContents)
        self.driving_license.setObjectName(u"driving_license")
        self.driving_license.setMinimumSize(QSize(0, 30))
        self.driving_license.setMaximumSize(QSize(16777215, 30))
        self.driving_license.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.driving_license, 0, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(65, 0))
        self.label.setMaximumSize(QSize(65, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.rb_rf = QRadioButton(self.scrollAreaWidgetContents)
        self.rb_rf.setObjectName(u"rb_rf")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_rf.sizePolicy().hasHeightForWidth())
        self.rb_rf.setSizePolicy(sizePolicy)
        self.rb_rf.setMinimumSize(QSize(220, 30))
        self.rb_rf.setMaximumSize(QSize(220, 30))
        self.rb_rf.setCursor(QCursor(Qt.PointingHandCursor))
        self.rb_rf.setChecked(True)

        self.gridLayout.addWidget(self.rb_rf, 0, 1, 1, 1)

        self.le_country = QLineEdit(self.scrollAreaWidgetContents)
        self.le_country.setObjectName(u"le_country")
        self.le_country.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.le_country, 1, 2, 1, 1)

        self.rb_inostran = QRadioButton(self.scrollAreaWidgetContents)
        self.rb_inostran.setObjectName(u"rb_inostran")
        sizePolicy.setHeightForWidth(self.rb_inostran.sizePolicy().hasHeightForWidth())
        self.rb_inostran.setSizePolicy(sizePolicy)
        self.rb_inostran.setMinimumSize(QSize(220, 30))
        self.rb_inostran.setMaximumSize(QSize(220, 30))
        self.rb_inostran.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.rb_inostran, 1, 1, 1, 1)

        self.lbl_arendator_id = QLabel(self.scrollAreaWidgetContents)
        self.lbl_arendator_id.setObjectName(u"lbl_arendator_id")
        self.lbl_arendator_id.setMinimumSize(QSize(20, 20))
        self.lbl_arendator_id.setMaximumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.lbl_arendator_id, 1, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 20, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(65, 26))
        self.label_2.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.le_seria_pasport = QLineEdit(self.groupBox_2)
        self.le_seria_pasport.setObjectName(u"le_seria_pasport")
        self.le_seria_pasport.setMinimumSize(QSize(90, 30))
        self.le_seria_pasport.setMaximumSize(QSize(90, 30))
        self.le_seria_pasport.setMaxLength(20)
        self.le_seria_pasport.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.le_seria_pasport)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 0))
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.le_number_pasport = QLineEdit(self.groupBox_2)
        self.le_number_pasport.setObjectName(u"le_number_pasport")
        self.le_number_pasport.setMinimumSize(QSize(150, 30))
        self.le_number_pasport.setMaximumSize(QSize(150, 30))
        self.le_number_pasport.setMaxLength(20)

        self.horizontalLayout.addWidget(self.le_number_pasport)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))
        self.label_4.setMaximumSize(QSize(50, 16777215))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.de_date_pasport = QDateEdit(self.groupBox_2)
        self.de_date_pasport.setObjectName(u"de_date_pasport")
        self.de_date_pasport.setMinimumSize(QSize(120, 30))
        self.de_date_pasport.setMaximumSize(QSize(120, 30))
        self.de_date_pasport.setCursor(QCursor(Qt.PointingHandCursor))
        self.de_date_pasport.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.de_date_pasport)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 26))
        self.label_5.setMaximumSize(QSize(120, 16777215))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.le_code_division = QLineEdit(self.groupBox_2)
        self.le_code_division.setObjectName(u"le_code_division")
        self.le_code_division.setMinimumSize(QSize(160, 30))
        self.le_code_division.setMaximumSize(QSize(16777215, 30))
        self.le_code_division.setInputMethodHints(Qt.ImhDigitsOnly)
        self.le_code_division.setMaxLength(20)
        self.le_code_division.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.le_code_division)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(65, 0))
        self.label_6.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_3.addWidget(self.label_6)

        self.le_who_issued = QLineEdit(self.groupBox_2)
        self.le_who_issued.setObjectName(u"le_who_issued")
        self.le_who_issued.setMinimumSize(QSize(0, 30))
        self.le_who_issued.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.le_who_issued)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.label_7)

        self.le_surname = QLineEdit(self.groupBox_3)
        self.le_surname.setObjectName(u"le_surname")
        self.le_surname.setMinimumSize(QSize(0, 30))
        self.le_surname.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.le_surname)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_8)

        self.le_name = QLineEdit(self.groupBox_3)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setMinimumSize(QSize(0, 30))
        self.le_name.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.le_name)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label_9)

        self.le_last_name = QLineEdit(self.groupBox_3)
        self.le_last_name.setObjectName(u"le_last_name")
        self.le_last_name.setMinimumSize(QSize(0, 30))
        self.le_last_name.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.le_last_name)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 10)
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.label_10)

        self.de_date_birthday = QDateEdit(self.groupBox_3)
        self.de_date_birthday.setObjectName(u"de_date_birthday")
        self.de_date_birthday.setMinimumSize(QSize(120, 30))
        self.de_date_birthday.setMaximumSize(QSize(120, 30))
        self.de_date_birthday.setCursor(QCursor(Qt.PointingHandCursor))
        self.de_date_birthday.setProperty("showGroupSeparator", False)
        self.de_date_birthday.setDateTime(QDateTime(QDate(2000, 1, 31), QTime(0, 0, 0)))
        self.de_date_birthday.setCalendarPopup(True)

        self.horizontalLayout_7.addWidget(self.de_date_birthday)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 26))

        self.verticalLayout_9.addWidget(self.label_11)

        self.le_address_registration = QLineEdit(self.groupBox_3)
        self.le_address_registration.setObjectName(u"le_address_registration")
        self.le_address_registration.setMinimumSize(QSize(0, 30))

        self.verticalLayout_9.addWidget(self.le_address_registration)


        self.verticalLayout_3.addLayout(self.verticalLayout_9)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 26))

        self.verticalLayout_4.addWidget(self.label_12)

        self.le_address_residence = QLineEdit(self.groupBox_3)
        self.le_address_residence.setObjectName(u"le_address_residence")
        self.le_address_residence.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.le_address_residence)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addWidget(self.groupBox_3, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(370, 0))
        self.scrollArea.setMaximumSize(QSize(370, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scroll_phones_arendator = QWidget()
        self.scroll_phones_arendator.setObjectName(u"scroll_phones_arendator")
        self.scroll_phones_arendator.setGeometry(QRect(0, 0, 368, 278))
        self.scroll_phones_arendator.setMinimumSize(QSize(0, 0))
        self.scroll_phones_arendator.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.scroll_phones_arendator)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.phones_arendator_layout = QVBoxLayout()
        self.phones_arendator_layout.setSpacing(5)
        self.phones_arendator_layout.setObjectName(u"phones_arendator_layout")
        self.phones_arendator_layout.setContentsMargins(-1, -1, 0, 0)

        self.verticalLayout_2.addLayout(self.phones_arendator_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scroll_phones_arendator)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.frm_save = QFrame(self.centralwidget)
        self.frm_save.setObjectName(u"frm_save")
        self.frm_save.setMinimumSize(QSize(0, 0))
        self.frm_save.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_18 = QHBoxLayout(self.frm_save)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 28, 15)
        self.btn_save = QPushButton(self.frm_save)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(400, 40))
        self.btn_save.setMaximumSize(QSize(16777215, 16777215))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.btn_save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.chb_flag_cliced_new_contract = QCheckBox(self.frm_save)
        self.chb_flag_cliced_new_contract.setObjectName(u"chb_flag_cliced_new_contract")
        self.chb_flag_cliced_new_contract.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_18.addWidget(self.chb_flag_cliced_new_contract)

        self.btn_new_contract = QPushButton(self.frm_save)
        self.btn_new_contract.setObjectName(u"btn_new_contract")
        self.btn_new_contract.setMinimumSize(QSize(150, 40))
        self.btn_new_contract.setMaximumSize(QSize(16777215, 16777215))
        self.btn_new_contract.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.btn_new_contract)


        self.verticalLayout_7.addWidget(self.frm_save)

        self.scrollArea_3 = QScrollArea(self.centralwidget)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 380))
        self.scrollArea_3.setMaximumSize(QSize(16777215, 380))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 878, 378))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.layoutNewFormCreateContract = QVBoxLayout()
        self.layoutNewFormCreateContract.setSpacing(0)
        self.layoutNewFormCreateContract.setObjectName(u"layoutNewFormCreateContract")
        self.layoutNewFormCreateContract.setContentsMargins(-1, -1, 0, -1)

        self.verticalLayout_6.addLayout(self.layoutNewFormCreateContract)

        self.layoutItemFormContract = QVBoxLayout()
        self.layoutItemFormContract.setSpacing(5)
        self.layoutItemFormContract.setObjectName(u"layoutItemFormContract")
        self.layoutItemFormContract.setContentsMargins(-1, -1, 0, -1)

        self.verticalLayout_6.addLayout(self.layoutItemFormContract)

        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_3)

        ArendatorWindow.setCentralWidget(self.centralwidget)
        self.scrollArea_2.raise_()
        self.scrollArea_3.raise_()
        self.frm_save.raise_()
        self.statusBar = QStatusBar(ArendatorWindow)
        self.statusBar.setObjectName(u"statusBar")
        ArendatorWindow.setStatusBar(self.statusBar)

        self.retranslateUi(ArendatorWindow)

        QMetaObject.connectSlotsByName(ArendatorWindow)
    # setupUi

    def retranslateUi(self, ArendatorWindow):
        ArendatorWindow.setWindowTitle(QCoreApplication.translate("ArendatorWindow", u"MainWindow", None))
        self.driving_license.setText(QCoreApplication.translate("ArendatorWindow", u"\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0435 \u0443\u0434\u043e\u0441\u0442\u043e\u0432\u0435\u0440\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("ArendatorWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442", None))
#if QT_CONFIG(accessibility)
        self.rb_rf.setAccessibleName(QCoreApplication.translate("ArendatorWindow", u"pasport", None))
#endif // QT_CONFIG(accessibility)
        self.rb_rf.setText(QCoreApplication.translate("ArendatorWindow", u"\u0413\u0440\u0430\u0436\u0434\u0430\u043d\u0438\u043d \u0420\u0424", None))
#if QT_CONFIG(accessibility)
        self.rb_inostran.setAccessibleName(QCoreApplication.translate("ArendatorWindow", u"pasport", None))
#endif // QT_CONFIG(accessibility)
        self.rb_inostran.setText(QCoreApplication.translate("ArendatorWindow", u"\u0418\u043d\u043e\u0441\u0442\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0430", None))
        self.lbl_arendator_id.setText("")
        self.groupBox_2.setTitle("")
        self.label_2.setText(QCoreApplication.translate("ArendatorWindow", u"\u0421\u0435\u0440\u0438\u044f", None))
        self.le_seria_pasport.setInputMask("")
        self.label_3.setText(QCoreApplication.translate("ArendatorWindow", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.le_number_pasport.setInputMask("")
        self.label_4.setText(QCoreApplication.translate("ArendatorWindow", u"\u0412\u044b\u0434\u0430\u043d", None))
        self.label_5.setText(QCoreApplication.translate("ArendatorWindow", u"\u041a\u043e\u0434 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.le_code_division.setInputMask("")
        self.label_6.setText(QCoreApplication.translate("ArendatorWindow", u"\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d", None))
        self.groupBox_3.setTitle("")
        self.label_7.setText(QCoreApplication.translate("ArendatorWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("ArendatorWindow", u"\u0418\u043c\u044f", None))
        self.label_9.setText(QCoreApplication.translate("ArendatorWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_10.setText(QCoreApplication.translate("ArendatorWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("ArendatorWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.label_12.setText(QCoreApplication.translate("ArendatorWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.btn_save.setText(QCoreApplication.translate("ArendatorWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.chb_flag_cliced_new_contract.setText("")
        self.btn_new_contract.setText(QCoreApplication.translate("ArendatorWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
    # retranslateUi

