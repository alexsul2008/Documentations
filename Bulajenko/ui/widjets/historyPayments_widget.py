# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget

from ui.windows.ui_widgetHistoryPayments import Ui_historyPayments_widget

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


class HistoryPaymentsWidget(QWidget):

    def __init__ (self, id_widget_base_item_history_paymets: int, fields = None, parent = None):
        super(HistoryPaymentsWidget, self).__init__(parent)
        self.ui = Ui_historyPayments_widget()
        self.ui.setupUi(self)

        self.id_widget_base_item_history_paymets = id_widget_base_item_history_paymets

        self.id_contract = fields.id_contract
        self.date_payment = fields.date_payment.strftime("%d.%m.%Y")
        self.total_pay = fields.total_pay
        self.size_payment = fields.size_payment
        self.comment_pay = fields.comment_pay
        self.tarif = fields.tarif
        # self.discount = fields.discount
        if fields.discount != '':
            self.discount = f'{fields.discount} руб.'
        else:
            self.discount = ''
        self.discount_comment = fields.discount_comment
        if fields.shtraf != '':
            self.shtraf = f'{fields.shtraf} руб.'
        else:
            self.shtraf = ''
        # self.shtraf = f'{self.shtraf} руб.' if fields.shtraf != "" else ''
        self.shtraf_comment = fields.shtraf_comment
        self.payments = fields.payments

        self.ui.le_id_contract.setText(str(self.id_contract))
        self.ui.le_date_payment.setText(f'{self.date_payment}г.')
        self.ui.le_total_pay.setText(f'{self.total_pay} руб.')
        self.ui.le_size_payment.setText(f'{self.total_pay} руб.')
        self.ui.le_comment_pay.setText(self.comment_pay)
        self.ui.le_tarif.setText(f'{self.tarif} руб.')
        self.ui.le_discount.setText(self.discount)
        self.ui.le_discount_comment.setText(self.discount_comment)
        self.ui.le_shtraf.setText(self.shtraf)
        self.ui.le_shtraf_comment.setText(self.shtraf_comment)
        self.ui.le_payments.setText(self.payments)