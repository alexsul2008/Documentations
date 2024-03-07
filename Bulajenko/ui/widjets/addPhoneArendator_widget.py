# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget

from ui.windows.ui_widjetAddPhoneForm import Ui_widjetAddPhoneForm


class AddPhoneArendatorWidget(QWidget):
	editingFinishedPhone = pyqtSignal(int)
	delete_phone_id = pyqtSignal(int)

	def __init__ (self, id_widget_phone: int, id_arendator: int, id_phone: int, phone = None, parent = None):
		super(AddPhoneArendatorWidget, self).__init__(parent)
		self.ui = Ui_widjetAddPhoneForm()
		self.ui.setupUi(self)

		self.id_widget_phone = id_widget_phone
		self.id_phone = id_phone
		self.parent = parent
		self.id_arendator = id_arendator
		self.phone = phone

		self.ui.gbx_msg.setHidden(True)

		self.ui.delete_phone.setHidden(True)
		if self.id_widget_phone > 2:
			self.ui.delete_phone.setHidden(False)

		self.ui.le_phone.setText(str(self.phone))
		self.ui.lbl_id_phone.setText(str(self.id_phone))

		self.ui.le_phone.editingFinished.connect(self.error_phone)
		self.ui.delete_phone.clicked.connect(self.delete)

	@pyqtSlot()
	def error_phone (self):
		self.editingFinishedPhone.emit(self.id_widget_phone)

	@pyqtSlot()
	def delete (self):
		self.delete_phone_id.emit(self.id_widget_phone)