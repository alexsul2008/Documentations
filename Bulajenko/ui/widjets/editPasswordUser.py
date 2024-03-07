# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from Core.Models.Worker import Usuarios
from Login_System.Verifications_and_Responses.Responses import Responses
from ui.windows.ui_EditPassword import Ui_DialogEditPassword


class EditPasswordUser(QDialog):
	def __init__ (self, id_user: int, parent = None, mainwindow = None):
		super(EditPasswordUser, self).__init__(parent)
		self.ui = Ui_DialogEditPassword()
		self.ui.setupUi(self)
		self.id_user = id_user
		self.parent = parent
		self.mainwindow = mainwindow

		self.responses = Responses()
		self.users_db = Usuarios()
		self.setWindowModality(Qt.ApplicationModal)

		self.ui.buttonBox.button(QDialogButtonBox.Save).setText("Сохранить")
		self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText("Отменить")
		self.ui.buttonBox.button(QDialogButtonBox.Cancel).setCursor(QCursor(Qt.PointingHandCursor))


		self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)



		self.ui.Responser.setText(f'{id_user}')

		self.ui.le_repeat_password.textChanged.connect(self.password_equal)


		self.ui.buttonBox.accepted.connect(self.accept_password)
		self.ui.buttonBox.rejected.connect(self.reject_password)

		# print(id_user)

	def password_equal(self):
		if str(self.ui.le_new_password.text().strip()) == str(self.ui.le_repeat_password.text().strip()):
			self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(True)
			self.ui.buttonBox.button(QDialogButtonBox.Save).setCursor(QCursor(Qt.PointingHandCursor))
			print('Пароли совпадают')
		else:
			self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)
			print('Пароли не совпадают')


	def closeEvent (self, event):
		self.mainwindow.effect.setEnabled(False)
		super(EditPasswordUser, self).closeEvent(event)

	def accept_password(self):
		print('Сохранить')
		print(str(self.ui.le_new_password.text().strip()))
		confirmation = self.users_db.update_password(self.id_user, str(self.ui.le_new_password.text().strip()))
		# print(confirmation)
		self.mainwindow.effect.setEnabled(False)
		# self.close()

	def reject_password(self):
		print('Отменить')
		self.mainwindow.effect.setEnabled(False)
		self.close()


		# buttonAceptar = self.ui.buttonBox.addButton(f"Сохранить", QMessageBox.YesRole)
		# buttonCancelar = self.ui.buttonBox.addButton(f"Отменить", QMessageBox.RejectRole)
		# self.setDefaultButton(buttonAceptar)
		# self.exec_()
		#
		# if self.clickedButton() == buttonAceptar:
		# 	print(f'Сохранить виджет {self.id_widget}')
		# 	# self.users_db.delete_roles(widget.ui.le_id.text())
		# 	# self.ui.add_widget_layout_role.removeWidget(widget)
		# 	# widget.deleteLater()
		# 	# widget.destroy()
		# elif self.clickedButton() == buttonCancelar:
		# 	print(f'Отменить виджет {self.id_widget}')