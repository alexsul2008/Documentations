# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from ui.windows.ui_widjetAddRoleFrom import Ui_WidjetAddRoleForm



class AddRoleFormWidget(QWidget):
	delete_role = pyqtSignal(int)
	save_role = pyqtSignal(int)
	editingFinishedRole = pyqtSignal(int)

	def __init__ (self, id_widget: int, id: int, role = None, name = None, parent = None):
		super(AddRoleFormWidget, self).__init__(parent)
		self.ui = Ui_WidjetAddRoleForm()
		self.ui.setupUi(self)

		self.ui.gbx_msg.setHidden(True)

		self.id_widget = id_widget
		self.id = id
		self.role = role
		self.name = name

		self.ui.le_id.setText(str(self.id))
		self.ui.le_role.setText(self.role)
		self.ui.le_name.setText(self.name)

		self.ui.btn_delete.clicked.connect(self.press_del_role)
		self.ui.btn_save.clicked.connect(self.press_save_role)
		self.ui.le_role.editingFinished.connect(self.error_role)

	@pyqtSlot()
	def press_del_role(self):
		# print('Из Role press_del: ', self.id_widget)
		self.delete_role.emit(self.id_widget)

	@pyqtSlot()
	def press_save_role(self):
		# print('Из Role press_save: ', self.id_widget)
		self.save_role.emit(self.id_widget)

	@pyqtSlot()
	def error_role(self):
		# print('Из Role error_role: ', self.id_widget)
		self.editingFinishedRole.emit(self.id_widget)