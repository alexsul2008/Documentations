# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLineEdit, QCheckBox, QSpacerItem, QMessageBox, QGraphicsBlurEffect, QGroupBox, \
	QRadioButton, QApplication, QLabel

from Core.Models.Worker import Usuarios
from Core.Utils.utils import enabled_elements
from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications

from ui.pages.windowArendator import ArendatorWindow
from ui.pages.windowHistoryPayments import HistoryPaymentsWindow
from ui.widjets.baseItemArendator_widget import BaseItemArendatorWidget

from ui.windows.ui_ArendatorsListWindow import Ui_ArendatorsListWindow

from ui.widjets.itemListArendator_widget import ItemListArendatorWidget





class AllArendatorsWindow(QMainWindow):

	def __init__(self, parent=None, role=None):
		super(AllArendatorsWindow, self).__init__(parent)
		self.ui = Ui_ArendatorsListWindow()
		self.ui.setupUi(self)

		self.count_item_base_list_arendator: int = 0

		self.parent = parent
		self.role = role

		self.base_list_arendators = self.parent.users_db.base_list_arendators()
		self.loadingBaseListArendators(self.base_list_arendators)

		enabled_elements(role = self.role, element = self.ui.groupBox, hideted = 'yes')

		if self.role in ['root', 'admin']:
			width_lbl = self.ui.lbl_indent_elements.width()
			self.ui.lbl_indent_elements.setMinimumWidth(int(width_lbl + 45))

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
		# print(f'filter_layout: {filter_layout}')

		self.base_list_arendators = self.parent.users_db.base_list_arendators(filters_arendators=filter_layout)
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

		self.parent.statusBar().showMessage(f"Выбрано клиентов: {item_arendators.count()}")



	@pyqtSlot()
	def histored_paymentswidjet(self):
		widget = self.sender()
		self.parent.effect.setEnabled(True)
		list_histored_payment = HistoryPaymentsWindow(ids_arendator=int(widget.ui.lbl_id_arendator.text()), parent=self.parent)
		list_histored_payment.show()

	# @pyqtSlot()
	def hidened_arendatorwidjet(self, status):
		widget = self.sender()
		self.parent.effect.setEnabled(True)

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
			self.parent.effect.setEnabled(False)

			if self.role not in ['root', 'admin']:
				self.ui.arendators_base_layout.removeWidget(widget)
				widget.deleteLater()
				widget.destroy()

			responce = self.parent.users_db.hidened_arendator(ids=widget.ui.lbl_id_arendator.text(), hidened = status)
			self.update()
			self.parent.responses.message_from_db(responce, self.parent.statusBar(), f'Клиент успешно отображен' if status else f'Клиент успешно '
																															   f'скрыт')

		elif self.msg.clickedButton() == self.buttonCancelar:
			self.parent.effect.setEnabled(False)
			self.msg.close()
		else:
			self.parent.effect.setEnabled(False)
			self.msg.close()


	@pyqtSlot()
	def delete_arendatorwidget(self):
		widget = self.sender()
		self.parent.effect.setEnabled(True)

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
			self.parent.effect.setEnabled(False)

			self.ui.arendators_base_layout.removeWidget(widget)

			responce = self.parent.users_db.delete_arendator(ids=widget.ui.lbl_id_arendator.text())
			widget.deleteLater()
			widget.destroy()

			self.parent.responses.message_from_db(responce, self.parent.statusBar(), f'Клиент успешно удален')

		elif self.msg.clickedButton() == self.buttonCancelar:
			self.parent.effect.setEnabled(False)
			self.msg.close()
		else:
			self.parent.effect.setEnabled(False)
			self.msg.close()

	@pyqtSlot()
	def get_areandator_contracted(self):
		widget = self.sender()
		self.parent.effect.setEnabled(True)
		arendator_card = ArendatorWindow(id_arendator=int(widget.ui.lbl_id_arendator.text()), parent=self.parent, widget_list = self)
		arendator_card.show()

	@pyqtSlot()
	def update(self) -> None:
		# print('UPDATERRRRRRRRRRRRRRRRRRRR 2222222222222222')
		# self.loadingBaseListArendators(self.base_list_arendators)
		self.base_list_arendators = self.parent.users_db.base_list_arendators()
		self.loadingBaseListArendators(self.base_list_arendators)

