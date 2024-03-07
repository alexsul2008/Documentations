# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from ui.windows.ui_widgetPaymentCategory import Ui_widgetPaymentCategory



class PaymentCategoryWidget(QWidget):
	delete_pcated = pyqtSignal(int)
	save_pcated = pyqtSignal(int)

	def __init__ (self, id_widget_pay_cat: int, id_pcat: int = 0, size=None, parent = None):
		super(PaymentCategoryWidget, self).__init__(parent)
		self.ui = Ui_widgetPaymentCategory()
		self.ui.setupUi(self)

		self.id_widget_pay_cat = id_widget_pay_cat
		self.id_pcat = id_pcat
		self.parent = parent
		self.size = size

		self.ui.lbl_id_pcat.setText(str(self.id_pcat))
		self.ui.le_paymen_category.setText(str(self.size) if self.size else '')

		self.ui.btn_delete_pcat.clicked.connect(self.press_delete_pcated)
		self.ui.btn_save_pcat.clicked.connect(self.press_save_pcated)


	@pyqtSlot()
	def press_delete_pcated (self):
		self.delete_pcated.emit(self.id_widget_pay_cat)

	@pyqtSlot()
	def press_save_pcated (self):
		# print('Из press_save: ', self.id_widget)
		self.save_pcated.emit(self.id_widget_pay_cat)

