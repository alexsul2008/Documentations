# -*- coding: utf-8 -*-
import datetime

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from Core.Models.Worker import Usuarios
from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications

from ui.windows.ui_PaymentArendatorFromContract import Ui_paymentArendatorFromContract


class PaymentArendatorWindow(QMainWindow):

    def __init__(self, id_arendator: int, id_contract: int, fio_arendator_confirm=None, payment_tarif=None, windget_parent = None, parent=None):
        super(PaymentArendatorWindow, self).__init__(parent)
        self.ui = Ui_paymentArendatorFromContract()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Форма оплаты')
        self.setWindowModality(Qt.WindowModal)

        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        # print('Ok5')
        self.ui.date_payment.setDate(datetime.date.today())


        self.id_arendator = id_arendator
        self.id_contract = id_contract
        self.fio_arendator_confirm = fio_arendator_confirm
        self.payment_tarif = payment_tarif
        self.parent = parent
        self.windget_parent = windget_parent


        self.ui.lbl_id_arendator.setText(str(self.id_arendator))
        self.ui.lbl_id_contract.setText(str(self.id_contract))
        self.ui.lbl_fio_arendator.setText(self.fio_arendator_confirm)
        self.ui.le_payment_tarif.setText(self.payment_tarif)

        self.ui.discount.editingFinished.connect(lambda: self.checking_for_number(self.ui.discount))
        self.ui.shtraf.editingFinished.connect(lambda: self.checking_for_number(self.ui.shtraf))

        self.ui.btn_save.setEnabled(False)

        self.ui.size_payment.installEventFilter(self)


        self.ui.btn_cancel.clicked.connect(self.form_payment_cancel)
        self.ui.btn_save.clicked.connect(self.save_pay_new_contract)



    # Проверка на Число
    def checking_for_number(self, field):

        if self.verify.is_digital(field.text().strip()):
            field.setStyleSheet('border: none;')
        else:
            field.setStyleSheet('border-bottom: 2px solid red;')

    def summa_field(self):
        tarif = int(self.ui.le_payment_tarif.text().split(' ')[0])
        discount = int(self.ui.discount.text()) if self.ui.discount.text() else 0
        shtraf = int(self.ui.shtraf.text()) if self.ui.shtraf.text() else 0
        return str(tarif - discount + shtraf)


    def save_pay_new_contract(self):
        self.confirm_pay = {
            'date_payment': datetime.datetime.now(),
            'size_payment': self.ui.size_payment.text().strip(),
            'comment_pay': self.ui.comment_pay.text().strip(),
            'tarif': self.ui.le_payment_tarif.text().split(' ')[0],
            'discount': self.ui.discount.text().strip(),
            'discount_comment': self.ui.discount_comment.text().strip(),
            'shtraf': self.ui.shtraf.text().strip(),
            'shtraf_comment': self.ui.shtraf_comment.text().strip(),
            'total_pay': self.ui.size_payment.text().strip(),
            'payments': self.ui.cb_payments.currentText(),
            'id_arendator': self.id_arendator,
            'id_contract': self.id_contract
        }
        responce = self.users_db.save_paymend_new_contract(confirm_pay = self.confirm_pay)

        self.responses.message_from_db(responce, self.statusBar(), f'Платеж успешно сохранен.')
        self.ui.btn_save.setEnabled(False)

        if responce == 'save':
            self.windget_parent.ui.btn_confirm_pay.setEnabled(False)
            self.parent.update()



    def form_payment_cancel(self):
        self.parent.effect.setEnabled(False)
        self.close()

    def closeEvent(self, event):
        self.parent.effect.setEnabled(False)
        super(PaymentArendatorWindow, self).closeEvent(event)


    def eventFilter (self, source, event):
        if event.type() == QEvent.FocusIn:
            # size_pay = self.summa_field()
            source.setText(self.summa_field())
            event.accept()
            self.ui.btn_save.setEnabled(True)
        return super().eventFilter(source, event)




