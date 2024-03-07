# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMenu, QAction
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt

from ui.widjets.editPasswordUser import EditPasswordUser
from ui.windows.ui_widjetAddUserFromManager import Ui_WidjetAddUserFromManager

from Core.Models.Worker import Usuarios



class AddUserManagerWidget(QWidget):
	delete = pyqtSignal(int)
	save = pyqtSignal(int)
	editingFinishedLogin = pyqtSignal(int)
	editingFinishedEmail = pyqtSignal(int)
	# set_text = Signal(str)
	# textChanged = Signal(str)
	# text = Signal(str)

	def __init__ (self, id_widget: int, id_user: int, role_id: int, username = None, name = None, email = None, password = None, date_created = None, parent = None):
		super(AddUserManagerWidget, self).__init__(parent)
		self.ui = Ui_WidjetAddUserFromManager()
		self.ui.setupUi(self)

		self._createActions()

		self.id_widget = id_widget
		self.parent = parent
		self.id_user = id_user
		self.username = username
		self.name = name
		self.email = email
		self.password = password
		self.date_created = date_created
		self.role_id = role_id

		self.edit_password = EditPasswordUser(self.id_user, parent = self.parent, mainwindow = parent)

		self.ui.le_id.setEnabled(False)
		self.ui.gbx_msg.setHidden(True)


		self.ui.cb_role.clear()

		# for item in ROLES:
		for item in Usuarios.all_roles():
			self.ui.cb_role.addItem(item.name, item.id)
			index = self.ui.cb_role.findText(item.name)
			if item.id == self.role_id:
				self.ui.cb_role.setCurrentIndex(index)

		# Отслеживаем изменение в ComboBox
		# self.ui.cb_role.activated.connect(self.getValueIdRole)

		self.ui.le_id.setText(str(self.id_user))
		self.ui.le_username.setText(self.username)
		self.ui.le_name.setText(self.name)
		self.ui.le_password.setText(self.password)
		self.ui.le_email.setText(self.email)
		self.ui.lbl_date_create.setText(str(self.date_created))

		self.ui.btn_delete.clicked.connect(self.press_del)
		self.ui.btn_save.clicked.connect(self.press_save)
		self.ui.le_username.editingFinished.connect(self.error_login)
		self.ui.le_email.editingFinished.connect(self.error_email)

		self.ui.le_password.setContextMenuPolicy(Qt.CustomContextMenu)
		# self.ui.le_password.customContextMenuRequested.connect(self.__contextMenu)
		self.ui.le_password.customContextMenuRequested.connect(self.__contextMenu)

		self.actionEditPassword.triggered.connect(self.editPasswordUser)

		self.popMenu = QMenu(self)
		self.popMenu.addAction(self.actionEditPassword)
		# self.popMenu.addAction(QAction('test1', self))
		# self.popMenu.addSeparator()
		# self.popMenu.addAction(QAction('test2', self))

	def _createActions (self):
		# File actions
		self.actionEditPassword = QAction(self)
		self.actionEditPassword.setText("&Редактировать пароль")
		self.actionEditPassword.setIcon(QIcon(":/Icons/icons/edit_.svg"))
		# self.actionEditPassword.sender(self.id_widget)


		# self.actionAddUserAdmin = QAction(QIcon(":/Icons/icons/user-plus_.svg"), "&Добавить пользователя...", self)

	def __contextMenu (self, location):
		# show context menu
		self.popMenu.exec_(self.ui.le_password.mapToGlobal(location))
	#
	def editPasswordUser (self):
		self.parent.effect.setEnabled(True)
		self.edit_password.show()

	# def getValueIdRole(self):
	# 	ROLES = updateRolesSql(True)
		# id_us = self.ui.cb_role.itemData(self.ui.cb_role.currentIndex())
		# print(id_us)

	@pyqtSlot()
	def press_del(self):
		# print('Из press_del: ', self.id_widget)
		self.delete.emit(self.id_widget)

	@pyqtSlot()
	def press_save(self):
		# print('Из press_save: ', self.id_widget)
		self.save.emit(self.id_widget)

	@pyqtSlot()
	def error_login(self):
		# print('Из error_login: ', self.id_widget)
		self.editingFinishedLogin.emit(self.id_widget)

	@pyqtSlot()
	def error_email(self):
		# print('Из error_email: ', self.id_widget)
		self.editingFinishedEmail.emit(self.id_widget)





