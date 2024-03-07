# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

from ui.pages.windowPaymentArendator import PaymentArendatorWindow
from ui.pages.windowReturnVehicle import WindowReturnVehicle
from ui.pages.windowSetNewDatePayment import SetNewDatePaymentWindow
from ui.windows.ui_widgetFromItemCurrentContract import Ui_FormItemCurrentContract




class FormItemCurrentContract(QWidget):
	return_vehicle = pyqtSignal(int)
	def __init__ (self, id_widget_arendator_contracted: int, list_fields = None, parent = None):
		super(FormItemCurrentContract, self).__init__(parent)
		self.ui = Ui_FormItemCurrentContract()
		self.ui.setupUi(self)

		self.setStyleSheet('''
					QPushButton:hover{
						background-color: orange;
					}
				''')

		self.parent = parent
		self.id_widget_arendator_contracted = id_widget_arendator_contracted
		self.list_fields = list_fields

		self.ui.btn_return.clicked.connect(self.select_form_returned)
		self.ui.btn_delay.clicked.connect(self.set_new_date_payment)

		self.ui.btn_confirm_pay.clicked.connect(self.confirm_pay)


	def set_new_date_payment(self):
		self.parent.effect.setEnabled(True)
		self.new_date_payment = SetNewDatePaymentWindow(id_contract = self.list_fields['id_contract'], date_old_payment = self.list_fields['dates_payments_next'], parent=self.parent)
		self.new_date_payment.show()


	def select_form_returned(self):
		self.parent.effect.setEnabled(True)
		self.return_vehicle = WindowReturnVehicle(fields = self.list_fields, parent = self.parent)
		self.return_vehicle.show()

	def confirm_pay(self):
		# print(self.list_fields)
		self.parent.effect.setEnabled(True)

		self.payment_tarif_item = f'{self.list_fields["size_pay"]} {self.list_fields["method_pay"]}'

		self.confirm_pay_form = PaymentArendatorWindow(
			id_arendator = self.list_fields['id_arendator'],
			id_contract = self.list_fields['id_contract'],
			fio_arendator_confirm = self.list_fields['fio_arendator'].title(),
			payment_tarif = self.payment_tarif_item,
			windget_parent = self,
			parent = self.parent
		)
		self.confirm_pay_form.show()
