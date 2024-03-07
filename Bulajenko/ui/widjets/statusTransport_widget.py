# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from ui.windows.ui_widgetStatusTransport import Ui_widgetStatusTransport




class StatusTransportWidget(QWidget):

	clickedStatus = pyqtSignal(int)

	def __init__ (self, id_widget_status: int, id_status: int, name=None, color=None, parent = None):
		super(StatusTransportWidget, self).__init__(parent)
		self.ui = Ui_widgetStatusTransport()
		self.ui.setupUi(self)

		self.id_widget_status = id_widget_status
		self.id_status = id_status
		self.parent = parent
		self.name = name
		self.color = color


		self.ui.lbl_id.setText(str(self.id_status))
		self.ui.lbl_color.setText(self.color)
		self.ui.btn_status.setText(self.name)
		self.ui.btn_status.setStyleSheet(f"border: none; background-color: %s;" % (self.color))

		self.ui.btn_status.clicked.connect(self.press_status)

	@pyqtSlot()
	def press_status(self):
		print('Из StatusTransportWidget press_status: ', self.id_widget_status)
		# print('Из StatusTransportWidget press_status: ', self.id_status, self.name, self.color)
		self.clickedStatus.emit(self.id_widget_status)





# self.hover_color = hex(int(str(self.color).lstrip('#'), 16) - 0x000030).lstrip('0x')
# if len(self.hover_color) == 4:
# 	self.hover_color = '#00' + self.hover_color
# elif len(self.hover_color) == 5:
# 	self.hover_color = '#0' + self.hover_color
# else:
# 	self.hover_color = '#' + self.hover_color

# style = f"""
# 			QPushButton{{"border: none; background-color: %s;"}}
# 			QPushButton:hover{{"background-color: %s;"}}
# 		""" % (self.color, self.hover_color)



