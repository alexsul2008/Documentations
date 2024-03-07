# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QEvent

from ui.windows.ui_widgetAddColorTransport import Ui_widgetAddColorTransport


# def clickable (widget):
# 	class Filter(QObject):
# 		clicked = pyqtSignal()
# 		def eventFilter (self, obj, event):
# 			if obj == widget:
# 				if event.type() == QEvent.MouseButtonRelease:
# 					if obj.rect().contains(event.pos()):
# 						self.clicked.emit()
# 						# The developer can opt for .emit(obj) to get the object within the slot.
# 						return True
# 			return False
# 	filter = Filter(widget)
# 	widget.installEventFilter(filter)
# 	return filter.clicked


class AddColorTransportWidget(QWidget):
	delete_colored = pyqtSignal(int)
	save_colored = pyqtSignal(int)
	mouse_lineedit_dbl_click = pyqtSignal(int)

	def __init__ (self, id_widget_add_color: int, id_color: int = 0, name=None, color=None, parent = None):
		super(AddColorTransportWidget, self).__init__(parent)
		self.ui = Ui_widgetAddColorTransport()
		self.ui.setupUi(self)

		self.ui.le_hex_color.installEventFilter(self)

		self.id_widget_color = id_widget_add_color
		self.id_color = id_color
		self.parent = parent
		self.name = name
		self.color = color

		self.ui.lbl_id.setText(str(self.id_color))
		self.ui.le_name_color.setText(self.name)
		self.ui.le_hex_color.setText(self.color)
		self.ui.le_hex_color.setStyleSheet(f"border: none; background-color: %s;" % (self.color))

		self.ui.btn_delete.clicked.connect(self.press_del_color)
		self.ui.btn_save.clicked.connect(self.press_save_color)

		# clickable(self.ui.grb_ts).connect(lambda: self.shows_selected_ts(id_ts = self.ui.lbl_id_ts.text()))

	@pyqtSlot()
	def press_del_color (self):
		self.delete_colored.emit(self.id_widget_color)

	@pyqtSlot()
	def press_save_color (self):
		# print('Из press_save: ', self.id_widget)
		self.save_colored.emit(self.id_widget_color)

	def eventFilter(self, obj, event):
		if event.type() == QEvent.MouseButtonDblClick:
			self.mouse_lineedit_dbl_click.emit(self.id_widget_color)
		return super(AddColorTransportWidget, self).eventFilter(obj, event)