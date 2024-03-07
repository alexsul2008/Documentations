# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QGraphicsBlurEffect, QSpacerItem, QLineEdit, QGroupBox, QRadioButton, QLabel, QComboBox

from Core.Models.Worker import Usuarios
from Core.Utils.utils import enabled_elements
from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications
from ui.pages.windowAllArendators import AllArendatorsWindow

from ui.pages.windowArendator import ArendatorWindow
from ui.pages.windowHistoryPayments import HistoryPaymentsWindow
from ui.widjets.baseItemArendator_widget import BaseItemArendatorWidget
from ui.widjets.baseMenu_widget import ListBtnMenu
from ui.widjets.formCharts_widget import BaseFormCharts

from ui.windows.ui_MainWindow import Ui_MainWindow


# for w in QtWidgets.QApplication.topLevelWidgets():
# 	if isinstance(w, QtWidgets.QMessageBox) and w.parent() == self:
# 		for button in w.buttons():
# 			button.setCursor(QCursor(Qt.PointingHandCursor))
# 	elif isinstance(w, QtWidgets.QFileDialog) and w.parent() == self:
# 		for button in w.findChildren(QtWidgets.QPushButton):
# 			button.setCursor(QCursor(Qt.PointingHandCursor))


class MainBaseWindow(QMainWindow):
	resizeBase = pyqtSignal()

	def __init__(self, user_fields=None, parent=None):
		super(MainBaseWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.statusBar().setStyleSheet('color: #ffffff;')
		self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
		self.setWindowTitle(f'Программа по учету ТС и заключенных договорах')


		# Выравнивание окна по центру монитора
		desktop = QApplication.desktop()
		x = (desktop.width() - self.frameSize().width()) // 2
		y = (desktop.height() - self.frameSize().height()) // 2
		self.move(x, y)

		self.effect = QGraphicsBlurEffect()
		self.effect.setBlurRadius(4)
		self.setGraphicsEffect(self.effect)
		self.effect.setEnabled(False)

		self.parent = parent



		self.responses = Responses()
		self.verify = Verifications()

		self.users_db = Usuarios()

		self.user_fields = user_fields
		self.role = self.user_fields.role
		self.role_name = self.user_fields.role_name
		self.username = self.user_fields.username
		self.name = self.user_fields.name

		self.ui.lbl_name_user.setText(self.name)
		self.ui.lbl_role_name.setText(self.role_name)
		self.ui.role.setText(self.role)

		self.window_add_arendator = ArendatorWindow(parent=self)

		self.ui.btn_hamburger_menu.clicked.connect(self.menu_humburger)

		self.ui.tabWidget.setCurrentIndex(1)
		self.all_arendators = AllArendatorsWindow(parent = self, role = self.role)
		self.ui.layout_arendators_window.addWidget(self.all_arendators)

		self.chaarts = BaseFormCharts(parent=self)
		self.ui.charts_layout.addWidget(self.chaarts)

		self.ui.tabWidget.blockSignals(True)
		self.ui.tabWidget.currentChanged.connect(self.selectorTabBase)
		self.ui.tabWidget.blockSignals(False)



	def selectorTabBase(self, selected_index):
		# print(f'Selected: {selected_index}')
		if selected_index == 0:
			self.chaarts.updater()
		elif selected_index == 1:
			pass
		elif selected_index == 2:
			pass


	def menu_humburger(self):
		if self.ui.btn_hamburger_menu.isChecked():
			self.hamburger = ListBtnMenu(self, self.ui.frm_top, role=self.role)
			self.hamburger.resize_menu()
			self.hamburger.show()
		else:
			self.hamburger.close()

	def keyPressEvent(self, e):
		if self.ui.btn_hamburger_menu.isChecked():
			self.ui.btn_hamburger_menu.setChecked(False)
		if e.key() == Qt.Key_Escape:
			self.hamburger.close()

	def resizeEvent(self, event):
		self.resizeBase.emit()
		return super(MainBaseWindow, self).resizeEvent(event)

	def closeEvent (self, event):
		for window in QApplication.topLevelWidgets():
			# print(f'Closed window: {window.objectName()}')
			window.close()












	# def eventFilter(self, obj, event):
	#
	# 	if obj == self.ui.frm_content and event.type() == event.Resize:
	# 		print("dock")
	# 		print(obj.objectName())
	# 		# print(self.hamburger.isHidden())
	# 	return super(MainBaseWindow, self).eventFilter(obj, event)



	# def eventFilter (self, obj, event):
	# 	if obj in {self.hamburger, self.centralWidget()} and event.type() == event.Resize:
	# 		print("dock")
	# 	return super().eventFilter(obj, event)

	# def event (self, e):
	# 	if e.type() == QEvent.Resize and e.type() == QEvent.ShowToParent:
	# 		# print(e.type())
	# 		self.hamburger.resize_menu(self)
	# 	return QMainWindow.event(self, e)



