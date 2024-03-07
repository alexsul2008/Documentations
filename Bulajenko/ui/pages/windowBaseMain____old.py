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

		self.count_item_base_list_arendator: int = 0

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

		# enabled_elements(role = self.role, element = self.ui.btn_user, hideted = 'yes')
		enabled_elements(role = self.role, element = self.ui.groupBox, hideted = 'yes')

		self.ui.btn_hamburger_menu.clicked.connect(self.menu_humburger)
		# self.ui.btn_user.clicked.connect(self.user_managers)

		self.base_list_arendators = self.users_db.base_list_arendators()
		self.loadingBaseListArendators(self.base_list_arendators)


		self.ui.cb_arendators.addItem('')
		self.ui.cb_arendators.addItem(f'ФИО от А до Я', 'surname___asc')
		self.ui.cb_arendators.addItem(f'ФИО от Я до А', 'surname___desc')
		self.ui.cb_arendators.addItem(f'Дата регистрации (по убывающей)', '___max_date')
		self.ui.cb_arendators.addItem(f'Дата регистрации (по возрастающей)', '___min_date')

		self.ui.surname___text.setPlaceholderText(u'Поиск клиента...')
		self.ui.surname___text.textChanged.connect(self.filters_in_db_arendators)

		self.ui.hiden_arendator__all.toggled.connect(self.filters_in_db_arendators)
		self.ui.hiden_arendator__active.toggled.connect(self.filters_in_db_arendators)
		self.ui.hiden_arendator__hidened.toggled.connect(self.filters_in_db_arendators)
		self.ui.cb_arendators.textActivated.connect(self.filters_in_db_arendators)


		if self.role in ['root', 'admin']:
			width_lbl = self.ui.lbl_indent_elements.width()
			self.ui.lbl_indent_elements.setMinimumWidth(int(width_lbl + 45))

		self.ui.tabWidget.setCurrentIndex(1)

		self.all_arendators = AllArendatorsWindow(parent = self)
		self.ui.layout_arendators_window.addWidget(self.all_arendators)

		self.chaarts = BaseFormCharts(parent=self)
		self.ui.charts_layout.addWidget(self.chaarts)

		self.ui.tabWidget.blockSignals(True)
		self.ui.tabWidget.currentChanged.connect(self.selectorTabBase)
		self.ui.tabWidget.blockSignals(False)

	def create_data_charts(self):
		# print(f'Из create_data_charts: {self.users_db.charts_data()}')
		result = self.users_db.charts_data()
		return result

	def selectorTabBase(self, selected_index):
		print(f'Selected: {selected_index}')
		if selected_index == 0:
			# self.chaarts.dataChanged.connect(self.chaarts.fierst_chart)
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
			window.close()


	def filters_in_db_arendators(self):

		filter_layout = {}
		def search_filter(layout):
			for i in reversed(range(layout.count())):
				layoutItem = layout.itemAt(i)

				if type(layoutItem) is QSpacerItem:
					continue

				if layoutItem.widget() is not None:
					widgetToFilter = layoutItem.widget()

					if isinstance(widgetToFilter, QLabel):
						continue

					if isinstance(widgetToFilter, QLineEdit):
						list_name_cut = widgetToFilter.objectName()
						data_filter = widgetToFilter.text()

					if isinstance(widgetToFilter, QGroupBox):
						for item in widgetToFilter.findChildren(QRadioButton):
							if item.isChecked():
								list_name_cut = item.objectName()
								data_filter = item.isChecked()

					if isinstance(widgetToFilter, QComboBox):
						list_name_cut = widgetToFilter.objectName()

						if widgetToFilter.currentData():
							data_filter = widgetToFilter.currentData()
						else:
							data_filter = widgetToFilter.currentText()

					filter_layout.update({list_name_cut: data_filter})

				else:
					layoutToFilter = layout.itemAt(i)
					search_filter(layoutToFilter)

		search_filter(self.ui.layoutSearchArendator)

		# self.list_new_transports = self.users_db.list_transport(filters=filter_cb)
		# print(f'filter_layout: {filter_layout}')

		self.base_list_arendators = self.users_db.base_list_arendators(filters_arendators=filter_layout)
		self.loadingBaseListArendators(self.base_list_arendators)


	def loadingBaseListArendators(self, list_arendators):
		if self.role in ['root', 'admin']:
			item_arendators = list_arendators['all_arendators']
		else:
			item_arendators = list_arendators['for_manadgers']

		while self.ui.arendators_base_layout.count() > 0:
			item = self.ui.arendators_base_layout.takeAt(0)
			item.widget().deleteLater()

		for item in item_arendators:
			self.count_item_base_list_arendator += 1
			item_arendator = BaseItemArendatorWidget(
				id_widget_base_item_arendator = self.count_item_base_list_arendator,
				id_arendator = item[0].id,
				hiden_arendator_db = item[0].hiden_arendator,
				count_contracts = item.count_conract,
				surname = item[0].surname,
				name = item[0].name,
				last_name = item[0].last_name,
				date_created = item[0].date_created,
				role = self.role,
				parent = self,
			)
			self.ui.arendators_base_layout.addWidget(item_arendator)
			item_arendator.clicked_arendator.connect(self.get_areandator_contracted)
			item_arendator.delete_arendator.connect(self.delete_arendatorwidget)
			item_arendator.hidened_arendator.connect(self.hidened_arendatorwidjet)
			item_arendator.histored_payments.connect(self.histored_paymentswidjet)

		self.statusBar().showMessage(f"Выбрано клиентов: {item_arendators.count()}")


	# def chartsBase(self):
	# 	result = self.users_db.charts_data()
	# 	print(result)
	# 	return result



	@pyqtSlot()
	def histored_paymentswidjet(self):
		widget = self.sender()
		self.effect.setEnabled(True)
		list_histored_payment = HistoryPaymentsWindow(ids_arendator=int(widget.ui.lbl_id_arendator.text()), parent=self)
		list_histored_payment.show()

	# @pyqtSlot()
	def hidened_arendatorwidjet(self, status):
		widget = self.sender()
		self.effect.setEnabled(True)

		self.msg = QMessageBox(self)
		self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
		self.msg.setIcon(QMessageBox.Question)
		self.msg.setWindowTitle("Отобразить клиента" if status else "Скрыть отображение клиента")
		self.msg.setText(
			f"Вы действительно хотите отобразить клиента {widget.ui.lbl_fio_arendator.text()} ?" if status else f"Вы действительно хотите скрыть клиента {widget.ui.lbl_fio_arendator.text()} ?")
		self.buttonAceptar = self.msg.addButton("Да, хочу", QMessageBox.YesRole)
		self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)
		self.msg.setDefaultButton(self.buttonAceptar)

		for button in self.msg.buttons():
			button.setCursor(QCursor(Qt.PointingHandCursor))
		self.msg.exec_()

		if self.msg.clickedButton() == self.buttonAceptar:
			self.effect.setEnabled(False)

			if self.role not in ['root', 'admin']:
				self.ui.arendators_base_layout.removeWidget(widget)
				widget.deleteLater()
				widget.destroy()

			responce = self.users_db.hidened_arendator(ids=widget.ui.lbl_id_arendator.text(), hidened = status)
			self.update()
			self.responses.message_from_db(responce, self.statusBar(), f'Клиент успешно отображен' if status else f'Клиент успешно скрыт')

		elif self.msg.clickedButton() == self.buttonCancelar:
			self.effect.setEnabled(False)
			self.msg.close()
		else:
			self.effect.setEnabled(False)
			self.msg.close()



	@pyqtSlot()
	def delete_arendatorwidget(self):
		widget = self.sender()
		self.effect.setEnabled(True)

		self.msg = QMessageBox(self)
		self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
		self.msg.setWindowTitle("Удаление учетной записи клиента")
		self.msg.setIcon(QMessageBox.Question)
		self.msg.setText(
			f"Вы действительно хотите удалить клиента {widget.ui.lbl_fio_arendator.text()} ?")

		self.buttonAceptar = self.msg.addButton("Да, хочу", QMessageBox.YesRole)
		self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)
		self.msg.setDefaultButton(self.buttonAceptar)

		for button in self.msg.buttons():
			button.setCursor(QCursor(Qt.PointingHandCursor))

		self.msg.exec_()

		if self.msg.clickedButton() == self.buttonAceptar:
			self.effect.setEnabled(False)

			self.ui.arendators_base_layout.removeWidget(widget)

			responce = self.users_db.delete_arendator(ids=widget.ui.lbl_id_arendator.text())
			widget.deleteLater()
			widget.destroy()

			self.responses.message_from_db(responce, self.statusBar(), f'Клиент успешно удален')

		elif self.msg.clickedButton() == self.buttonCancelar:
			self.effect.setEnabled(False)
			self.msg.close()
		else:
			self.effect.setEnabled(False)
			self.msg.close()

	@pyqtSlot()
	def get_areandator_contracted(self):
		widget = self.sender()
		self.effect.setEnabled(True)
		arendator_card = ArendatorWindow(id_arendator=int(widget.ui.lbl_id_arendator.text()), parent=self)
		arendator_card.show()

	@pyqtSlot()
	def update(self) -> None:
		print('UPDATERRRRRRRRRRRRRRRRRRRR 2222222222222222')
		# self.loadingBaseListArendators(self.base_list_arendators)
		self.base_list_arendators = self.users_db.base_list_arendators()
		self.loadingBaseListArendators(self.base_list_arendators)











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



