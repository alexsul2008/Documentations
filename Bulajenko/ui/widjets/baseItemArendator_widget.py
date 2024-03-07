# -*- coding: utf-8 -*-
from PyQt5.QtCore import QEvent, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from Core.Utils.utils import enabled_elements
from ui.windows.ui_BaseItemArendatorWidget import Ui_BaseItemArendatorWidget

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


class BaseItemArendatorWidget(QWidget):
	delete_arendator = pyqtSignal(int)
	clicked_arendator = pyqtSignal(int)
	hidened_arendator = pyqtSignal(bool)
	histored_payments = pyqtSignal(int)

	def __init__ (self, id_widget_base_item_arendator: int, id_arendator: int, count_contracts: int, hiden_arendator_db: bool, surname=None,
				  name=None,
				  last_name=None,
				  date_created=None, role=None, parent = None):
		super(BaseItemArendatorWidget, self).__init__(parent)
		self.ui = Ui_BaseItemArendatorWidget()
		self.ui.setupUi(self)

		self.defaultIcon = QIcon(QPixmap(":/Icons/icons/eye_.svg"))
		self.hoverIcon = QIcon(QPixmap(":/Icons/icons/eye-off_.svg"))
		self.ui.btn_hidened_arendator.setIcon(self.defaultIcon)
		self.ui.btn_hidened_arendator.setIconSize(QSize(30, 30))
		self.ui.btn_hidened_arendator.installEventFilter(self)

		self.role = role
		self.parent = parent
		self.id_widget_base_item_arendator = id_widget_base_item_arendator
		self.id_arendator = id_arendator
		self.hiden_arendator_db = hiden_arendator_db
		self.count_contracts = count_contracts
		self.surname = surname.title()
		self.name = name.title()
		self.last_name = last_name.title()
		self.date_created = date_created.strftime("%d/%m/%Y")
		self.fio = f'{self.surname} {self.name} {self.last_name}'

		if self.id_widget_base_item_arendator % 2 == 0:
			self.setStyleSheet("background-color: #222222;")
		else:
			self.setStyleSheet("background-color: #333333;")

		self.ui.btn_delete.setStyleSheet('''
					#btn_delete{
						border: 1px solid orange;
						border-radius: 3px;
						padding: 0;
					}
					#btn_delete:hover{	
						background-color: #d60000;
						border: 1px solid #d60000;
					}
					#btn_delete:disabled{  
						border: 2px solid qrey;
						color: rgba(195, 195, 195, 200);
						/*change-cursor: cursor('Forbidden');*/
						cursor: not-allowed;
					}
				''')
		self.ui.btn_history_payments.setStyleSheet('''
			#btn_history_payments:hover{	
						background-color: orange;
					}
		''')


		self.ui.lbl_id_arendator.setText(str(self.id_arendator))
		self.ui.lbl_fio_arendator.setText(self.fio)
		self.ui.le_date_registration.setText(self.date_created)
		self.ui.le_count_contract.setText(str(self.count_contracts))

		if self.hiden_arendator_db:
			self.ui.btn_hidened_arendator.setIcon(self.hoverIcon)
			self.ui.btn_hidened_arendator.setStyleSheet("QPushButton{background-color: grey;}")
			self.ui.btn_hidened_arendator.setToolTip(f'Отобразить клиента')
			self.ui.btn_hidened_arendator.setChecked(True)

		enabled_elements(role = self.role, element = self.ui.btn_delete, hideted = 'yes')

		# print(f'{self.fio} - {self.ui.btn_hidened_arendator.isChecked()}')

		self.ui.btn_delete.clicked.connect(self.press_delete_arendator)
		self.ui.btn_hidened_arendator.clicked.connect(self.press_hidened_arendator)
		self.ui.btn_history_payments.clicked.connect(self.press_histored_payments)

	@pyqtSlot()
	def press_histored_payments(self):
		self.histored_payments.emit(self.id_widget_base_item_arendator)

	@pyqtSlot()
	def press_delete_arendator(self):
		# print('Из press_delete_arendator: ', self.id_widget_base_item_arendator)
		self.delete_arendator.emit(self.id_widget_base_item_arendator)

	# @pyqtSlot()
	def press_hidened_arendator(self):
		self.hidened_arendator.emit(self.hiden_arendator_db)

	def mousePressEvent(self, event):
		child = self.childAt(event.pos())
		if child.objectName() == 'lbl_fio_arendator':
			self.clicked_arendator.emit(self.id_widget_base_item_arendator)


	def eventFilter (self, source, event):
		if not self.hiden_arendator_db:
			if event.type() == QEvent.HoverEnter:
				self.ui.btn_hidened_arendator.setIcon(self.hoverIcon)
				self.ui.btn_hidened_arendator.setIconSize(QSize(30, 30))
				self.ui.btn_hidened_arendator.setStyleSheet("QPushButton{background-color: #37be40; border: 1px solid #37be40;}")
			elif event.type() == QEvent.HoverLeave:
				self.ui.btn_hidened_arendator.setIcon(self.defaultIcon)
				self.ui.btn_hidened_arendator.setStyleSheet("QPushButton{background-color: transparent; border: 1px solid orange;}")
		return super(BaseItemArendatorWidget, self).eventFilter(source, event)