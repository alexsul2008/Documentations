# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Core.Models.Worker import Usuarios

from ui.widjets.addRoleFromUser_widget import AddRoleFormWidget

from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications

from ui.windows.ui_RoleWindow import Ui_RoleWindow


class RoleForm(QMainWindow):
    update_my = pyqtSignal()
    def __init__(self, parent=None):
        super(RoleForm, self).__init__(parent)
        self.ui = Ui_RoleWindow()
        self.ui.setupUi(self)
        self.statusBar().setStyleSheet('color: #ffffff;')
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Редактирование прав доступа пользователя')
        self.parent = parent

        self.setWindowModality(Qt.ApplicationModal)

        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        self.count_id: int = 0

        self.list_roleUsers()

        self.ui.btn_add_role.clicked.connect(lambda: self.add_role_user(self.count_id))


    def closeEvent(self, event) -> None:
        self.parent.effect.setEnabled(False)
        self.update_my.emit()
        super(RoleForm, self).closeEvent(event)


    @pyqtSlot()
    def add_role_user (self, count_id):
        # print('count_id из add_role_user : ', count_id)
        self.count_id = count_id
        self.count_id += 1
        add_rolewidget = AddRoleFormWidget(id_widget = self.count_id, id = '', role = '', name = '')
        self.ui.add_widget_layout_role.addWidget(add_rolewidget)
        add_rolewidget.delete_role.connect(self.delete_rolewidget)
        add_rolewidget.save_role.connect(self.save_rolewidget)
        add_rolewidget.editingFinishedRole.connect(self.editingFinishedRole_userwidget)

    @pyqtSlot()
    def save_rolewidget (self):
        widget = self.sender()
        confirmation = self.users_db.add_roles(role = widget.ui.le_role.text().strip(), name = widget.ui.le_name.text().strip())
        self.responses.success_message_status_bar(self.ui.statusbar, f'Роль доступа: {widget.ui.le_name.text().strip()} - {confirmation}')

    @pyqtSlot()
    def delete_rolewidget (self):
        widget = self.sender()

        self.msg = QMessageBox(self)
        self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.msg.setWindowTitle("Удаление записи")
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setText(f"Вы уверены, что хотите удалить:  {widget.ui.le_role.text().strip()} ?")

        self.buttonAceptar = self.msg.addButton("Да, хочу", QMessageBox.YesRole)
        self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)
        self.msg.setDefaultButton(self.buttonAceptar)

        for button in self.msg.buttons():
            button.setCursor(QCursor(Qt.PointingHandCursor))

        self.msg.exec_()

        if self.msg.clickedButton() == self.buttonAceptar:
            self.users_db.delete_roles(widget.ui.le_id.text())
            self.ui.add_widget_layout_role.removeWidget(widget)
            widget.deleteLater()
            widget.destroy()
        elif self.msg.clickedButton() == self.buttonCancelar:
            pass

        self.update_role()


    @pyqtSlot()
    def editingFinishedRole_userwidget (self):
        widget = self.sender()
        error = self.users_db.get_role_id(widget.ui.le_role.text().strip())
        if error != None:
            widget.ui.gbx_msg.setHidden(False)
            widget.ui.le_role.setStyleSheet('border-bottom: 2px solid red;')
            self.responses.raise_error(widget.ui.lbl_msg, f'Роль доступа: {widget.ui.le_role.text().strip()} - уже существует в БД')
        else:
            widget.ui.le_role.setStyleSheet('border: none;')
            self.responses.clear_msg(widget.ui.gbx_msg, widget.ui.lbl_msg, True)


    def clear_area (self):
        self.count_id = 0
        while self.ui.add_widget_layout_role.count() > 0:
            item = self.ui.add_widget_layout_role.takeAt(0)
            item.widget().deleteLater()
            item.widget().destroy()

    def list_roleUsers(self):
        self.list_role_users = self.users_db.roles()
        for item in self.list_role_users:
            self.count_id += 1
            add_rolewidget = AddRoleFormWidget(id_widget=self.count_id, id=item.id, role=item.role, name=item.name)
            self.ui.add_widget_layout_role.addWidget(add_rolewidget)
            add_rolewidget.ui.le_role.setEnabled(False)
            add_rolewidget.delete_role.connect(self.delete_rolewidget)
            add_rolewidget.save_role.connect(self.save_rolewidget)

    def update_role(self) -> None:
        self.clear_area()
        self.list_roleUsers()
