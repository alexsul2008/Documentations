# -*- coding: utf-8 -*-
from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from Core.Models.Worker import Usuarios
from Login_System.Verifications_and_Responses.Responses import Responses

from ui.windows.ui_SetNewDatePayment import Ui_SetNewDatePayment


class SetNewDatePaymentWindow(QMainWindow):

    def __init__(self, id_contract=None, date_old_payment=None, parent=None):
        super(SetNewDatePaymentWindow, self).__init__(parent)
        self.ui = Ui_SetNewDatePayment()
        self.ui.setupUi(self)
        self.statusBar().setStyleSheet('color: #ffffff;')
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Новая дата платежа')

        # Выравнивание окна по центру монитора
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width()) // 2
        y = (desktop.height() - self.frameSize().height()) // 2
        self.move(x, y)

        self.parent = parent
        self.id_contract = id_contract
        self.date_old_payment = date_old_payment

        self.responses = Responses()

        self.users_db = Usuarios()

        self.ui.de_new_date_payment.calendarWidget().setCursor(Qt.PointingHandCursor)

        # print(f'ID contract: {self.id_contract} дата платежа: {self.date_old_payment}')

        self.ui.de_new_date_payment.setDate(datetime.today().date())

        self.ui.btn_cancel.clicked.connect(self.close_form_set_new_date_payment)
        self.ui.btn_save.clicked.connect(self.set_new_date_payment)


    def set_new_date_payment(self):
        responce = self.users_db.set_new_date_payment(id_conract = self.id_contract, new_date_payment = self.ui.de_new_date_payment.date().toPyDate(), old_date_payment = self.date_old_payment)
        self.responses.message_from_db(responce, self.statusBar(), f'Дата платежа успешно изменена')
        if responce == 'update':
            self.ui.btn_cancel.setText(f'Закрыть')
            self.parent.update()


    def close_form_set_new_date_payment(self):
        self.parent.effect.setEnabled(False)
        self.close()

    def closeEvent(self, event):
        self.parent.effect.setEnabled(False)
        super(SetNewDatePaymentWindow, self).closeEvent(event)