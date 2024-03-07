# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMainWindow, QAction, QGraphicsBlurEffect, QMessageBox, QColorDialog

from Core.Models.Worker import Usuarios
from ui.pages.windowRoleForm import RoleForm
from ui.widjets.addColorTransport_widget import AddColorTransportWidget

from ui.widjets.addUserManager_widget import AddUserManagerWidget
from ui.widjets.paymentCategory_widget import PaymentCategoryWidget
from ui.widjets.vehicleCategory_widget import VehicleCategoryWidget
from ui.windows.ui_UsersWindow import Ui_AdminSystem

from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications





class AdminWindow(QMainWindow):

    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.ui = Ui_AdminSystem()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Пользователи системы и их права доступа')
        self.setWindowModality(Qt.WindowModal)
        #
        self.parent = parent


        self.effect = QGraphicsBlurEffect()
        self.effect.setBlurRadius(4)
        self.setGraphicsEffect(self.effect)
        self.effect.setEnabled(False)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_NoSystemBackground, True)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.desenfoque = QGraphicsDropShadowEffect()
        # self.desenfoque.setBlurRadius(0.4)

        self._createActions()
        self._createToolBars()

        self.counter_id: int = 0
        self.id_widget_add_color: int = 0
        self.id_widget_pay_cat: int = 0
        self.id_widget_veh_cat: int = 0

        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        self._currect_pages(self.ui.page_users)

        self.listUsersManagers()
        self.listColorsTransport()
        self.listPaymentCategory()
        self.listVehicleCategory()

        # self.actionAddUserAdmin.triggered.connect(lambda: self.add_user_admin(self.counter_id))
        self.actionAddUserAdmin.triggered.connect(lambda: self._currect_pages(self.ui.page_users))
        self.actionsAccessRights.triggered.connect(self.add_role_from_admin)
        self.actionsSettings.triggered.connect(lambda: self._currect_pages(self.ui.page_settings))

        # self.update_my.connect(self.update)
        self.role_user = RoleForm(parent = self)
        self.role_user.update_my.connect(self.updated)

        self.ui.btn_add_user.clicked.connect(lambda: self.add_user_admin(self.counter_id))

        self.ui.btn_add_color_ts.clicked.connect(self.add_item_color_transport)
        self.ui.btn_add_payment_category.clicked.connect(self.add_item_payment_category)
        self.ui.btn_add_view_ts.clicked.connect(self.add_item_vehicle_category)


    def _createActions(self):
        # File actions
        self.actionsAccessRights = QAction(self)
        self.actionsAccessRights.setText("&Редактировать права доступа")
        self.actionsAccessRights.setIcon(QIcon(":/Icons/icons/lock_.svg"))

        self.actionAddUserAdmin = QAction(QIcon(":/Icons/icons/user-plus_.svg"), "&Добавить пользователя...", self)
        self.actionsSettings = QAction(QIcon(":/Icons/icons/sliders_.svg"), "&Настройки ТС...", self)


    def _createToolBars(self):
        # Toolbar
        self.ui.toolBar.addAction(self.actionsAccessRights)
        self.ui.toolBar.addAction(self.actionAddUserAdmin)
        self.ui.toolBar.addAction(self.actionsSettings)
        # self.ui.toolBar.widgetForAction().setCursor(QCursor(Qt.PointingHandCursor))
        # print(self.ui.toolBar.widgetForAction())

    def _currect_pages(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)


    def add_role_from_admin(self):
        # self._currect_pages(self.ui.page_users)
        self.effect.setEnabled(True)
        self.role_user.show()


    @pyqtSlot()
    def add_user_admin (self, counter_id):
        self.counter_id = counter_id
        self.counter_id += 1
        add_userwidget = AddUserManagerWidget(id_widget = self.counter_id, id_user = '', username = '', name = '', email = '', password = '', role_id = '')
        self.ui.add_widget_layout.addWidget(add_userwidget)
        add_userwidget.delete.connect(self.delete_userwidget)
        add_userwidget.save.connect(self.save_userwidget)
        add_userwidget.editingFinishedLogin.connect(self.editingFinishedLogin_userwidget)
        add_userwidget.editingFinishedEmail.connect(self.editingFinishedEmail_userwidget)


    @pyqtSlot()
    def editingFinishedLogin_userwidget(self):
        widget = self.sender()
        error, _ = self.users_db.get_user_id(widget.ui.le_username.text().strip())
        if error != None:
            widget.ui.gbx_msg.setHidden(False)
            widget.ui.le_username.setStyleSheet('border-bottom: 2px solid red;')
            self.responses.raise_error(widget.ui.lbl_msg, f'Пользователь: {widget.ui.le_username.text().strip()} - уже существует в БД')
        else:
            widget.ui.le_username.setStyleSheet('border: none;')
            self.responses.clear_msg(widget.ui.gbx_msg, widget.ui.lbl_msg, True)

    @pyqtSlot()
    def editingFinishedEmail_userwidget(self):
        widget = self.sender()

        if widget.ui.le_email.text() != '':
            if not self.verify.is_email(widget.ui.le_email.text().strip()):
                widget.ui.gbx_msg.setHidden(False)
                widget.ui.le_email.setStyleSheet('border-bottom: 2px solid red;')
                self.responses.raise_error(widget.ui.lbl_msg, 'Указан не корректый e-mail. Проверьте введенные данные')
            else:
                widget.ui.le_email.setStyleSheet('border: none;')
                self.responses.clear_msg(widget.ui.gbx_msg, widget.ui.lbl_msg, True)

    @pyqtSlot()
    def save_userwidget(self):
        widget = self.sender()

        confirmation = self.users_db.add_user_admin(username = widget.ui.le_username.text().strip(),
                                     name = widget.ui.le_name.text().strip(),
                                     password = widget.ui.le_password.text().strip(),
                                     email = widget.ui.le_email.text().strip(),
                                     role_id = widget.ui.cb_role.itemData(widget.ui.cb_role.currentIndex())
                                )
        self.updated()
        self.responses.success_message_status_bar(self.ui.statusBar, f'Пользователь: {widget.ui.le_username.text().strip()} - {confirmation}')

    @pyqtSlot()
    def delete_userwidget (self):
        widget = self.sender()

        if widget.ui.le_username.text().strip() == '':
            self.ui.add_widget_layout.removeWidget(widget)
            widget.deleteLater()
        else:
            self.effect.setEnabled(True)
            self.msg = QMessageBox(self)
            self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
            self.msg.setWindowTitle("Удаление пользователя")
            self.msg.setIcon(QMessageBox.Question)
            self.msg.setText(f"Вы уверены, что хотите удалить пользователя:  {widget.ui.le_username.text().strip()} ?")

            self.buttonAceptar = self.msg.addButton("Да, хочу", QMessageBox.YesRole)
            self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)
            self.msg.setDefaultButton(self.buttonAceptar)
            self.buttonAceptar.setCursor(QCursor(Qt.PointingHandCursor))
            self.buttonCancelar.setCursor(QCursor(Qt.PointingHandCursor))

            for button in self.msg.buttons():
                button.setCursor(QCursor(Qt.PointingHandCursor))

            self.msg.exec_()

            if self.msg.clickedButton() == self.buttonAceptar:
                # print('Удаляем user с ID: ', widget.ui.le_id.text())
                self.effect.setEnabled(False)
                self.users_db.delete_user_admin(widget.ui.le_id.text())
                self.ui.add_widget_layout.removeWidget(widget)
                widget.deleteLater()
            elif self.msg.clickedButton() == self.buttonCancelar:
                self.effect.setEnabled(False)

    @pyqtSlot()
    def clear_area (self):
        self.counter_id = 0
        while self.ui.add_widget_layout.count() > 0:
            item = self.ui.add_widget_layout.takeAt(0)
            item.widget().deleteLater()
            item.widget().destroy()


    def listUsersManagers(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_users)
        self.list_users_managers = self.users_db.all_users_managers()
        # print(self)
        for item in self.list_users_managers:
            self.counter_id += 1
            add_userwidget = AddUserManagerWidget(id_widget = self.counter_id,
                                                  id_user = item.id,
                                                  username = item.username,
                                                  name = item.name,
                                                  email = item.email,
                                                  password = item.password,
                                                  role_id = item.role_id,
                                                  date_created = item.date_created.strftime("%d-%m-%Y %H:%M"),
                                                  parent = self
                                        )
            self.ui.add_widget_layout.addWidget(add_userwidget)
            add_userwidget.ui.le_username.setEnabled(False)
            add_userwidget.delete.connect(self.delete_userwidget)
            add_userwidget.save.connect(self.save_userwidget)
            add_userwidget.editingFinishedEmail.connect(self.editingFinishedEmail_userwidget)

        # print('Из listUsersManagers после вывода пользователей :  ', self.counter_id)


    def listColorsTransport(self):
        self.list_colors_transport = self.users_db.all_colors_transport()
        # print(self)
        for item in self.list_colors_transport:
            self.id_widget_add_color += 1
            colors_transportwidget = AddColorTransportWidget(id_widget_add_color = self.id_widget_add_color,
                                                  id_color = item.id,
                                                  name = item.name,
                                                  color = item.color,
                                                  parent = self
                                        )
            self.ui.layout_colored_ts.addWidget(colors_transportwidget)

            colors_transportwidget.mouse_lineedit_dbl_click.connect(self.item_mouse_lineedit_dbl_clickwidget)
            colors_transportwidget.delete_colored.connect(self.delete_coloredwidget)
            colors_transportwidget.save_colored.connect(self.save_coloredwidget)


    def add_item_color_transport(self):
        self.id_widget_add_color = self.ui.layout_colored_ts.count() + 1
        add_colorwidget = AddColorTransportWidget(id_widget_add_color = self.id_widget_add_color)
        self.ui.layout_colored_ts.addWidget(add_colorwidget)

        add_colorwidget.mouse_lineedit_dbl_click.connect(self.item_mouse_lineedit_dbl_clickwidget)
        add_colorwidget.delete_colored.connect(self.delete_coloredwidget)
        add_colorwidget.save_colored.connect(self.save_coloredwidget)


    @pyqtSlot()
    def item_mouse_lineedit_dbl_clickwidget (self):
        widget = self.sender()
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            widget.ui.le_hex_color.setText(color.name())
            widget.ui.le_hex_color.setStyleSheet(f"border: none; background-color: %s;" % (color.name()))

    @pyqtSlot()
    def save_coloredwidget (self):
        widget = self.sender()
        ids_color = widget.ui.lbl_id.text() if widget.ui.lbl_id.text() != '' else 0
        responce, ids = self.users_db.add_color_transport(db_ids = ids_color, db_name = widget.ui.le_name_color.text().strip(),
                                                    db_color = widget.ui.le_hex_color.text().strip()
                                                    )
        if responce == 'save':
            widget.ui.lbl_id.setText(str(ids))
            self.responses.message_from_db(responce, self.statusBar(), f'Цвет успешно добавлен')
        elif responce == 'update':
            self.responses.message_from_db(responce, self.statusBar(), f'Цвет успешно обновлен')
        elif responce == 'error':
            self.responses.message_from_db(responce, self.statusBar(), f'Что-то пошло не так!')


    @pyqtSlot()
    def delete_coloredwidget (self):
        widget = self.sender()
        if (widget.ui.le_name_color.text().strip() or widget.ui.le_hex_color.text().strip()) == '':
            self.ui.layout_colored_ts.removeWidget(widget)
            widget.deleteLater()
        else:
            responce, count_ts = self.users_db.delete_color_transport(ids = widget.ui.lbl_id.text())
            if responce == 'deletes':
                self.ui.layout_colored_ts.removeWidget(widget)
                widget.deleteLater()
                self.responses.message_from_db(responce, self.statusBar(), f'Цвет успешно удален')
            elif responce == 'not_deletes':
                self.effect.setEnabled(True)
                self.msg = QMessageBox(self)
                self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
                self.msg.setWindowTitle("Удаление цвета ТС")
                self.msg.setStyleSheet('''
                    QMessageBox{border: 1px solid orange;}
                ''')
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText(f"Вы не можете удалить цвет: {widget.ui.le_name_color.text()}, т.к. он используется в {count_ts}-и ТС")

                self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)
                self.buttonCancelar.setCursor(QCursor(Qt.PointingHandCursor))
                self.msg.exec_()

                if self.msg.clickedButton() == self.buttonCancelar:
                    self.effect.setEnabled(False)
                    self.msg.close()
                else:
                    self.effect.setEnabled(False)
                    self.msg.close()



    def listPaymentCategory(self):
        self.list_payment_category = self.users_db.payment_category_db()
        for item in self.list_payment_category:
            self.id_widget_pay_cat += 1
            self.payment_categorytwidget = PaymentCategoryWidget(
                    id_widget_pay_cat = self.id_widget_pay_cat,
                    id_pcat = item.id,
                    size = item.size,
                    parent = self
                )
            self.ui.layout_payment_category.addWidget(self.payment_categorytwidget)
            #
            self.payment_categorytwidget.delete_pcated.connect(self.delete_pcatedwidget)
            self.payment_categorytwidget.save_pcated.connect(self.save_pcatedwidget)


    def add_item_payment_category(self):
        self.id_widget_payment_category = self.ui.layout_payment_category.count() + 1
        self.payment_categorytwidget = PaymentCategoryWidget(id_widget_pay_cat = self.id_widget_payment_category)
        self.ui.layout_payment_category.addWidget(self.payment_categorytwidget)

        self.payment_categorytwidget.delete_pcated.connect(self.delete_pcatedwidget)
        self.payment_categorytwidget.save_pcated.connect(self.save_pcatedwidget)


    @pyqtSlot()
    def save_pcatedwidget(self):
        widget = self.sender()

        ids_pcat = widget.ui.lbl_id_pcat.text() if widget.ui.lbl_id_pcat.text() != '' else 0
        responce, ids = self.users_db.add_payment_category(db_ids = ids_pcat, db_size = widget.ui.le_paymen_category.text().strip())
        if responce == 'save':
            widget.ui.lbl_id_pcat.setText(str(ids))
            self.responses.message_from_db(responce, self.statusBar(), f'Категория успешно добавлена')
        elif responce == 'update':
            self.responses.message_from_db(responce, self.statusBar(), f'Категория успешно обновлена')
        elif responce == 'error':
            self.responses.message_from_db(responce, self.statusBar(), f'Что-то пошло не так!')

    @pyqtSlot()
    def delete_pcatedwidget(self):
        widget = self.sender()
        if widget.ui.le_paymen_category.text().strip() == '':
            self.ui.layout_payment_category.removeWidget(widget)
            widget.deleteLater()
        else:
            responce, count_pcat = self.users_db.delete_payment_category(ids = widget.ui.lbl_id_pcat.text())
            if responce == 'deletes':
                self.ui.layout_payment_category.removeWidget(widget)
                widget.deleteLater()
                self.responses.message_from_db(responce, self.statusBar(), f'Категория успешно удалена')
            elif responce == 'not_deletes':
                self.effect.setEnabled(True)
                self.msg = QMessageBox(self)
                self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
                self.msg.setWindowTitle("Удаление ценовой категории ТС")
                self.msg.setStyleSheet('''
                        QMessageBox{border: 1px solid orange;}
                    ''')
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText(f"Вы не можете удалить ценовую категорию: {widget.ui.le_paymen_category.text()}, т.к. он используется в {count_pcat}-и ТС")

                self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)

                for button in self.msg.buttons():
                    button.setCursor(QCursor(Qt.PointingHandCursor))

                self.msg.exec_()

                if self.msg.clickedButton() == self.buttonCancelar:
                    self.effect.setEnabled(False)
                    self.msg.close()
                else:
                    self.effect.setEnabled(False)
                    self.msg.close()


    def listVehicleCategory(self):
        self.list_vehicle_category = self.users_db.vehicle_category_db()
        for item in self.list_vehicle_category:
            self.id_widget_veh_cat += 1
            self.vehicle_categorytwidget = VehicleCategoryWidget(
                    id_widget_veh_cat = self.id_widget_veh_cat,
                    id_vehcat = item.id,
                    name = item.name,
                    parent = self
                )
            self.ui.layout_view_ts.addWidget(self.vehicle_categorytwidget)
            #
            self.vehicle_categorytwidget.delete_vehiclecated.connect(self.delete_vehiclecatedwidget)
            self.vehicle_categorytwidget.save_vehiclecated.connect(self.save_vehiclecatedwidget)


    def add_item_vehicle_category(self):
        self.id_widget_veh_cat = self.ui.layout_colored_ts.count() + 1
        self.vehicle_categorytwidget = VehicleCategoryWidget(id_widget_veh_cat = self.id_widget_veh_cat)
        self.ui.layout_view_ts.addWidget(self.vehicle_categorytwidget)

        self.vehicle_categorytwidget.delete_vehiclecated.connect(self.delete_vehiclecatedwidget)
        self.vehicle_categorytwidget.save_vehiclecated.connect(self.save_vehiclecatedwidget)

    @pyqtSlot()
    def save_vehiclecatedwidget (self):
        widget = self.sender()
        ids_vehcat = widget.ui.lbl_id_ts_cat.text() if widget.ui.lbl_id_ts_cat.text() != '' else 0
        responce, ids = self.users_db.add_vehicle_category(db_ids = ids_vehcat, db_name = widget.ui.le_vehicle_category.text().strip())
        if responce == 'save':
            widget.ui.lbl_id_ts_cat.setText(str(ids))
            self.responses.message_from_db(responce, self.statusBar(), f'Категория ТС успешно добавлена')
        elif responce == 'update':
            self.responses.message_from_db(responce, self.statusBar(), f'Категория ТС успешно обновлена')
        elif responce == 'error':
            self.responses.message_from_db(responce, self.statusBar(), f'Что-то пошло не так!')

    @pyqtSlot()
    def delete_vehiclecatedwidget(self):
        widget = self.sender()
        if widget.ui.le_vehicle_category.text().strip() == '':
            self.ui.layout_view_ts.removeWidget(widget)
            widget.deleteLater()
        else:
            responce, count_vehcat = self.users_db.delete_vehicle_category(ids = widget.ui.lbl_id_ts_cat.text())
            if responce == 'deletes':
                self.ui.layout_view_ts.removeWidget(widget)
                widget.deleteLater()
                self.responses.message_from_db(responce, self.statusBar(), f'Категория ТС успешно удалена')
            elif responce == 'not_deletes':
                self.effect.setEnabled(True)
                self.msg = QMessageBox(self)
                self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
                self.msg.setWindowTitle("Удаление категории ТС")
                self.msg.setStyleSheet('''
                                QMessageBox{border: 1px solid orange;}
                            ''')
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText(
                    f"Вы не можете удалить категорию ТС: {widget.ui.le_vehicle_category.text()}, т.к. она используется в {count_vehcat}-и ТС")

                self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)

                for button in self.msg.buttons():
                    button.setCursor(QCursor(Qt.PointingHandCursor))

                self.msg.exec_()

                if self.msg.clickedButton() == self.buttonCancelar:
                    self.effect.setEnabled(False)
                    self.msg.close()
                else:
                    self.effect.setEnabled(False)
                    self.msg.close()





    @pyqtSlot()
    def updated(self) -> None:
        self.clear_area()
        self.listUsersManagers()

    def closeEvent(self, event):
        self.parent.effect.setEnabled(False)
