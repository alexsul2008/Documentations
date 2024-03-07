# -*- coding: utf-8 -*-
import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox

from Core.Models.Worker import Usuarios
from Core.WordToPython.WordToPython import CreateDogovor

from ui.windows.ui_ReturnVehicleWindow import Ui_WindowReturnVehicle

from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications


class WindowReturnVehicle(QMainWindow):

    def __init__(self, fields=None, parent=None):
        super(WindowReturnVehicle, self).__init__(parent)
        self.ui = Ui_WindowReturnVehicle()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Карточка возврата ТС')
        self.setWindowModality(Qt.WindowModal)

        # Выравнивание окна по центру монитора
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width()) // 2
        y = (desktop.height() - self.frameSize().height()) // 2
        self.move(x, y)

        self.parent = parent
        self.fields = fields

        # print(self.fields)

        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        self.ui.lbl_ts_id.setText(str(self.fields['id_ts']))
        self.ui.lbl_dogovor_id.setText(str(self.fields['id_contract']))
        self.ui.le_fio_arendator.setText(self.fields['fio_arendator'].title())
        self.ui.lbl_ts.setText(self.fields['ts_brand_model'])
        self.ui.lbl_vin_ts.setText(self.fields['ts_vin'])
        self.ui.lbl_color_ts.setStyleSheet(f"border: none; background-color: %s;" % (self.fields['ts_color']))
        self.ui.date_return.setText(str(datetime.date.today().strftime("%d-%m-%Y")))

        # print(self.fields['optional_equipment'])


        checkboxes = (self.ui.checkboxes_layout.itemAt(i).widget() for i in range(self.ui.checkboxes_layout.count()))
        for check in checkboxes:
            if isinstance(check, QCheckBox):
                if check.text() in self.fields['optional_equipment'].split(', ')[:4]:
                    check.setChecked(True)
                else:
                    check.setHidden(True)

        optional_equipment_string = ', '.join(map(str, self.fields['optional_equipment'].split(', ')[4:]))
        if optional_equipment_string != '':
            self.ui.le_equipment.setText(optional_equipment_string)
        else:
            self.ui.le_equipment.setHidden(True)

        status = self.users_db.status_transport()
        for item in status:
            self.ui.cb_status_ts.addItem(item.name, item.id)



        self.ui.btn_close.clicked.connect(self.form_feturned_vehicle_cancel)
        self.ui.btn_save.clicked.connect(self.form_returned_ts)


    def status_flag(self):
        count_checked = 0

        # print(f'Optional: {self.fields["optional_equipment"]}')

        checkboxes = (self.ui.checkboxes_layout.itemAt(i).widget() for i in range(self.ui.checkboxes_layout.count()))
        for check in checkboxes:
            if isinstance(check, QCheckBox):
                if check.text() in self.fields['optional_equipment'].split(', ')[:4]:
                    if (check.isVisible() and check.checkState() == False) == True:
                        count_checked += 1
                        check.setStyleSheet('color: red;')
                    else:
                        check.setStyleSheet('color: white;')

        if count_checked != 0 and len(self.ui.le_size_dolg.text().strip()) == 0:
            flag_confirm = False
        elif len(self.ui.le_prev_mileage.text().strip()) == 0:
            self.responses.raise_alert(self.ui.lbl_error, f'*Обязательно для заполнения.')
            flag_confirm = False

        elif self.ui.le_prev_mileage.text().strip().isdigit() == False:
            self.responses.raise_alert(self.ui.lbl_error, f'*Только числовое значение.')
            flag_confirm = False
        elif len(self.ui.le_size_dolg.text().strip()) != 0 and self.ui.le_size_dolg.text().strip().isdigit() == False:
            self.responses.raise_alert(self.ui.lbl_error_2, f'*Только числовое значение.')
            flag_confirm = False
        else:
            flag_confirm = True
        return flag_confirm



    def form_returned_ts(self):

        self.flag = self.status_flag()

        if self.flag == True:

            self.returned_ts = {
                'id_ts': int(self.ui.lbl_ts_id.text()),
                'prev_mileage': int(self.ui.le_prev_mileage.text().strip()),
                'status_ts': int(self.ui.cb_status_ts.currentData()),
                'date_closed_contract': datetime.datetime.now(),
                'id_dogovor': int(self.ui.lbl_dogovor_id.text())
            }

            responce = self.users_db.returnet_ts(returned = self.returned_ts)

            if responce == 'update':
                self.parent.update()
                self.responses.message_from_db(responce, self.statusBar(), f'Данные успешно сохранены.')
                self.responses.clear([self.ui.lbl_error, self.ui.lbl_error_2])

                # Объединяем два словаря
                self.returned_ts.update(self.fields)

                CreateDogovor(fields=self.returned_ts, tpl="act_returned_ts_tpl.docx", type='act')

            elif responce == 'error':
                self.responses.message_from_db(responce, self.statusBar(), f'Что-то пошло не так!')





    def form_feturned_vehicle_cancel(self):
        self.parent.effect.setEnabled(False)
        self.close()

    def closeEvent(self, event):
        self.parent.effect.setEnabled(False)
        super(WindowReturnVehicle, self).closeEvent(event)



