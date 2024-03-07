# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPoint

from Core.Utils.utils import enabled_elements
from ui.pages.windowAdminUsers import AdminWindow
from ui.pages.windowListArendator import ListArendatorsWindow
from ui.pages.windowListTransports import ListTransportsWindow
from ui.pages.windowTransportCard import TransportCardWindow

from ui.windows.ui_widgetBaseMenu import Ui_baseMenu

class ListBtnMenu(QWidget):

	def __init__(self, parent=None, widget_menu = None, role=None):
		super(ListBtnMenu, self).__init__(parent)
		self.ui = Ui_baseMenu()
		self.ui.setupUi(self)

		self.parent = parent
		self.role = role
		self.setStyleSheet('''
			QWidget{
				background-color: rgba(25, 25, 25, 210);
			}
			QPushButton:hover{
				background-color: orange;
			}
		''')

		# self.ui.verticalFrame.setStyleSheet('border: 1px solid red;')

		# self.setAutoFillBackground(True)
		# palette = self.palette()
		# palette.setColor(palette.Window, QColor(240, 240, 240))
		# self.setPalette(palette)

		# self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		# self.setWindowFlags(self.windowFlags())
		# self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
		# self.setAttribute(Qt.WA_TranslucentBackground, True)

		point = widget_menu.rect().bottomLeft()
		# global_point = widget_menu.mapToGlobal(point)
		# self.move(global_point - QPoint(self.width(), self.rect().height()))
		self.move(point + QPoint(5, 15))
		# print(point)
		# print(point + QPoint(0, 10))
		# self.move(global_point)

		# print('Widget_menu: ', widget_menu.rect())
		# print('Point: ', point)
		# print('Global_point: ', global_point)
		# print('widget_menu.rect(): ', widget_menu.rect())
		# print('self.parent: ', self.parent.ui.frm_content.height())
		# print('self.parent.geometry(): ', self.parent.ui.frm_content.geometry().height())
		# print('self.parent.central: ', self.parent.ui.frm_content.geometry().height())
		# print('self: ', self.height())


		# self.resize_menu()

		# self.resize(int(self.size().width()), int(self.parent.ui.frm_content.geometry().height()))

		# print('self: old', self.size().width(), self.size().height())
		# print('self: new', self.size().width(), self.size().height())

		enabled_elements(role=self.role, element=self.ui.btn_user, hideted='yes')
		enabled_elements(role=self.role, element=self.ui.btn_add_ts, hideted='yes')

		self.ui.btn_list_arendators.clicked.connect(lambda: self.press_window_list_arendators())
		self.ui.btn_add_arendator.clicked.connect(lambda: self.press_window_add_arendator())
		self.ui.btn_list_ts.clicked.connect(lambda: self.press_window_list_transports())
		self.ui.btn_user.clicked.connect(lambda: self.press_window_list_users())
		self.ui.btn_add_ts.clicked.connect(lambda: self.press_window_add_ts())

		self.parent.resizeBase.connect(self.resize_menu)

	def press_window_add_ts(self):
		self.parent.effect.setEnabled(True)
		self.card_transport = TransportCardWindow(parent=self.parent, role=self.role)
		self.card_transport.show()


	def press_window_list_users(self):
		self.parent.effect.setEnabled(True)
		self.user_manager = AdminWindow(parent=self.parent)
		self.user_manager.show()

	def resize_menu(self):
		self.resize(int(self.size().width()), int(self.parent.ui.frm_content.geometry().height()) + 5)


	def press_window_list_arendators(self):
		# self.parent.ui.layoutContent.addWidget(self.parent.window_list_arendators)
		# print(self.parent)
		self.parent.window_list_arendators = ListArendatorsWindow(role=self.role) #, parent = self.parent)
		self.parent.window_list_arendators.show()

	def press_window_add_arendator(self):
		self.parent.window_add_arendator.show()

	def press_window_list_transports(self):
		self.parent.window_list_transports = ListTransportsWindow(role=self.role)
		self.parent.window_list_transports.show()






