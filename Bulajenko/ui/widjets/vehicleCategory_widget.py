# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from ui.windows.ui_widgetVehicleCategory import Ui_widgetVehicleCategory



class VehicleCategoryWidget(QWidget):
	delete_vehiclecated = pyqtSignal(int)
	save_vehiclecated = pyqtSignal(int)

	def __init__ (self, id_widget_veh_cat: int, id_vehcat: int = 0, name=None, parent = None):
		super(VehicleCategoryWidget, self).__init__(parent)
		self.ui = Ui_widgetVehicleCategory()
		self.ui.setupUi(self)

		self.id_widget_veh_cat = id_widget_veh_cat
		self.id_vehcat = id_vehcat
		self.parent = parent
		self.name = name

		self.ui.lbl_id_ts_cat.setText(str(self.id_vehcat))
		self.ui.le_vehicle_category.setText(self.name)

		self.ui.btn_delete_ts_cat.clicked.connect(self.press_delete_vehiclecated)
		self.ui.btn_save_ts_cat.clicked.connect(self.press_save_vehiclecated)


	@pyqtSlot()
	def press_delete_vehiclecated (self):
		self.delete_vehiclecated.emit(self.id_widget_veh_cat)

	@pyqtSlot()
	def press_save_vehiclecated (self):
		# print('Из press_save: ', self.id_widget)
		self.save_vehiclecated.emit(self.id_widget_veh_cat)

