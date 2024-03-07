# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from Core.Models.Models import UPLOAD_FOLDER
from Core.Utils.utils import enabled_elements
from ui.windows.ui_widgetItemListTransport import Ui_WidgetItemListTransport




class ItemListTransportWidget(QWidget):

	delete_ts = pyqtSignal(int)
	mouse_button_dbl_click = pyqtSignal(int)

	def __init__ (self, id_widget_item: int, id_ts: int, contract_number: int,
					brand,
					model,
					bodywork,
					color_name,
					color_hex,
					market_price,
					date_next_to,
					prev_mileage,
					next_mileage,
					image,
					name_status,
					color_status,
				  	payment_categoryed,
					parent = None, role=None):
		super(ItemListTransportWidget, self).__init__(parent)
		self.ui = Ui_WidgetItemListTransport()
		self.ui.setupUi(self)

		self.installEventFilter(self)

		self.parent = parent
		self.role = role

		self.id_widget_item = id_widget_item
		self.id_ts = id_ts
		self.brand = brand
		self.model = model
		self.bodywork = bodywork
		self.color_name = color_name
		self.color_hex = color_hex
		self.prev_mileage = prev_mileage
		self.next_mileage = next_mileage
		self.date_next_to = date_next_to.strftime("%d.%m.%Y")
		self.market_price = market_price
		self.name_status = name_status
		self.color_status = color_status
		self.contract_number = contract_number
		self.payment_categoryed = payment_categoryed
		self.image = os.path.join(UPLOAD_FOLDER, image)

		enabled_elements(role=self.role, element=self.ui.btn_delete, hideted='yes')

		self.ui.lbl_color_ts.setStyleSheet(f"background-color: %s;" % (self.color_hex))
		self.ui.lbl_brand.setText(self.brand)
		self.ui.lbl_model.setText(self.model)
		self.ui.lbl_vin.setText(self.bodywork)
		# self.ui.lbl_color.setText(self.color_name)

		# Следующее ТО дата или пробег
		next_to = f' или {self.next_mileage}км.' if self.next_mileage != '' else ''
		self.ui.lbl_mileage.setText(f'{self.date_next_to}г.{next_to}')

		contract_number = self.contract_number if self.contract_number != 0 else ''
		nomer = '№' if contract_number != '' else ''

		self.ui.lbl_status.setText(f'{self.name_status} {nomer}{contract_number}')
		self.ui.lbl_status.setStyleSheet(f"background-color: %s;" % (self.color_status))

		self.ui.lbl_id_ts.setText(str(self.id_ts))

		prev_to = f'{self.prev_mileage}км.' if self.prev_mileage != '' else 'н/д'
		self.ui.le_prev_milage_list.setText(prev_to)

		self.ui.lbl_price_category.setText(f'{str(self.payment_categoryed)} р./день')

		pixmap = QPixmap(self.image)
		pixmap_resized = pixmap.scaled(self.ui.lbl_photo.width() - 2, self.ui.lbl_photo.height(), Qt.KeepAspectRatio, Qt.FastTransformation)
		self.ui.lbl_photo.setPixmap(pixmap_resized)

		self.ui.btn_delete.clicked.connect(self.press_delete_ts)

	# def eventFilter(self, obj, event):
	#
	# 	# if event.type() == QEvent.MouseButtonPress:
	# 	# 	if event.button() == Qt.LeftButton:
	# 	# 		# If image is left clicked, display a red bar.
	# 	# 		print('one left')
	# 	# 	elif event.button() == Qt.RightButton:
	# 	# 		print('one right')
	# 	# elif event.type() == QEvent.MouseButtonDblClick:
	# 	if event.type() == QEvent.MouseButtonDblClick:
	# 		print(f'Duble Press: {event.type()}')
	# 		self.ts_card = TransportCardWindow(ts_id = self.ui.lbl_id_ts.text(), parent = self.parent, role=self.role)
	# 		self.ts_card.show()
	# 	return super(ItemListTransportWidget, self).eventFilter(obj, event)

	def eventFilter(self, obj, event):
		if event.type() == QEvent.MouseButtonDblClick:
			self.mouse_button_dbl_click.emit(self.id_widget_item)
		return super(ItemListTransportWidget, self).eventFilter(obj, event)

	@pyqtSlot()
	def press_delete_ts (self):
		# print('Из press_delete_ts: ', self.id_widget_item)
		self.delete_ts.emit(self.id_widget_item)





