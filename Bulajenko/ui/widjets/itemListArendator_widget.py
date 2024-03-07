# -*- coding: utf-8 -*-
from datetime import datetime
from PyQt5.QtCore import Qt, QEvent, QObject
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from Core.WordToPython.WordToPython import CreateDogovor
from ui.pages.windowTransportCard import TransportCardWindow
from ui.widjets.fromItemClosedContract_widget import FormItemClosedContract
from ui.widjets.fromItemCurrentContract_widget import FormItemCurrentContract
from ui.windows.ui_widgetItemListArendator import Ui_WidgetItemListArendator



def clickable (widget):
	class Filter(QObject):
		clicked = pyqtSignal()
		def eventFilter (self, obj, event):
			if obj == widget:
				if event.type() == QEvent.MouseButtonRelease:
					if obj.rect().contains(event.pos()):
						self.clicked.emit()
						# The developer can opt for .emit(obj) to get the object within the slot.
						return True
			return False
	filter = Filter(widget)
	widget.installEventFilter(filter)
	return filter.clicked


class ItemListArendatorWidget(QWidget):
	clicked_arendator = pyqtSignal(int)
	close_contract = pyqtSignal(int)

	def __init__ (self, id_widget_item_arendator_contracted: int, id_arendator: int, id_contract: int, id_ts: int, draft: bool, fio_arendator, phone, phones, vikup,
				  brand, model, bodywork, market_price, status_contract, date_closed_contract, optional_equipment, method_pay, size_pay, color_ts, ts_color_name,
				  rental_period, set_date_contract, dates_payments_next, address_registration, address_residence,
				  passport_country, serial_pasport,
				  number_pasport, date_pasport, who_issued, date_birthday, type_ts, engine_volume, parent = None, role=None):

		super(ItemListArendatorWidget, self).__init__(parent)
		self.ui = Ui_WidgetItemListArendator()
		self.ui.setupUi(self)

		self.setStyleSheet('''
							QPushButton#btn_close_contract:hover{
								background-color: orange;
							}
						''')

		self.parent = parent
		self.role = role
		self.id_widget_item_arendator_contracted = id_widget_item_arendator_contracted
		self.id_arendator = id_arendator
		self.id_contract = id_contract
		self.id_ts = id_ts
		self.draft = draft
		self.fio_arendator = fio_arendator
		self.status_contract = status_contract
		self.date_closed_contract = date_closed_contract.strftime("%d-%m-%Y")
		self.method_pay = method_pay
		self.size_pay = size_pay
		self.rental_period = rental_period
		self.optional_equipment = optional_equipment
		self.dates_payments_next = dates_payments_next
		self.phone = phone
		self.phones = phones
		self.vikup = vikup
		self.brand = brand
		self.model = model
		self.bodywork = bodywork
		self.color_ts = color_ts
		self.ts_color_name = ts_color_name
		self.market_price = market_price
		self.ts = f'{brand} {model} {bodywork}'
		self.set_date_contract = set_date_contract.strftime("%d-%m-%Y")
		self.date_contract = set_date_contract
		self.address_registration = address_registration
		self.address_residence = address_residence
		self.passport_country = passport_country
		self.serial_pasport = serial_pasport
		self.number_pasport = number_pasport
		self.date_pasport = date_pasport
		self.who_issued = who_issued
		self.date_birthday = date_birthday
		self.type_ts = type_ts
		self.engine_volume = engine_volume

		# self.installEventFilter(self)

		self.ui.lbl_fio_arendator.setCursor(QCursor(Qt.PointingHandCursor))


		self.ui.lbl_id_arendator.setText(str(self.id_arendator))
		self.ui.lbl_id_ts.setText(str(self.id_ts))
		self.ui.lbl_dogovor.setText(f'№ {str(self.id_contract)}')
		self.ui.lbl_fio_arendator.setText(f'{str(self.fio_arendator).title()}')
		self.ui.lbl_size_pay.setText(f'{str(self.size_pay)} руб.')
		self.ui.lbl_metod_pay.setText(self.method_pay)
		self.ui.lbl_transport_model.setText(f'{self.brand} {self.model}')
		self.ui.lbl_transport_vin.setText(f'{self.bodywork}')
		self.ui.lbl_phone.setText(self.phone)
		self.ui.lbl_date_set_arenda.setText(self.set_date_contract)

		self.ui.lbl_next_pay.setText(str(self.dates_payments_next.strftime("%d-%m-%Y") if self.dates_payments_next else ''))

		self.ui.lbl_color_ts.setStyleSheet(f'background-color: {self.color_ts}')

		if self.vikup:
			self.ui.lbl_vikup.setText('выкуп')

		self.get_status_contract(status=self.status_contract)


		# if datetime.fromisoformat(str(self.date_finish_contract)).date() == datetime.now().date():
		# 	self.ui.label_3.setText('Истекла дата договора')

		# print(type(datetime.now().date()))
		# print(type(self.date_finish_contract.strftime("%Y-%m-%d")))
		# print(self.date_finish_contract.strftime("%Y-%m-%d"))
		# print(datetime.fromisoformat(str(self.date_finish_contract.strftime("%Y-%m-%d"))).date())

		self.ui.btn_close_contract.clicked.connect(self.press_close_contract)
		self.ui.btn_dogovor.clicked.connect(self.create_dogovor_arendator)

		clickable(self.ui.grb_ts).connect(lambda: self.shows_selected_ts(id_ts=self.ui.lbl_id_ts.text()))



		# print('Ok5')


	# def eventFilter(self, obj, event):
	# 	child = self.childAt(event.pos())
	# 	# if event.type() == QEvent.MouseButtonPress:
	# 	# 	if event.button() == Qt.LeftButton:
	# 	# 		# If image is left clicked, display a red bar.
	# 	# 		print('one left')
	# 	# 	elif event.button() == Qt.RightButton:
	# 	# 		print('one right')
	# 	# elif event.type() == QEvent.MouseButtonDblClick:
	# 	# if event.type() == QEvent.MouseButtonDblClick:
	# 	if event.type() == QEvent.MouseButtonPress and child == self.ui.lbl_fio_arendator:
	#
	# 		print(child.objectName(), child.text())
	# 		# ts_card = TransportCardWindow(ts_id = self.ui.lbl_id_ts.text(), parent = self.parent)
	# 		# ts_card.show()
	# 	return super(ItemListArendatorWidget, self).eventFilter(obj, event)

	@pyqtSlot()
	def get_status_contract(self, status=False):
		for i in reversed(range(self.ui.buttonsOption_layout.count())):
			self.ui.buttonsOption_layout.takeAt(i).widget().deleteLater()

		if status:
			self.ui.btn_close_contract.setIcon(QIcon(':/Icons/icons/lock_.svg'))
			self.ui.btn_close_contract.setEnabled(False)
			self.setStyleSheet("background-color: #393939;")

			self.ui.label_3.setText(f'Договор')
			self.ui.lbl_date_closed_contract.setText(f'закрыт\n{self.date_closed_contract}')
			self.ui.lbl_next_pay.setText('закрыт')

			button_option = FormItemClosedContract(id_widget_item_add_dogovor = self.id_widget_item_arendator_contracted,
													id_arendator =  self.id_arendator,
													parent = self.parent)
			self.ui.buttonsOption_layout.addWidget(button_option)
		else:
			self.setStyleSheet("background-color: #222222;")

			if self.dates_payments_next is not None:
				# print(f'Contract: {self.id_contract} next pay: {self.dates_payments_next}')
				if datetime.today().date() > self.dates_payments_next:
					self.ui.lbl_date_closed_contract.setText('долг')
					self.ui.lbl_date_closed_contract.setStyleSheet('color: red; font-size: 11pt; font-weight: 600;')
			else:
				self.ui.label_3.setText(f'Истекла дата\nдоговора')
				self.ui.label_3.setStyleSheet('color: orange;')
				self.ui.lbl_next_pay.setMaximumHeight(0)


			if self.draft:
				self.setStyleSheet("background-color: #957b39;")
				self.ui.lbl_date_closed_contract.setText('черновик')
				self.ui.lbl_date_closed_contract.setStyleSheet('color: orange; font-size: 9pt; font-weight: 500;')

			button_option = FormItemCurrentContract(id_widget_arendator_contracted = self.id_widget_item_arendator_contracted,
													list_fields = self.list_fields_arendators(),
													parent = self.parent
													)
			self.ui.buttonsOption_layout.addWidget(button_option)


	def list_fields_arendators(self):
		list_fields = {
			'id_arendator': self.id_arendator,
			'id_contract': self.id_contract,
			'id_ts': self.id_ts,
			'fio_arendator': self.fio_arendator,
			'phones': self.phones,
			'phones_new': '',
			'ts_brand_model': f'{self.brand} {self.model}',
			'brand_ts': self.brand,
			'model_ts': self.model,
			'ts_vin': self.bodywork,
			'market_price': self.market_price,
			'ts_color': self.color_ts,
			'ts_color_name': self.ts_color_name,
			'optional_equipment': self.optional_equipment,
			'size_pay': self.size_pay,
			'method_pay': self.method_pay,
			'dates_payments_next': self.dates_payments_next,
			'date_contract': self.date_contract,
			'set_date_contract': self.set_date_contract,
			'address_registration': self.address_registration,
			'address_residence': self.address_residence,
			'passport_country': self.passport_country,
			'serial_pasport': self.serial_pasport,
			'number_pasport': self.number_pasport,
			'date_pasport': self.date_pasport,
			'who_issued': self.who_issued,
			'date_birthday': self.date_birthday,
			'type_ts': self.type_ts,
			'engine_volume': self.engine_volume,
		}
		return list_fields

	def create_dogovor_arendator(self):
		self.list_fields_from_dogovor = self.list_fields_arendators()
		CreateDogovor(fields=self.list_fields_from_dogovor, tpl="contract_tpl.docx")


	def shows_selected_ts(self, id_ts=None):
		ts_card = TransportCardWindow(ts_id = id_ts, parent = self.parent, role=self.role)
		ts_card.show()

	def mousePressEvent(self, event):
		child = self.childAt(event.pos())
		if child.objectName() == 'lbl_fio_arendator':
			self.clicked_arendator.emit(self.id_widget_item_arendator_contracted)


	@pyqtSlot()
	def press_close_contract(self):
		# print('Из press_close_contract: ', self.id_widget_item_arendator_contracted)
		self.close_contract.emit(self.id_widget_item_arendator_contracted)

	@pyqtSlot()
	def press_get_arendator_contracter(self):
		self.clicked_arendator.emit(self.id_widget_item_arendator_contracted)















