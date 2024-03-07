# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from ui.pages.windowArendator import ArendatorWindow
from ui.windows.ui_widgetFromItemClosedContract import Ui_FormItemClosedContract




class FormItemClosedContract(QWidget):

	clicked_add_doogovor = pyqtSignal(int)

	def __init__ (self, id_widget_item_add_dogovor: int, id_arendator: int, parent = None):
		super(FormItemClosedContract, self).__init__(parent)
		self.ui = Ui_FormItemClosedContract()
		self.ui.setupUi(self)

		self.setStyleSheet('''
			QPushButton:hover{
				background-color: orange;
			}
		''')

		self.parent = parent

		self.id_widget_item_add_dogovor = id_widget_item_add_dogovor
		self.id_arendator = id_arendator

		# print(self.id_arendator)

		self.ui.btn_issue_another.clicked.connect(self.press_clicked_add_doogovor)


	@pyqtSlot()
	def press_clicked_add_doogovor(self):
		arendator_card = ArendatorWindow(id_arendator = self.id_arendator, parent = self.parent)
		arendator_card.add_new_contracts(0)
		arendator_card.show()