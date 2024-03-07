# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QRadioButton, QApplication, QGraphicsBlurEffect

from Core.Models.Worker import Usuarios
from ui.pages.windowPaymentArendator import PaymentArendatorWindow
from ui.widjets.addNewContract_widget import AddNewContractWidget

from ui.widjets.addPhoneArendator_widget import AddPhoneArendatorWidget
from ui.widjets.itemListContract_widget import ItemListContractWidget

from ui.windows.ui_ArendatorWindow import Ui_ArendatorWindow

from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications


class ArendatorWindow(QMainWindow):
    entered = pyqtSignal()

    def __init__(self, id_arendator = 0, parent=None, role=None, widget_list = None):
        super(ArendatorWindow, self).__init__(parent)
        self.ui = Ui_ArendatorWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Карточка клиента')


        # Выравнивание окна по центру монитора
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width()) // 2
        y = (desktop.height() - self.frameSize().height()) // 2
        self.move(x, y)

        self.parent = parent
        self.role = role
        self.widget_list = widget_list

        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        self.effect = QGraphicsBlurEffect()
        self.effect.setBlurRadius(4)
        self.setGraphicsEffect(self.effect)
        self.effect.setEnabled(False)

        self.id_count_phone: int = 0
        self.id_count_contract: int = 0
        self.id_count_new_contract: int = 0

        self.ui.chb_flag_cliced_new_contract.setChecked(False)

        self.style_base = """
            #groupBox_base{
                background-color: #191919;
                border: 1px solid green;
                border-radius: 2px;
            }
        """


        #
        self.id_arendator = id_arendator

        self.ui.lbl_arendator_id.setText(str(self.id_arendator))

        # Устновка значения Паспорта по умолчанию
        self.checked_passport = self.ui.rb_rf.objectName()
        # Скрываем поле иностранного государства
        # self.ui.le_country.setVisible(False)

        if self.id_arendator != 0:
            self.field_arendator(self.users_db.get_arendator(ids = self.id_arendator))

        self.listPhonesArendator()

        self.ui.de_date_pasport.calendarWidget().setCursor(Qt.PointingHandCursor)
        self.ui.de_date_birthday.calendarWidget().setCursor(Qt.PointingHandCursor)

        self.ui.btn_save.clicked.connect(self.add_or_update_arendator)
        self.ui.btn_new_contract.clicked.connect(lambda: self.add_new_contracts(self.id_count_new_contract))

        self.ui.rb_rf.toggled.connect(self.onChecked)
        self.ui.rb_inostran.toggled.connect(self.onChecked)



    def field_arendator(self, fields_arendator):
        self.ui.lbl_arendator_id.setText(str(self.id_arendator))
        self.ui.le_surname.setText(fields_arendator.surname.title())
        self.ui.le_name.setText(fields_arendator.name.title())
        self.ui.le_last_name.setText(fields_arendator.last_name.title())
        self.ui.de_date_birthday.setDate(fields_arendator.date_birthday)
        self.ui.de_date_pasport.setDate(fields_arendator.date_pasport)
        self.ui.le_seria_pasport.setText(fields_arendator.serial_pasport)
        self.ui.le_number_pasport.setText(fields_arendator.number_pasport)
        self.ui.le_code_division.setText(fields_arendator.code_division)
        self.ui.le_who_issued.setText(fields_arendator.who_issued)
        self.ui.le_address_registration.setText(fields_arendator.address_registration)
        self.ui.le_address_residence.setText(fields_arendator.address_residence)

        # if fields_arendator.passport_country is not None:
        self.ui.le_country.setText(fields_arendator.passport_country)

        if fields_arendator.driving_license == True:
            self.ui.driving_license.setChecked(True)

        widgets = (self.ui.gridLayout.itemAt(i).widget() for i in range(self.ui.gridLayout.count()))
        for widget in widgets:
            if isinstance(widget, QRadioButton):
                if widget.objectName() == fields_arendator.checked_passport:
                    widget.setChecked(True)

                # if widget.objectName() == 'rb_inostran':
                #     self.ui.le_country.setVisible(True)
                # else:
                #     self.ui.le_country.clear()
                #     self.ui.le_country.setVisible(False)


        self.id_count_phone = 0
        for item in fields_arendator.phoneses:
            self.id_count_phone += 1
            list_phonewidget = AddPhoneArendatorWidget(id_widget_phone = self.id_count_phone, id_arendator = self.id_arendator, phone = item.phone,
                                                       id_phone = item.id)
            list_phonewidget.ui.lbl_count.setText(str(self.id_count_phone))
            self.ui.phones_arendator_layout.addWidget(list_phonewidget)
            list_phonewidget.ui.add_phone.clicked.connect(lambda: self.add_phone_arendator(self.id_count_phone - 1))
            list_phonewidget.editingFinishedPhone.connect(self.editingFinishedPhone_phonewidget)
            list_phonewidget.delete_phone_id.connect(self.delete_phone_phonewidget)



        for item in fields_arendator.contracted:
            self.id_count_contract += 1
            list_contractwidget = ItemListContractWidget(id_widget_contract = self.id_count_contract,
                                                         id_dogovor=item.id,
                                                         date_contract = item.date_contract.strftime("%d.%m.%Y"),
                                                         rental_period = item.rental_period,
                                                         status_contract = item.status_contract,
                                                         confirm_pay = item.confirm_pay,
                                                         draft_contract = item.draft,
                                                         vikup_ts = item.transported.vikup,
                                                         ts = f'{item.transported.brand} {item.transported.model} {item.transported.bodywork}',
                                                         size_pay = item.size_pay,
                                                         method_pay = item.method_pay,
                                                         optional_equipment = item.optional_equipment,
                                                         parent = self
                                                         )
            self.ui.layoutItemFormContract.addWidget(list_contractwidget)
            list_contractwidget.setStyleSheet(self.style_base)
            list_contractwidget.collapse_contract.connect(self.collapse_contractwidget)
            # list_contractwidget.save_draft.connect(self.save_draftwidget)
            list_contractwidget.delete_draft.connect(self.delete_draftwidget)
            list_contractwidget.confirm_draft_pay.connect(self.confirm_draft_paytwidget)


    @pyqtSlot()
    def collapse_contractwidget(self):
        widget = self.sender()
        if widget.ui.btn_collaps.isChecked():
            widget.ui.btn_collaps.setIcon(QIcon(QPixmap(':/Icons/icons/chevron-up_.svg')))
            widget.ui.groupBox_content.setMaximumHeight(206)
        else:
            widget.ui.btn_collaps.setIcon(QIcon(QPixmap(':/Icons/icons/chevron-down_.svg')))
            widget.ui.groupBox_content.setMaximumHeight(0)


    @pyqtSlot()
    def delete_draftwidget(self):
        widget = self.sender()
        self.ui.layoutItemFormContract.removeWidget(widget)
        responce = self.users_db.delete_draft_contract(ids=widget.ui.le_contract_id.text())
        widget.deleteLater()
        widget.destroy()
        # self.id_count_phone = self.ui.phones_arendator_layout.count()
        self.responses.message_from_db(responce, self.statusBar(), f'Черновик успешно удален')


    @pyqtSlot()
    def confirm_draft_paytwidget(self):
        widget = self.sender()

        self.fio_arendator_draft = f'{self.ui.le_surname.text().strip()} {self.ui.le_name.text().strip()} {self.ui.le_last_name.text().strip()}'
        self.payment_tarif_draft = f'{widget.ui.lbl_size_pay.text().strip()} {widget.ui.lbl_method_pay.text()}'
        self.contract_id = widget.ui.le_contract_id.text()

        self.effect.setEnabled(True)

        self.confirm_draft_pay = PaymentArendatorWindow(
            id_arendator = self.id_arendator,
            id_contract = self.contract_id,
            fio_arendator_confirm = self.fio_arendator_draft.title(),
            payment_tarif = self.payment_tarif_draft,
            windget_parent = widget,
            parent = self
        )
        self.confirm_draft_pay.show()


    def listPhonesArendator(self):
        self.id_count_phone = self.ui.phones_arendator_layout.count()
        self.id_count_phone += 1
        if self.ui.phones_arendator_layout.count() == 0:
            add_phonewidget = AddPhoneArendatorWidget(id_widget_phone = self.id_count_phone, id_arendator = '', phone = '', id_phone = '')
            add_phonewidget.ui.lbl_count.setText(str(self.id_count_phone))
            self.ui.phones_arendator_layout.addWidget(add_phonewidget)
            add_phonewidget.editingFinishedPhone.connect(self.editingFinishedPhone_phonewidget)

            self.id_count_phone += 1
            add_phonewidget = AddPhoneArendatorWidget(id_widget_phone = self.id_count_phone, id_arendator = '', phone = '', id_phone = '')
            add_phonewidget.ui.lbl_count.setText(str(self.id_count_phone))
            self.ui.phones_arendator_layout.addWidget(add_phonewidget)
            add_phonewidget.ui.add_phone.clicked.connect(lambda: self.add_phone_arendator(self.id_count_phone))
            add_phonewidget.editingFinishedPhone.connect(self.editingFinishedPhone_phonewidget)


    def add_phone_arendator(self, id_count_phone):
        self.id_count_phone = self.ui.phones_arendator_layout.count() + 1
        add_phonewidget = AddPhoneArendatorWidget(id_widget_phone = self.id_count_phone, id_arendator = '', phone = '', id_phone = '')
        add_phonewidget.ui.lbl_count.setText(str(self.id_count_phone))
        add_phonewidget.ui.lbl_id_phone.setText('')
        self.ui.phones_arendator_layout.addWidget(add_phonewidget)

        add_phonewidget.ui.add_phone.clicked.connect(lambda: self.add_phone_arendator(self.id_count_phone))
        add_phonewidget.editingFinishedPhone.connect(self.editingFinishedPhone_phonewidget)
        add_phonewidget.delete_phone_id.connect(self.delete_phone_phonewidget)

    @pyqtSlot()
    def delete_phone_phonewidget(self):
        widget = self.sender()
        self.ui.phones_arendator_layout.removeWidget(widget)
        responce = self.users_db.delete_phone_arendator(ids=widget.ui.lbl_id_phone.text())
        widget.deleteLater()
        widget.destroy()
        self.id_count_phone = self.ui.phones_arendator_layout.count()
        self.responses.message_from_db(responce, self.statusBar(), f'Телефон успешно удален')

    @pyqtSlot()
    def editingFinishedPhone_phonewidget(self):
        widget = self.sender()
        if widget.ui.le_phone.text() != '':
            if not self.verify.is_phone(widget.ui.le_phone.text().strip()):
                widget.ui.gbx_msg.setHidden(False)
                widget.ui.le_phone.setStyleSheet('border-bottom: 2px solid red;')
                self.responses.raise_error(widget.ui.lbl_msg, 'Указан не корректый телефон. Проверьте введенные данные')
            else:
                widget.ui.le_phone.setStyleSheet('border: none;')
                self.responses.clear_msg(widget.ui.gbx_msg, widget.ui.lbl_msg, True)

    def onChecked (self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.checked_passport = radioButton.objectName()

        if radioButton.objectName() == 'rb_rf':
            self.ui.le_country.setText(f'Гражданин РФ')
        else:
            self.ui.le_country.clear()


    def create_list_fields_arendator(self):
        widgets = (self.ui.phones_arendator_layout.itemAt(i).widget() for i in
                   range(self.ui.phones_arendator_layout.count()))
        phones_arendator = []
        for widget in widgets:
            if widget.ui.le_phone.text().strip() != '':
                id = widget.ui.lbl_id_phone.text() if widget.ui.lbl_id_phone.text() != '' else 0
                phone = widget.ui.le_phone.text().strip()
                phones_arendator.append({'id': id, 'phone': phone})

        if self.ui.driving_license.isChecked():
            self.driving_license = True
        else:
            self.driving_license = False


        for chec in self.ui.gridLayout.findChildren(QRadioButton):
            if chec.isChecked():
                self.checked_passport = chec.objectName()



        list_fields_arendator = {
            'surname': self.ui.le_surname.text().strip(),
            'name': self.ui.le_name.text().strip(),
            'last_name': self.ui.le_last_name.text().strip(),
            'date_birthday': self.ui.de_date_birthday.date().toPyDate(),
            'checked_passport': self.checked_passport,
            'driving_license': self.driving_license,
            'serial_pasport': self.ui.le_seria_pasport.text().strip(),
            'number_pasport': self.ui.le_number_pasport.text().strip(),
            'date_pasport': self.ui.de_date_pasport.date().toPyDate(),
            'code_division': self.ui.le_code_division.text().strip(),
            'who_issued': self.ui.le_who_issued.text().strip(),
            'address_registration': self.ui.le_address_registration.text().strip(),
            'address_residence': self.ui.le_address_residence.text().strip(),
            'phones_arendator': phones_arendator,
            'passport_country': self.ui.le_country.text().strip()
        }
        return list_fields_arendator


    def add_or_update_arendator(self):
        item_list_arendator = self.create_list_fields_arendator()
        arendator_id, responce = self.users_db.create_or_update_arendator(ids=self.ui.lbl_arendator_id.text(), list_fields = item_list_arendator)

        self.ui.lbl_arendator_id.setText(str(arendator_id[0]))

        if responce == 'save':
            self.responses.message_from_db(responce, self.statusBar(), f'Клиент успешно добавлен')
        elif responce == 'update':
            self.responses.message_from_db(responce, self.statusBar(), f'Данные успешно обновлены')
        elif responce == 'error':
            self.responses.message_from_db(responce, self.statusBar(), f'Что-то пошло не так!')


    def add_new_contracts(self, id_count_new_contract):
        self.id_count_new_contract = id_count_new_contract
        self.id_count_new_contract += 1
        add_new_contractwidget = AddNewContractWidget(self, parent=self)
        self.ui.layoutNewFormCreateContract.addWidget(add_new_contractwidget)
        self.ui.chb_flag_cliced_new_contract.setChecked(True)
        self.ui.btn_new_contract.setEnabled(False)
        add_new_contractwidget.delete_contract_widget.connect(self.delete_new_contractwidget)

    @pyqtSlot()
    def delete_new_contractwidget(self):
        widget = self.sender()
        self.ui.layoutNewFormCreateContract.removeWidget(widget)
        widget.deleteLater()
        widget.destroy()

        self.id_count_new_contract -= 1
        self.ui.chb_flag_cliced_new_contract.setChecked(False)
        self.ui.btn_new_contract.setEnabled(True)


    # def clearLayouts (layout):
    #     print(layout)
    #     for i in reversed(range(layout.count())):
    #         print(i)
    #         layout.itemAt(i).widget().close()
    #         layout.takeAt(i)

    def clear_area (self):
        while self.ui.verticalLayout_7.count() > 0:
            # print(f'Count: {self.ui.verticalLayout_7.count()}')
            item = self.ui.verticalLayout_7.takeAt(0)
            item.widget().deleteLater()
            item.widget().destroy()


    def closeEvent(self, event) -> None:
        # self.clearLayouts(self.ui.verticalLayout_7)

        if self.parent is not None:
            self.parent.effect.setEnabled(False)

        if self.widget_list is not None:
            self.widget_list.update()

        self.clear_area()



        # self.close()
        super(ArendatorWindow, self).closeEvent(event)










