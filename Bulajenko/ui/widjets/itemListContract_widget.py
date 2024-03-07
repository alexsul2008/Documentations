# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QCheckBox

from ui.windows.ui_widgetItemListContract import Ui_widgetItemNewContract

class ItemListContractWidget(QWidget):
	collapse_contract = pyqtSignal(int)
	delete_draft = pyqtSignal(int)
	confirm_draft_pay = pyqtSignal(int)

	def __init__ (self, id_widget_contract: int,
				  id_dogovor: int,
				  status_contract: bool,
				  confirm_pay: bool,
				  draft_contract: bool,
				  vikup_ts: bool,
				  date_contract = None,
				  rental_period = None,
				  size_pay = None,
				  method_pay = None,
				  optional_equipment = None,
				  ts = None,
				  parent = None
			):
		super(ItemListContractWidget, self).__init__(parent)
		self.ui = Ui_widgetItemNewContract()
		self.ui.setupUi(self)
		icon_down = QPixmap(':/Icons/icons/chevron-down_.svg')
		self.ui.btn_collaps.setIcon(QIcon(icon_down))
		self.ui.groupBox_content.setMaximumHeight(0)
		self.ui.btn_delete.setHidden(True)

		self.parent = parent

		self.id_arendator = self.parent.ui.lbl_arendator_id.text()
		self.id_widget_contract = id_widget_contract
		self.status_contract = status_contract
		self.confirm_pay = confirm_pay
		self.draft_contract = draft_contract
		self.vikup_ts = vikup_ts
		self.rental_period = rental_period
		self.size_pay = size_pay
		self.method_pay = method_pay
		self.optional_equipment = optional_equipment
		self.ts = ts

		# self.users_db = Usuarios()
		# self.responses = Responses()
		# self.verify = Verifications()

		# print(f'Договор № {id_dogovor} статус договора: {status_contract} - состояние: {draft_contract} - выкуп ТС: {vikup_ts}')
		self.style_draft = """
			#groupBox_base{
				background-color: orange;
				border: 1px solid red;
				border-radius: 2px;
			}
		"""
		self.style_closed = """					
			#groupBox_base{
				background-color: #505050;
				border: 1px solid green;
				border-radius: 2px;
			}
		"""

		self.ui.le_contract_id.setText(str(id_dogovor))
		self.ui.lbl_date_set_arenda.setText(f'{date_contract}')
		self.ui.lbl_rental_period.setText(self.rental_period)
		self.ui.lbl_method_pay.setText(self.method_pay)
		self.ui.le_size_pay.setText(str(self.size_pay))
		self.ui.le_ts.setText(self.ts)

		# btn_confirm_pay

		if self.confirm_pay == True:
			self.ui.btn_confirm_pay.setEnabled(False)

		if self.draft_contract == True:
			self.ui.btn_delete.setHidden(False)
			self.ui.groupBox_base.setStyleSheet(self.style_draft)


		checkboxes = (self.ui.checkboxes_layout.itemAt(i).widget() for i in range(self.ui.checkboxes_layout.count()))
		for check in checkboxes:
			if isinstance(check, QCheckBox):
				if check.text() in self.optional_equipment.split(', ')[:4]:
					check.setChecked(True)

		optional_equipment_string = ', '.join(map(str, self.optional_equipment.split(', ')[4:]))
		self.ui.le_equipment.setText(optional_equipment_string)


		if self.status_contract == True:
			self.ui.lbl_status_contact.setText('Закрыт')
			self.ui.groupBox_base.setStyleSheet(self.style_closed)
			self.ui.groupBox_actions.setHidden(True)
		elif self.draft_contract == True:
			self.ui.lbl_status_contact.setText('Черновик')
		else:
			self.ui.lbl_status_contact.setText('Действующий')



		if self.vikup_ts == True:
			self.ui.lbl_vikup.setText('выкуп')


		self.ui.btn_collaps.clicked.connect(self.press_collapse_contract)
		self.ui.btn_delete.clicked.connect(self.press_delete_draft_dogovor)

		self.ui.btn_confirm_pay.clicked.connect(self.press_confirm_draft_pay)




	@pyqtSlot()
	def press_collapse_contract(self):
		self.collapse_contract.emit(self.id_widget_contract)


	@pyqtSlot()
	def press_delete_draft_dogovor(self):
		self.delete_draft.emit(self.id_widget_contract)

	@pyqtSlot()
	def press_confirm_draft_pay (self):
		# print(f'Click in press_confirm_draft_pay - {self.id_widget_contract}')
		self.confirm_draft_pay.emit(self.id_widget_contract)






