# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from ui.windows.ui_widgetColorTransport import Ui_widgetColorTransport




class ColorTransportWidget(QWidget):

	clickedColor = pyqtSignal(int)

	def __init__ (self, id_widget_color: int, id_color: int, name=None, color=None, parent = None):
		super(ColorTransportWidget, self).__init__(parent)
		self.ui = Ui_widgetColorTransport()
		self.ui.setupUi(self)

		self.id_widget_color = id_widget_color
		self.id_color = id_color
		self.parent = parent
		self.name = name
		self.color = color


		self.ui.lbl_id.setText(str(self.id_color))
		self.ui.lbl_color.setText(self.color)
		self.ui.btn_name.setText(self.name)
		self.ui.btn_name.setStyleSheet(f"border: none; background-color: %s;" % (self.color))

		self.ui.btn_name.clicked.connect(self.press_color)

	@pyqtSlot()
	def press_color(self):
		# print('Из ColorTransportWidget press_status: ', self.id_widget_color)
		# print('Из StatusTransportWidget press_status: ', self.id_status, self.name, self.color)
		self.clickedColor.emit(self.id_widget_color)





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



