# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot, Signal

from ui.gt_base_ui.ui_widgetAdminRow import Ui_widgetListsAdmins


class ListAdminsWidget(QWidget):
	delete_admin = Signal(int)
	save_admin = Signal(int)

	def __init__ (self, id_widget: int, user_id: int = 0, user_name=None): #, parent = None):
		super(ListAdminsWidget, self).__init__()
		self.ui = Ui_widgetListsAdmins()
		self.ui.setupUi(self)

		self.id_widget = id_widget
		self.user_id = user_id
		self.user_name = user_name

		# print(f'ID User from widget: {str(self.user_id)}')
		# self.ui.btn_delete_admin.setStyleSheet(STYLE_HOVER_GREEN)

		self.ui.lbl_id_admin.setText(str(self.user_id))
		self.ui.le_name_admin.setText(self.user_name)

		self.ui.btn_delete_admin.clicked.connect(self.press_delete_admin)
		self.ui.btn_save_admin.clicked.connect(self.press_save_admin)
	#
	#
	@Slot()
	def press_delete_admin (self):
		self.delete_admin.emit(self.id_widget)
	#
	@Slot()
	def press_save_admin (self):
		print('Из press_save: ', self.id_widget)
		self.save_admin.emit(self.id_widget)

