# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot, Signal

from ui.gt_base_ui.ui_widgetFieldAddEmail import Ui_WidgetAddEmailOperator

class AddEmailOperatorWidget(QWidget):
	delete = Signal(int)
	# set_text = Signal(str)
	# textChanged = Signal(str)
	# text = Signal(str)

	# def __init__(self, id_widget: int, email_operator: str, parent=None):
	def __init__ (self, id_widget: int, parent = None):
		super(AddEmailOperatorWidget, self).__init__(parent)
		self.ui = Ui_WidgetAddEmailOperator()
		self.ui.setupUi(self)
		self.id_widget = id_widget
		# self.email_operator = email_operator
		self.ui.lbl_add_email_operator.setText(str(id_widget))
		# self.ui.lineEditNewEmall.setText(str(email_operator))
		self.ui.btn_delete_email_operator.clicked.connect(self.press_del)

	@Slot()
	def press_del(self):
		self.delete.emit(self.id_widget)


	# def line_email_text(self):
	# 	print(self.ui.lineEditNewEmall.textChanged())
		# return self.ui.lineEditNewEmall.text()


