# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLineEdit, QCheckBox, QSpacerItem, QMessageBox, QGraphicsBlurEffect, QGroupBox, \
	QRadioButton, QApplication

from Core.Models.Worker import Usuarios
from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications

from ui.pages.windowArendator import ArendatorWindow

from ui.windows.ui_ListArendatorWindow import Ui_ListArendatorWindow

from ui.widjets.itemListArendator_widget import ItemListArendatorWidget





class ListArendatorsWindow(QMainWindow):

	def __init__(self, parent=None, role=None):
		super(ListArendatorsWindow, self).__init__(parent)
		self.ui = Ui_ListArendatorWindow()
		self.ui.setupUi(self)
		self.statusBar().setStyleSheet('color: #ffffff;')
		self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
		self.setWindowTitle(f'Арендаторы транспортных средств')

		# Выравнивание окна по центру монитора
		desktop = QApplication.desktop()
		x = (desktop.width() - self.frameSize().width()) // 2
		y = (desktop.height() - self.frameSize().height()) // 2
		self.move(x, y)




		self.parent = parent
		self.role = role

		self.effect = QGraphicsBlurEffect()
		self.effect.setBlurRadius(4)
		self.setGraphicsEffect(self.effect)
		self.effect.setEnabled(False)

		self.count_item_list_arendator: int = 0



		self.responses = Responses()
		self.verify = Verifications()

		self.users_db = Usuarios()


		self.list_arendators = self.users_db.list_arendators()

		self.loadingListArendators(self.list_arendators)


		self.ui.date_contract.addItem('')
		self.ui.date_contract.addItem(f'Дата договора с начала новые', '___max_date')
		self.ui.date_contract.addItem(f'Дата договора с начала старые', '___min_date')
		self.ui.date_contract.addItem(f'Цена ТС с начала дешевле', '___min_market_price')
		self.ui.date_contract.addItem(f'Цена ТС с начала дорогие', '___max_market_price')

		self.ui.fio_arendator__text.textChanged.connect(self.filters_fields_in_db)
		self.ui.id_dogovor.textChanged.connect(self.filters_fields_in_db)
		self.ui.vikup___ts.stateChanged.connect(self.filters_fields_in_db)
		self.ui.driving_license.stateChanged.connect(self.filters_fields_in_db)
		self.ui.dolg.stateChanged.connect(self.filters_fields_in_db)
		self.ui.date_contract.textActivated.connect(self.filters_fields_in_db)


		self.ui.status_contract___all.toggled.connect(self.filters_fields_in_db)
		self.ui.status_contract__open.toggled.connect(self.filters_fields_in_db)
		self.ui.status_contract__close.toggled.connect(self.filters_fields_in_db)

		self.ui.estimated_date___all.toggled.connect(self.filters_fields_in_db)
		self.ui.estimated_date___today.toggled.connect(self.filters_fields_in_db)
		self.ui.estimated_date___tomorrow.toggled.connect(self.filters_fields_in_db)

		self.ui.btn_clear_filter.clicked.connect(self.clear_all_filters)

		self.ui.btn_add_client.clicked.connect(self.add_new_client)




	def counter_simbols(self):
		if self.ui.fio_arendator__text.text().count('') > 4:
			self.filters_fields_in_db()


	def filters_fields_in_db(self):

		filter_layout = {}

		def search_filter(layout):
			# print(layout.count())
			list_name_cut = data_filter = None
			for i in reversed(range(layout.count())):
				layoutItem = layout.itemAt(i)
				if type(layoutItem) is QSpacerItem:
					continue

				if layoutItem.widget() is not None:
					widgetToFilter = layoutItem.widget()
					# print(widgetToFilter.objectName())
					if isinstance(widgetToFilter, QComboBox):
						list_name_cut = widgetToFilter.objectName()

						if widgetToFilter.currentData():
							data_filter = widgetToFilter.currentData()
						else:
							data_filter = widgetToFilter.currentText()

					if isinstance(widgetToFilter, QLineEdit):
						list_name_cut = widgetToFilter.objectName()
						data_filter = widgetToFilter.text()

					if isinstance(widgetToFilter, QCheckBox):
						list_name_cut = widgetToFilter.objectName()
						data_filter = widgetToFilter.isChecked()

					if isinstance(widgetToFilter, QGroupBox):
						for item in widgetToFilter.findChildren(QRadioButton):
							if item.isChecked():
								list_name_cut = item.objectName()
								data_filter = item.isChecked()

					filter_layout.update({list_name_cut: data_filter})

				else:
					layoutToFilter = layout.itemAt(i)
					search_filter(layoutToFilter)

		search_filter(self.ui.layoutFiltersContracts)
		# print(filter_layout)
		self.list_new_transports = self.users_db.list_arendators(filters_contract=filter_layout)
		self.loadingListArendators(self.list_new_transports)


	def loadingListArendators(self, list_arendators):

		while self.ui.listArendatorLayout.count() > 0:
			item = self.ui.listArendatorLayout.takeAt(0)
			item.widget().deleteLater()

		self.statusBar().showMessage(f'Выделено договоров: {list_arendators["all_arendators"].count()} шт.')

		print('Привет')

		for item in list_arendators['all_arendators']:
			self.count_item_list_arendator += 1
			item_arendator = ItemListArendatorWidget(
				id_widget_item_arendator_contracted = self.count_item_list_arendator,
				id_arendator = item.id_arendator,
				address_registration = item.arendatored.address_registration,
				address_residence = item.arendatored.address_residence,
				passport_country = item.arendatored.passport_country,
				serial_pasport = item.arendatored.serial_pasport,
				number_pasport = item.arendatored.number_pasport,
				date_pasport = item.arendatored.date_pasport,
				who_issued = item.arendatored.who_issued,
				date_birthday = item.arendatored.date_birthday,
				id_ts = item.id_ts,  #item.transported.id if item.transported != None else 0,
				id_contract = item.id,
				draft = item.draft,
				fio_arendator = item.fio_arendator,
				method_pay = item.method_pay,
				size_pay = item.size_pay,
				rental_period = item.rental_period,
				phone = item.arendatored.phoneses[0].phone if len(item.arendatored.phoneses) > 0 else 'None',
				phones = item.arendatored.phoneses,
				type_ts = item.transported.type_transported.name,  # if item.transported != None else 'None',
				vikup = item.transported.vikup,  # if item.transported != None else 'None',
				brand = item.transported.brand,  # if item.transported != None else 'None',
				model = item.transported.model,  # if item.transported != None else 'None',
				bodywork = item.transported.bodywork,  # if item.transported != None else 'None',
				engine_volume = item.transported.engine_volume,  # if item.transported != None else 'None',
				market_price = item.transported.market_price,  # if item.transported != None else 'None',
				color_ts = item.transported.colored.color,  # if item.transported != None else 'None',
				ts_color_name = item.transported.colored.name,  # if item.transported != None else 'None',
				set_date_contract = item.date_contract,
				date_closed_contract = item.date_closed_contract,
				optional_equipment = item.optional_equipment,
				status_contract = item.status_contract,
				dates_payments_next = item.dates_payments_next,
				parent = self,
				role = self.role
			)
			self.ui.listArendatorLayout.addWidget(item_arendator)
			item_arendator.close_contract.connect(self.set_closing_contract)
			item_arendator.clicked_arendator.connect(self.get_areandator_contracted)



	@pyqtSlot()
	def set_closing_contract(self):
		widget = self.sender()
		self.effect.setEnabled(True)

		self.msg = QMessageBox(self)
		self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
		self.msg.setWindowTitle("Закрытие договора транспортного средства")
		self.msg.setIcon(QMessageBox.Question)
		self.msg.setText(f"Вы действительно хотите закрыть договор {widget.ui.lbl_dogovor.text()} от {widget.ui.lbl_date_set_arenda.text()} ?")

		self.buttonAceptar = self.msg.addButton("Да, хочу", QMessageBox.YesRole)
		self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)
		self.msg.setDefaultButton(self.buttonAceptar)

		for button in self.msg.buttons():
			button.setCursor(QCursor(Qt.PointingHandCursor))

		self.msg.exec_()

		if self.msg.clickedButton() == self.buttonAceptar:
			self.effect.setEnabled(False)
			widget.setStyleSheet("background: #393939; color: yellow;")
			widget.ui.btn_close_contract.setIcon(QIcon(':/Icons/icons/lock_.svg'))
			widget.ui.btn_close_contract.setEnabled(False)

			responce = self.users_db.close_contract(ids=widget.ui.lbl_dogovor.text().split(' ')[1], id_ts=int(widget.ui.lbl_id_ts.text()), vikup=True if widget.ui.lbl_vikup.text() != '' else False)

			widget.get_status_contract(status=responce)
		elif self.msg.clickedButton() == self.buttonCancelar:
			self.effect.setEnabled(False)
			self.msg.close()
		else:
			self.effect.setEnabled(False)
			self.msg.close()


	@pyqtSlot()
	def get_areandator_contracted(self):
		widget = self.sender()

		# self.list_fields_from_dogovor = widget.list_fields_arendators()

		arendator_card = ArendatorWindow(id_arendator = int(widget.ui.lbl_id_arendator.text()), parent=self, role=self.role)
		arendator_card.show()

	@pyqtSlot()
	def update(self) -> None:
		print('UPDATERRRRRRRRRRRRRRRRRRRR')
		self.loadingListArendators(self.list_arendators)


	def clear_all_filters(self):
		def search_filter(layout):
			for i in reversed(range(layout.count())):
				layoutItem = layout.itemAt(i)
				if type(layoutItem) is QSpacerItem:
					continue

				if layoutItem.widget() is not None:
					widgetToFilter = layoutItem.widget()
					if isinstance(widgetToFilter, QComboBox):
						widgetToFilter.setCurrentIndex(0)

					if isinstance(widgetToFilter, QLineEdit):
						widgetToFilter.clear()

					if isinstance(widgetToFilter, QCheckBox):
						widgetToFilter.setChecked(False)

					if isinstance(widgetToFilter, QGroupBox):
						for item in widgetToFilter.findChildren(QRadioButton):
							if item.objectName().endswith('___all'):
								item.setChecked(True)
				else:
					layoutToFilter = layout.itemAt(i)
					search_filter(layoutToFilter)

		search_filter(self.ui.layoutFiltersContracts)
		self.filters_fields_in_db()


	def add_new_client(self):
		self.new_client = ArendatorWindow(parent=self, role=self.role)
		self.new_client.show()









	# def on_select_currentData (self, ix):
	# 	print("currentIndex:", ix)
	# 	print("currentData:", self.ui.date_contract.currentData())
	# 	print("currentText:", self.ui.date_contract.currentText())

	# def onClickedStatus(self):
	# 	radioBtn = self.sender()
	# 	if radioBtn.isChecked():
	# 		# self.label2.setText("You live in " + radioBtn.text())
	# 		# print(radioBtn.text())
	# 		return radioBtn.objectName(), True
	#
	# def onClickedDate(self):
	# 	radioBtn = self.sender()
	# 	if radioBtn.isChecked():
	# 		# self.label2.setText("You live in " + radioBtn.text())
	# 		print(radioBtn.text())



