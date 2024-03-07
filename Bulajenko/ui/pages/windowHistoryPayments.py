# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsBlurEffect


from Core.Models.Worker import Usuarios
from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications

from ui.widjets.historyPayments_widget import HistoryPaymentsWidget

from ui.windows.ui_HistoryPaymentsWindow import Ui_HistoryPaymentsWindow




class HistoryPaymentsWindow(QMainWindow):

    def __init__(self, ids_arendator:int = None, parent=None):
        super(HistoryPaymentsWindow, self).__init__(parent)
        self.ui = Ui_HistoryPaymentsWindow()
        self.ui.setupUi(self)
        self.statusBar().setStyleSheet('color: #ffffff;')
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'История платежей')


        # Выравнивание окна по центру монитора
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width()) // 2
        y = (desktop.height() - self.frameSize().height()) // 2
        self.move(x, y)

        self.effect = QGraphicsBlurEffect()
        self.effect.setBlurRadius(4)
        self.setGraphicsEffect(self.effect)
        self.effect.setEnabled(False)

        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        self.count_item_list_history_paymets: int = 0

        self.parent = parent
        self.ids_arendator = ids_arendator


        self.ui.lbl_id_arendator.setText(str(self.ids_arendator))

        self.items = self.users_db.list_histored_payments(ids_arendator=self.ids_arendator)
        self.listHistoredPaymets(items = self.items)


    def listHistoredPaymets(self, items=None):
        while self.ui.layoutItemsHistoryPaymets.count() > 0:
            item = self.ui.layoutItemsHistoryPaymets.takeAt(0)
            item.widget().deleteLater()

        for item in items:
            self.count_item_list_history_paymets += 1
            item_historpay = HistoryPaymentsWidget(
                id_widget_base_item_history_paymets=self.count_item_list_history_paymets,
                fields = item,
                parent=self,
            )
            self.ui.layoutItemsHistoryPaymets.addWidget(item_historpay)


    def closeEvent(self, event):
        self.parent.effect.setEnabled(False)