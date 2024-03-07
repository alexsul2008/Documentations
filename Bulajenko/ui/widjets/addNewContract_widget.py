# -*- coding: utf-8 -*-
import datetime

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QComboBox, QSpacerItem, QLineEdit, QCheckBox

from Core.Utils.utils import date_temp_payment
from Core.WordToPython.WordToPython import CreateDogovor
from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications
from ui.pages.windowPaymentArendator import PaymentArendatorWindow
from ui.windows.ui_widgetItemNewContract import Ui_widgetItemNewContract

from Core.Models.Worker import Usuarios


class AddNewContractWidget(QWidget):
	delete_contract_widget = pyqtSignal(int)

	def __init__ (self, id_widget_new_contract: int, parent=None):
		super(AddNewContractWidget, self).__init__(parent)
		self.ui = Ui_widgetItemNewContract()
		self.ui.setupUi(self)

		self.parent = parent
		self.list_selected_ts = []


		self.id_widget_new_contract = id_widget_new_contract
		self.id_arendator = self.parent.ui.lbl_arendator_id.text()

		self.ui.btn_confirm_pay.setEnabled(False)
		self.ui.btn_create_dogovor.setEnabled(False)

		self.users_db = Usuarios()
		self.responses = Responses()
		self.verify = Verifications()

		# Установка поля Дата договора в текущий день
		self.ui.lbl_date_set_arenda.setText(f'{datetime.date.today().strftime("%d.%m.%Y")}')

		# Combobox с выбором Типа ТС
		self.ui.cb_type_ts.addItem('')
		for item in self.users_db.type_transport():
			self.ui.cb_type_ts.addItem(item.name, item.id)

		# # Combobox с выбором Марки ТС
		# for item in self.users_db.select_ts(int(self.ui.cb_type_ts.currentData())):
		# 	self.ui.cb_brand_ts.addItem(item.brand)

		# # Combobox с выбором VIN ТС
		# for item in self.users_db.select_ts_vin(self.ui.cb_brand_ts.currentText()):
		# 	self.ui.cb_vin.addItem(item.bodywork, item.id)

		self.ui.cb_vin.currentIndexChanged.connect(self.selected_id_ts)

		self.ui.cb_type_ts.currentIndexChanged.connect(self.on_list_brand_ts_currentData)
		self.ui.cb_brand_ts.currentTextChanged.connect(self.on_list_models_ts_currentText)

		self.ui.le_rental_period.editingFinished.connect(self.field_inputs_rental_and_size_pay)
		self.ui.le_size_pay.editingFinished.connect(self.field_inputs_rental_and_size_pay)

		# Установка частоты оплаты согласно выброного периода из выпадающего списка
		self.ui.lbl_period_pay.setText(self.ui.cb_method_pay.currentText().lower())
		self.ui.cb_method_pay.currentTextChanged.connect(self.setMetodPay)

		self.ui.btn_cancel_new_contract.clicked.connect(self.pess_delete_new_contractwidget)
		self.ui.btn_create_dogovor.clicked.connect(self.create_dogovor)
		self.ui.btn_confirm_pay.clicked.connect(self.form_confirm_pay)


	def create_dogovor(self):
		item_fields_dogovor = self.create_list_fields_dogovor()
		id_dogovor, responce = self.users_db.create_or_update_dogovor(list_fields = item_fields_dogovor)

		item_fields_dogovor['id_contract'] = id_dogovor[0]

		self.list_temporary_item, self.period = date_temp_payment(date_dogovor=item_fields_dogovor['date_contract'],
										method_pay=item_fields_dogovor['method_pay'],
										rental_period=item_fields_dogovor['rental_period'],
										id_dogovor=id_dogovor[0])

		# print(f'Temporary period in dogovor: {self.list_temporary_item}')
		# print(f'Finished period in dogovor: {self.period}')

		self.users_db.temporary_payment(self.list_temporary_item)
		self.users_db.create_or_update_dogovor(ids=id_dogovor[0], date_finish_contract = self.period)

		self.ui.lbl_id_dogovor.setText(str(id_dogovor[0]))
		self.ui.btn_cancel_new_contract.setEnabled(False)
		self.ui.btn_create_dogovor.setHidden(True)

		# CreateDogovor(item_fields_dogovor)
		CreateDogovor(fields=item_fields_dogovor, tpl="contract_tpl.docx")


	def create_list_fields_dogovor(self):
		if self.ui.chb_vikup.isChecked():
			self.vikup = True
		else:
			self.vikup = False

		equipments = []
		def equipments_item (layout):
			# for i in reversed(range(layout.count())):
			for i in range(layout.count()):
				layoutItem = layout.itemAt(i)
				if type(layoutItem) is QSpacerItem:
					continue

				if layoutItem.widget() is not None:
					item = layoutItem.widget()

					if isinstance(item, QCheckBox):
						if item.isChecked():
							equipments.append(item.text().strip())
						else:
							equipments.append(' ')

					if isinstance(item, QLineEdit):
						if item.text() != '':
							equipments.append(item.text().strip())
				else:
					layoutToFilter = layout.itemAt(i)
					equipments_item(layoutToFilter)

		equipments_item(self.ui.equipments_layout)

		self.optional_equipment = ', '.join(equipments)

		# print(f'Data selected TS: {self.list_selected_ts}')

		list_fields_dogovor = {
			'date_contract': datetime.datetime.now(),
			'rental_period': f'{self.ui.le_rental_period.text().strip()} {self.ui.cb_rental_period.currentText().lower()}',
			'size_pay': self.ui.le_size_pay.text().strip(),
			'method_pay': self.ui.cb_method_pay.currentText().lower(),
			'vikup': self.vikup,
			'id_ts': self.ui.lbl_id_ts.text(),
			'optional_equipment': self.optional_equipment,
			'fio_arendator': f'{self.parent.ui.le_surname.text().strip().title()} {self.parent.ui.le_name.text().strip().title()} {self.parent.ui.le_last_name.text().strip().title()}',
			'id_arendator': self.id_arendator,
			'id_contract': 0,
			'address_registration': self.parent.ui.le_address_registration.text().strip(),
			'address_residence': self.parent.ui.le_address_residence.text().strip(),
			'passport_country': self.parent.ui.le_country.text().strip(),
			'serial_pasport': self.parent.ui.le_seria_pasport.text().strip(),
			'number_pasport': self.parent.ui.le_number_pasport.text().strip(),
			'date_pasport': self.parent.ui.de_date_pasport.date().toPyDate(),
			'who_issued': self.parent.ui.le_who_issued.text().strip(),
			'date_birthday': self.parent.ui.de_date_birthday.date().toPyDate(),
			'type_ts': self.ui.cb_type_ts.currentText(),
			'brand_ts': self.ui.cb_brand_ts.currentText(),
			'ts_vin': self.ui.cb_vin.currentText(),
			'model_ts': self.list_selected_ts[0],
			'engine_volume': self.list_selected_ts[1],
			'ts_color_name': self.list_selected_ts[2],
			'market_price': self.list_selected_ts[3],
			'phones': '',
			'phones_new': self.list_phones_arendator()
		}
		return list_fields_dogovor


	def list_phones_arendator(self):
		item_phones = []

		def phones_item(layout):
			for i in range(layout.count()):
				layoutItem = layout.itemAt(i)
				if type(layoutItem) is QSpacerItem:
					continue

				if layoutItem.widget() is not None:
					item = layoutItem.widget()

					if item.ui.le_phone.text() != '':
						item_phones.append(item.ui.le_phone.text().strip())
				else:
					layoutToFilter = layout.itemAt(i)
					phones_item(layoutToFilter)

		phones_item(self.parent.ui.phones_arendator_layout)
		# print(f'Phones: {item_phones}')
		return item_phones



	def field_inputs_rental_and_size_pay(self):
		self.responses.clear_msg(self.ui.lbl_msg_period, self.ui.lbl_msg_period, True)
		self.ui.le_rental_period.setStyleSheet('border: none;')

		self.responses.clear_msg(self.ui.lbl_msg_size, self.ui.lbl_msg_size, True)
		self.ui.le_size_pay.setStyleSheet('border: none;')


	def form_confirm_pay(self):
		if self.ui.le_rental_period.text() == '':
			self.ui.lbl_msg_period.setHidden(False)
			self.ui.le_rental_period.setStyleSheet('border-bottom: 2px solid red;')
			self.responses.raise_error(self.ui.lbl_msg_period, 'Обязательно для заполнения.')
			return

		if self.ui.le_size_pay.text() == '':
			self.ui.lbl_msg_size.setHidden(False)
			self.ui.le_size_pay.setStyleSheet('border-bottom: 2px solid red;')
			self.responses.raise_error(self.ui.lbl_msg_size, 'Обязательно для заполнения.')
			return

		self.fio_arendator = f'{self.parent.ui.le_surname.text().strip()} {self.parent.ui.le_name.text().strip()} {self.parent.ui.le_last_name.text().strip()}'
		self.payment_tarif = f'{self.ui.le_size_pay.text().strip()} {self.ui.cb_method_pay.currentText().lower()}'
		self.id_contract = self.ui.lbl_id_dogovor.text()

		self.parent.effect.setEnabled(True)

		self.confirm_pay = PaymentArendatorWindow(id_arendator = self.id_arendator,
												  id_contract = self.id_contract,
												  fio_arendator_confirm = self.fio_arendator.title(),
												  payment_tarif = self.payment_tarif,
												  windget_parent = self,
												  parent=self.parent
												  )
		self.confirm_pay.show()

	def status_fields(self):
		combo_select_all = []
		for i in range(self.ui.layoutSelectTS.count()):
			combobox = self.ui.layoutSelectTS.itemAt(i).widget()
			if isinstance(combobox, QComboBox):
				if combobox.currentIndex() > 0:
					combo_select_all.append(1)

		# if (self.ui.le_rental_period.text() and self.ui.le_size_pay.text()) != '':
		# 	combo_select_all.append(1)

		# if combo_select_all == [1,1,1,1]:
		if combo_select_all == [1,1,1]:
			self.ui.btn_confirm_pay.setEnabled(True)
			self.ui.btn_create_dogovor.setEnabled(True)
		else:
			self.ui.btn_confirm_pay.setEnabled(False)
			self.ui.btn_create_dogovor.setEnabled(False)

		#
		# print(f'Status ComBox: {combo_select_all}')
		# print(f'Status: {combo_select_all == [1,1,1,1]}')


	@pyqtSlot()
	def pess_delete_new_contractwidget(self):
		# print(f'click из pess_delete_new_contractwidget - {self.id_widget_new_contract}')
		self.delete_contract_widget.emit(self.id_widget_new_contract)

	def setMetodPay (self):
		self.ui.lbl_period_pay.setText(self.ui.cb_method_pay.currentText().lower())

	def on_list_brand_ts_currentData(self, ix):
		# print("currentIndex:", ix)
		# print("currentData:", self.ui.cb_type_ts.currentData())
		# print("currentText:", self.ui.cb_type_ts.currentText())
		# self.status_fields()
		self.ui.cb_brand_ts.clear()
		self.ui.cb_brand_ts.addItem('')
		for item in self.users_db.select_ts(int(self.ui.cb_type_ts.currentData())):
			self.ui.cb_brand_ts.addItem(item.brand)

	def on_list_models_ts_currentText(self, ix):
		# print("currentIndex:", ix)
		# # print("currentData:", self.ui.cb_brand_ts.currentData())
		# print("currentText:", self.ui.cb_vin.currentText())
		# self.status_fields()
		self.ui.cb_vin.clear()
		self.ui.cb_vin.addItem('')
		for item in self.users_db.select_ts_vin(self.ui.cb_brand_ts.currentText(), int(self.ui.cb_type_ts.currentData())):
			self.ui.cb_vin.addItem(item.bodywork, (item.id, item.payment_categoryed.size, item.model, item.engine_volume, item.colored.name, item.market_price))


	def selected_id_ts(self):
		self.status_fields()
		data_selected_ts = self.ui.cb_vin.currentData()

		if data_selected_ts != None:
			# print(data_selected_ts[0])
			# print(data_selected_ts[1])
			self.list_selected_ts.append(data_selected_ts[2])
			self.list_selected_ts.append(data_selected_ts[3])
			self.list_selected_ts.append(data_selected_ts[4])
			self.list_selected_ts.append(data_selected_ts[5])

			# print(f'Type: {type(self.list_selected_ts)}')
			# print(f'Data selected TS: {self.list_selected_ts}')

			self.ui.lbl_id_ts.setText(str(data_selected_ts[0]))
			self.ui.le_size_pay.setText(str(data_selected_ts[1]))
			self.ui.lbl_model_ts.setText(str(self.list_selected_ts))

	# def selected_ts_from_vin(self):
	# 	result = self.users_db.selected_ts_from_vin(int(self.ui.cb_type_ts.currentData()), self.ui.cb_brand_ts.currentText())
	# 	# print(result)
	#
	# 	self.ui.cb_brand_ts.clear()
	# 	self.ui.cb_brand_ts.addItem('')
	# 	for item in result['brands']:
	# 		self.ui.cb_brand_ts.addItem(item.brand)
	#
	# 	self.ui.cb_vin.clear()
	# 	for item in result['vins']:
	# 		print(item)
	# 		self.ui.cb_vin.addItem(item.bodywork, item.id)




